"""Carga el banco semilla y los simulacros en Firestore."""
from __future__ import annotations

from .. import bank
from ..catalog import AREA_ORDER
from ..db import db, now
from . import bank_lec, bank_more, bank_nat_ing, bank_seed, bank_sim, bank_soc, families  # noqa: F401  (los bank_* agregan sus preguntas al importarse)

# Cada simulacro tiene su propio juego de preguntas. Los tipo examen respetan la proporción por área de la prueba
# (Lectura 41, Matemáticas 50, Sociales 50, Naturales 58, Inglés 55 preguntas) a escala de 60 preguntas.
SIMULACROS = {
    "general-1": {"title": "Simulacro corto", "order": 1},
    "general-2": {"title": "Simulacro tipo examen 1", "order": 2},
    "general-3": {"title": "Simulacro tipo examen 2", "order": 3},
}
MINUTES_PER_QUESTION = 2  # la prueba real da cerca de 2 minutos por pregunta

# Variantes de familias reservadas para cada simulacro tipo examen (se completan con las preguntas escritas de bank_sim).
RESERVED = {
    "general-2": {
        "MAT": ["mediana", "participacion_porcentual", "tasa_de_cambio", "rango_de_datos", "regla_tres_inversa", "interes_simple", "pitagoras",
                "ecuacion_plan", "descuento", "sube_y_baja", "promedio_con_nuevo_dato", "muestra_sesgada"],
        "SOC": ["mecanismo", "mecanismo", "organismo", "organismo"],
        "NAT": ["densidad", "ley_de_ohm", "cruce_genetico", "concentracion", "flota_o_se_hunde", "circuito_en_serie",
                "variables_experimento", "variables_experimento", "conclusion_de_tabla", "grupo_control"],
        "ING": ["vocabulary", "notice", "conversation", "message", "present_simple", "past_simple", "comparative", "time_preposition", "there_is_are"],
    },
    "general-3": {
        "MAT": ["tabla_variacion", "lineal", "mediana", "participacion_porcentual", "proporcion", "cerca_rectangulo", "volumen_tanque",
                "conteo_combinaciones", "tiempo_recorrido", "oferta_comparada", "comparar_fracciones", "media_atipico"],
        "SOC": ["mecanismo", "mecanismo", "organismo", "organismo"],
        "NAT": ["segunda_ley", "energia_trofica", "acidez_suelos", "densidad", "flota_o_se_hunde", "circuito_en_serie",
                "variables_experimento", "promedio_de_mediciones", "conclusion_de_tabla", "grupo_control"],
        "ING": ["vocabulary", "notice", "conversation", "message", "much_many", "question_word", "past_simple", "present_simple", "comparative"],
    },
}


def reserved_items() -> list[dict]:
    taken: set[str] = set()
    out = []
    for sim_id, by_area in RESERVED.items():
        for area in AREA_ORDER:
            names = by_area.get(area, [])
            for k, name in enumerate(names, start=1):
                repeat = names[:k].count(name)  # dos variantes de la misma familia en un simulacro: distintas entre sí
                item = families.reserved(name, f"{sim_id}:{repeat}", 1, taken)[0]
                item.update(id=f"{area}-{sim_id.upper().replace('GENERAL-', 'S')}-F{k:02d}", pool="simulacro", sim=sim_id, status="borrador")
                out.append(item)
    return out


def seed_items() -> list[dict]:
    return list(bank_seed.ITEMS) + families.templates() + reserved_items()


def simulacro_defs(items: list[dict]) -> dict[str, dict]:
    defs = {}
    for sim_id, meta in SIMULACROS.items():
        ids = [it["id"] for area in AREA_ORDER for it in items
               if it["pool"] == "simulacro" and it.get("sim", "general-1") == sim_id and it["area"] == area]
        defs[sim_id] = {"title": meta["title"], "order": meta["order"], "minutes": max(20, MINUTES_PER_QUESTION * len(ids)), "itemIds": ids}
    return defs


def load_seed() -> dict:
    items = seed_items()
    existing = {s.id: s.to_dict() for s in db().collection("items").stream()}
    writes, written, skipped = [], 0, 0
    for it in items:
        if existing.get(it["id"], {}).get("reviewedBy"):
            skipped += 1  # no pisar lo que un docente ya revisó
            continue
        data = {k: v for k, v in it.items() if k != "id"}
        data["updatedAt"] = now()
        writes.append((db().collection("items").document(it["id"]), data))
        written += 1
    defs = simulacro_defs(items)
    for sim_id, d in defs.items():
        writes.append((db().collection("simulacros").document(sim_id), {**d, "status": "publicado", "updatedAt": now()}))
    for start in range(0, len(writes), 400):  # Firestore admite hasta 500 escrituras por lote
        batch = db().batch()
        for ref, data in writes[start:start + 400]:
            batch.set(ref, data)
        batch.commit()
    bank.invalidate()
    return {"written": written, "skipped": skipped, "simulacroItems": sum(len(d["itemIds"]) for d in defs.values()),
            "simulacros": {k: len(d["itemIds"]) for k, d in defs.items()}}
