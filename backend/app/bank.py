"""Banco de ítems: lectura con caché en memoria para gastar pocas lecturas de Firestore."""
from __future__ import annotations

import time

from .config import settings
from .db import db

_cache: dict = {"at": 0.0, "items": []}
TTL = 300


def all_items(force: bool = False) -> list[dict]:
    if force or time.time() - _cache["at"] > TTL or not _cache["items"]:
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
    return [it for it in all_items() if it.get("status") in ok]


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
