"""Bayesian Knowledge Tracing: dominio estimado por competencia."""
from __future__ import annotations

import math

SLIP = 0.10
GUESS = 0.25
TRANSIT = 0.12
GUESS_HINTED = 0.50  # un acierto con pista es evidencia más débil de dominio


def _clip(p: float) -> float:
    return max(0.02, min(0.98, p))


def update(p: float, correct: bool, hinted: bool = False) -> float:
    guess = GUESS_HINTED if hinted else GUESS
    if correct:
        num = p * (1 - SLIP)
        den = num + (1 - p) * guess
    else:
        num = p * SLIP
        den = num + (1 - p) * (1 - guess)
    posterior = num / den if den else p
    return _clip(posterior + (1 - posterior) * TRANSIT)


def init_from_diagnostic(theta: float, correct: int, total: int) -> float:
    """Dominio inicial: mezcla la habilidad del área con el desempeño observado en la competencia."""
    area = 1.0 / (1.0 + math.exp(-1.2 * theta))
    observed = (correct + 0.5) / (total + 1.0)
    w = 0.6 if total == 0 else max(0.3, 0.6 - 0.1 * total)
    return _clip(w * area + (1 - w) * observed)
