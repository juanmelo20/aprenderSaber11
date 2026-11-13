"""Carga el banco semilla y el simulacro general en Firestore."""
from __future__ import annotations

from .. import bank
from ..catalog import AREA_ORDER
from ..db import db, now
from . import bank_lec, bank_nat_ing, bank_seed, bank_soc, families  # noqa: F401  (los bank_* agregan sus preguntas al importarse)


def seed_items() -> list[dict]:
    return list(bank_seed.ITEMS) + families.templates()


def load_seed() -> dict:
    items = seed_items()
    existing = {s.id: s.to_dict() for s in db().collection("items").stream()}
    batch, written, skipped = db().batch(), 0, 0
    for it in items:
        if existing.get(it["id"], {}).get("reviewedBy"):
            skipped += 1  # no pisar lo que un docente ya revisó
            continue
        data = {k: v for k, v in it.items() if k != "id"}
        data["updatedAt"] = now()
        batch.set(db().collection("items").document(it["id"]), data)
        written += 1
    sim_ids = [it["id"] for area in AREA_ORDER for it in items if it["pool"] == "simulacro" and it["area"] == area]
    batch.set(db().collection("simulacros").document("general-1"), {
        "title": "Simulacro general 1", "minutes": max(20, 2 * len(sim_ids)), "itemIds": sim_ids,
        "status": "publicado", "updatedAt": now(),
    })
    batch.commit()
    bank.invalidate()
    return {"written": written, "skipped": skipped, "simulacroItems": len(sim_ids)}
