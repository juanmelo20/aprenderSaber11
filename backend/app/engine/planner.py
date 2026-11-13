"""Generación del plan semanal a partir del dominio por competencia.

Diseño instruccional: práctica de recuperación (cuestionarios cortos), práctica distribuida
(repaso de lo ya trabajado) y cuestionario de salida sin ayudas para volver a medir.
"""
from __future__ import annotations

import random

from ..catalog import AREAS, comp_label

MAX_FOCUS = 3
MAX_FOCUS_PER_AREA = 2


def pick_focus(mastery: dict[str, float], diagnosed_areas: list[str], repeat_focus: list[str] | None = None) -> list[str]:
    if repeat_focus:
        return repeat_focus[:MAX_FOCUS]
    ranked = sorted((k for k in mastery if k.split(".")[0] in diagnosed_areas), key=lambda k: mastery[k])
    focus: list[str] = []
    per_area: dict[str, int] = {}
    for key in ranked:
        area = key.split(".")[0]
        if per_area.get(area, 0) >= MAX_FOCUS_PER_AREA:
            continue
        focus.append(key)
        per_area[area] = per_area.get(area, 0) + 1
        if len(focus) == MAX_FOCUS:
            break
    return focus


def _client_item(item: dict) -> dict:
    return {
        "id": item["id"],
        "area": item["area"],
        "competencia": item["competencia"],
        "context": item.get("context"),
        "stem": item["stem"],
        "options": item["options"],
        "correct": item["correct"],
        "explanation": item.get("explanation", ""),
        "hints": item.get("hints", []),
    }


def _choose(items: list[dict], key: str, n: int, theta: float, seen: set[str], used: set[str], pools: tuple[str, ...], rng: random.Random) -> list[dict]:
    area, comp = key.split(".", 1)
    cands = [it for it in items if it["area"] == area and it["competencia"] == comp and it["pool"] in pools and it["id"] not in used]

    def rank(it: dict) -> tuple:
        return (it["id"] in seen, pools.index(it["pool"]), abs(it.get("b", 0.0) - theta) + rng.random() * 0.3)

    chosen = sorted(cands, key=rank)[:n]
    used.update(it["id"] for it in chosen)
    return chosen


def build_plan(
    week: int,
    mastery: dict[str, float],
    thetas: dict[str, float],
    items: list[dict],
    seen: set[str],
    previous_focus: list[str],
    practice_n: int,
    exit_n: int,
    repeat_focus: list[str] | None = None,
    rng: random.Random | None = None,
) -> dict | None:
    rng = rng or random.Random()
    diagnosed = list(thetas.keys())
    focus = pick_focus(mastery, diagnosed, repeat_focus)
    if not focus:
        return None
    used: set[str] = set()
    sessions: list[dict] = []

    # Primero se apartan las preguntas del cuestionario de salida: sin ellas no se puede volver a medir.
    # Con un banco pequeño, la práctica se queda con lo que sobra (no al revés).
    exit_items: list[dict] = []
    for key in focus:
        area, comp = key.split(".", 1)
        available = sum(1 for it in items if it["area"] == area and it["competencia"] == comp and it["pool"] in ("practica", "diagnostico"))
        reserve = min(exit_n, max(1, available // 3)) if available >= 2 else 0
        exit_items += _choose(items, key, reserve, thetas.get(area, 0.0), seen, used, ("diagnostico", "practica"), rng)

    for i, key in enumerate(focus, start=1):
        area = key.split(".")[0]
        chosen = _choose(items, key, practice_n, thetas.get(area, 0.0), seen, used, ("practica", "diagnostico"), rng)
        if not chosen:
            continue
        sessions.append({
            "id": f"p{i}",
            "type": "practica",
            "area": area,
            "competencia": key,
            "title": f"Práctica: {comp_label(key)}",
            "tutor": True,
            "status": "pendiente",
            "items": [_client_item(it) for it in chosen],
        })

    # Repaso espaciado: competencias trabajadas en semanas anteriores que no son foco hoy.
    review_keys = [k for k in previous_focus if k not in focus][:2]
    review_items: list[dict] = []
    for key in review_keys:
        area = key.split(".")[0]
        review_items += _choose(items, key, 2, thetas.get(area, 0.0), seen, used, ("practica", "diagnostico"), rng)
    if review_items:
        rng.shuffle(review_items)  # intercalado
        sessions.append({
            "id": "r1",
            "type": "repaso",
            "area": "MIX",
            "competencia": None,
            "title": "Repaso espaciado de semanas anteriores",
            "tutor": True,
            "status": "pendiente",
            "items": [_client_item(it) for it in review_items],
        })

    if exit_items:
        rng.shuffle(exit_items)
        sessions.append({
            "id": "s1",
            "type": "salida",
            "area": "MIX",
            "competencia": None,
            "title": "Cuestionario de salida (sin ayudas)",
            "tutor": False,
            "status": "bloqueada",
            "items": [_client_item(it) for it in exit_items],
        })

    if not sessions:
        return None
    return {
        "week": week,
        "status": "activo",
        "refuerzo": bool(repeat_focus),
        "focus": focus,
        "focusLabels": [f"{AREAS[k.split('.')[0]]['name']}: {comp_label(k)}" for k in focus],
        "sessions": sessions,
        "exitPassed": None,
    }
