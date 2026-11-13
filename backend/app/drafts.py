"""Borradores de preguntas redactados con un modelo de lenguaje, para que un docente los revise.

Regla de seguridad: un borrador de origen 'ia' nunca se muestra a estudiantes hasta que un docente lo aprueba,
sin importar la configuración. El modelo propone; quien valida es una persona.
"""
from __future__ import annotations

import json
import random
import time

import httpx
from fastapi import HTTPException

from . import bank
from .catalog import AREAS
from .config import settings
from .db import db, now

GUIDE = {
    "LEC": "Lectura crítica. Escribe primero un texto ORIGINAL de 90 a 130 palabras (no copies textos existentes): puede ser narrativo, "
           "argumentativo, expositivo o un aviso o recibo. Todas las preguntas se responden solo con ese texto.",
    "SOC": "Sociales y ciudadanas. Escribe primero un caso ORIGINAL de 50 a 90 palabras situado en Colombia (un conflicto entre grupos, una "
           "decisión pública, dos fuentes que se contradicen). No cites artículos ni cifras que no estés seguro de que son correctos.",
    "NAT": "Ciencias naturales. Escribe primero una situación ORIGINAL de 40 a 80 palabras (un experimento escolar o un fenómeno cotidiano). "
           "Usa solo ciencia escolar bien establecida.",
    "MAT": "Matemáticas. Escribe primero una situación ORIGINAL de 30 a 70 palabras con datos numéricos sencillos y verifica cada cálculo.",
    "ING": "Inglés, nivel A2 a B1. Escribe primero un texto ORIGINAL en inglés de 70 a 110 palabras. Preguntas y opciones en inglés; "
           "explicación y pistas en español.",
}
SYSTEM = (
    "Eres un constructor de preguntas de selección múltiple para estudiantes colombianos de grado 11. Redactas borradores que revisará un "
    "docente. Reglas: cuatro opciones, una sola correcta e indiscutible; distractores plausibles que correspondan a errores frecuentes; "
    "sin 'todas las anteriores' ni 'ninguna de las anteriores'; lenguaje claro; nada ofensivo; no menciones letras de opciones en la "
    "explicación. Responde SOLO con un objeto JSON con esta forma: "
    '{"contexto": "...", "preguntas": [{"enunciado": "...", "opciones": ["...", "...", "...", "..."], "correcta": 0, '
    '"explicacion": "...", "pistas": ["...", "..."], "dificultad": "baja|media|alta"}]}. '
    "'correcta' es la posición (0 a 3) de la opción correcta. Las pistas orientan sin revelar la respuesta."
)


def _weakest_competencia(area: str) -> str:
    counts = {c: 0 for c in AREAS[area]["competencias"]}
    for it in bank.all_items():
        if it["area"] == area and it.get("pool") in ("practica", "diagnostico") and it.get("status") != "descartado":
            counts[it["competencia"]] = counts.get(it["competencia"], 0) + 1
    return min(counts, key=counts.get)


def _valid(q: dict) -> bool:
    opts = q.get("opciones")
    return (isinstance(q.get("enunciado"), str) and len(q["enunciado"]) > 10 and isinstance(opts, list) and len(opts) == 4
            and all(isinstance(o, str) and o.strip() for o in opts) and len({o.strip().lower() for o in opts}) == 4
            and q.get("correcta") in (0, 1, 2, 3) and isinstance(q.get("explicacion"), str) and len(q["explicacion"]) > 15)


def create(area: str, n: int = 4, call=None) -> dict:
    if area not in AREAS:
        raise HTTPException(404, "Área desconocida.")
    if not settings.groq_api_key and call is None:
        raise HTTPException(409, "Falta la clave de Groq en el servidor (variable GROQ_API_KEY).")
    comp = _weakest_competencia(area)
    label = AREAS[area]["competencias"][comp][0]
    user = f"{GUIDE[area]}\nCompetencia que deben evaluar las preguntas: {label}.\nNúmero de preguntas: {n}."
    try:
        raw = (call or _groq)(SYSTEM, user)
        data = json.loads(raw)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(502, "El modelo no devolvió un borrador utilizable. Intenta de nuevo en un minuto.") from exc
    context = str(data.get("contexto") or "").strip()[:1500] or None
    stamp, batch, saved = format(int(time.time()), "x"), db().batch(), []
    for k, q in enumerate([q for q in data.get("preguntas", []) if isinstance(q, dict) and _valid(q)][:n], start=1):
        order = [0, 1, 2, 3]
        random.shuffle(order)
        item_id = f"{area}-IA-{stamp}-{k}"
        batch.set(db().collection("items").document(item_id), {
            "area": area, "competencia": comp, "pool": "practica", "a": 1.0, "c": 0.25,
            "b": {"baja": -0.6, "media": 0.0, "alta": 0.6}.get(str(q.get("dificultad")).lower(), 0.0),
            "context": context, "stem": q["enunciado"].strip(), "options": {"ABCD"[i]: q["opciones"][j].strip() for i, j in enumerate(order)},
            "correct": "ABCD"[order.index(q["correcta"])], "explanation": q["explicacion"].strip(),
            "hints": [str(h).strip() for h in (q.get("pistas") or []) if str(h).strip()][:3] or ["Vuelve a leer con calma qué te preguntan."],
            "status": "borrador", "origin": "ia", "model": settings.groq_model, "createdAt": now(),
        })
        saved.append(item_id)
    if not saved:
        raise HTTPException(502, "El modelo no devolvió preguntas con el formato correcto. Intenta de nuevo.")
    batch.commit()
    bank.invalidate()
    return {"area": area, "competencia": label, "created": len(saved), "ids": saved}


def _groq(system: str, user: str) -> str:
    resp = httpx.post(
        settings.groq_url, headers={"Authorization": f"Bearer {settings.groq_api_key}"},
        json={"model": settings.groq_model, "temperature": 0.7, "max_tokens": 3500, "response_format": {"type": "json_object"},
              "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
              **({"reasoning_effort": settings.groq_reasoning} if "gpt-oss" in settings.groq_model and settings.groq_reasoning else {})},
        timeout=60,
    )
    if resp.status_code == 429:
        raise HTTPException(429, "Se alcanzó el límite gratuito del modelo. Espera un minuto e intenta de nuevo.")
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
