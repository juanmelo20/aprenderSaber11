"""Teoría de Respuesta al Ítem (modelo 3PL) y prueba adaptativa (CAT).

Python puro, sin numpy, para que quepa holgado en una instancia gratuita de 512 MB.
"""
from __future__ import annotations

import math
import random

GRID = [-4.0 + 0.1 * i for i in range(81)]
D = 1.0  # métrica logística


def p3pl(theta: float, a: float, b: float, c: float = 0.25) -> float:
    return c + (1.0 - c) / (1.0 + math.exp(-D * a * (theta - b)))


def information(theta: float, a: float, b: float, c: float = 0.25) -> float:
    p = p3pl(theta, a, b, c)
    q = 1.0 - p
    if p <= 0 or c >= 1:
        return 0.0
    return (D * a) ** 2 * (q / p) * ((p - c) / (1.0 - c)) ** 2


def eap(responses: list[tuple[float, float, float, bool]], prior_mean: float = 0.0, prior_sd: float = 1.0) -> tuple[float, float]:
    """Estimación EAP de la habilidad. responses: (a, b, c, acierto). Devuelve (theta, error estándar)."""
    weights = []
    for t in GRID:
        log_w = -0.5 * ((t - prior_mean) / prior_sd) ** 2
        for a, b, c, u in responses:
            p = p3pl(t, a, b, c)
            log_w += math.log(p if u else (1.0 - p))
        weights.append(log_w)
    m = max(weights)
    weights = [math.exp(w - m) for w in weights]
    total = sum(weights)
    theta = sum(t * w for t, w in zip(GRID, weights)) / total
    var = sum((t - theta) ** 2 * w for t, w in zip(GRID, weights)) / total
    return theta, math.sqrt(var)


def score_from_theta(theta: float) -> int:
    """Puntaje estimado en la escala 0-100 (media 50, desviación 10)."""
    return int(round(max(0.0, min(100.0, 50.0 + 10.0 * theta))))


def select_next(
    theta: float,
    candidates: list[dict],
    administered: list[dict],
    weights: dict[str, float],
    rng: random.Random | None = None,
    top_k: int = 3,
) -> dict | None:
    """Elige el siguiente ítem: balancea competencias según su peso en la prueba y, dentro
    de la competencia más atrasada, toma uno de los top_k más informativos (control de exposición)."""
    if not candidates:
        return None
    rng = rng or random.Random()
    n = len(administered) + 1
    counts: dict[str, int] = {}
    for it in administered:
        counts[it["competencia"]] = counts.get(it["competencia"], 0) + 1
    available = {it["competencia"] for it in candidates}
    # déficit = cuota esperada - administrados
    deficits = {c: weights.get(c, 0.0) * n - counts.get(c, 0) for c in available}
    target = max(deficits, key=lambda c: (deficits[c], weights.get(c, 0.0)))
    pool = [it for it in candidates if it["competencia"] == target] or candidates
    pool = sorted(pool, key=lambda it: information(theta, it.get("a", 1.0), it.get("b", 0.0), it.get("c", 0.25)), reverse=True)
    return rng.choice(pool[: max(1, top_k)])


def should_stop(n: int, se: float, remaining: int, min_items: int, max_items: int, se_target: float) -> bool:
    if remaining <= 0 or n >= max_items:
        return True
    return n >= min_items and se <= se_target
