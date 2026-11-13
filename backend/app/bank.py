"""Banco de ítems: lectura con caché en memoria para gastar pocas lecturas de Firestore."""
from __future__ import annotations

import random
import time
import zlib

from .config import settings
from .db import db
from .seed import families

_cache: dict = {"at": 0.0, "items": []}


def all_items(force: bool = False) -> list[dict]:
    if force or time.time() - _cache["at"] > settings.bank_ttl or not _cache["items"]:
        items = []
        for snap in db().collection("items").stream():
            data = snap.to_dict()
            data["id"] = snap.id
            items.append(data)
        _cache.update(at=time.time(), items=items)
    return _cache["items"]


def invalidate() -> None:
    _cache["at"] = 0.0


def usable_items() -> list[dict]:
    """Ítems que se pueden mostrar a estudiantes: publicados (revisados por docente) y,
    solo si ALLOW_UNREVIEWED_ITEMS está activo, también el banco semilla en borrador."""
    ok = {"publicado"} | ({"borrador", "revisado"} if settings.allow_unreviewed else set())
    return [it for it in all_items() if it.get("pool") != "plantilla"
            and (it.get("status") == "publicado" or (it.get("status") in ok and it.get("origin") != "ia"))]


def approved_families() -> list[str]:
    """Familias cuyas variantes se pueden generar para estudiantes: las que tienen al menos una plantilla
    aprobada por un docente (o todas, si se permite el banco sin revisar)."""
    if settings.allow_unreviewed:
        return list(families.REGISTRY)
    names = {str(it.get("origin", "")).split(":", 1)[1] for it in all_items()
             if it.get("pool") == "plantilla" and it.get("status") == "publicado" and str(it.get("origin", "")).startswith("familia:")}
    return [n for n in families.REGISTRY if n in names]


def fresh_variants(uid: str, week: int, seen: set[str], per_family: int = 3) -> list[dict]:
    """Preguntas nuevas para este estudiante, generadas a partir de las familias aprobadas."""
    rng = random.Random(zlib.crc32(f"{uid}:{week}".encode()))
    return families.fresh(approved_families(), seen, per_family, rng)


def by_id() -> dict[str, dict]:
    return {it["id"]: it for it in all_items()}


def public_item(item: dict) -> dict:
    """Versión sin clave ni explicación (diagnóstico y simulacro)."""
    return {
        "id": item["id"],
        "area": item["area"],
        "competencia": item["competencia"],
        "context": item.get("context"),
        "stem": item["stem"],
        "options": item["options"],
    }
