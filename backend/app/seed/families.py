"""Familias de preguntas: plantillas que producen variantes nuevas cada vez.

Sirven para que la práctica no se repita: cuando un estudiante necesita preguntas de una competencia,
el servidor genera variantes que ese estudiante no ha visto. Cada variante lleva en su identificador una
firma de su contenido, de modo que dos variantes con el mismo texto cuentan como la misma pregunta.

Identificador de una variante generada:  G.<familia>.<semilla>.<firma>
Las plantillas guardadas en el banco (para revisión docente) usan:  <ÁREA>-F-<familia>-<n>
"""
from __future__ import annotations

import random
import zlib

from . import families_ing, families_mat, families_nat, math_families

REGISTRY: dict[str, tuple[str, object]] = {}
for _area, _module in (("MAT", math_families), ("MAT", families_mat), ("NAT", families_nat), ("ING", families_ing)):
    for _fn in _module.FAMILIES:
        assert _fn.__name__ not in REGISTRY, _fn.__name__
        REGISTRY[_fn.__name__] = (_area, _fn)


def _b36(n: int) -> str:
    digits, out = "0123456789abcdefghijklmnopqrstuvwxyz", ""
    while n:
        n, r = divmod(n, 36)
        out = digits[r] + out
    return out or "0"


def signature(item: dict) -> str:
    """Firma del contenido (no depende del orden de las opciones)."""
    text = "|".join([str(item.get("context") or ""), item["stem"], *sorted(item["options"].values())])
    return _b36(zlib.crc32(text.encode("utf-8")))


def _build(name: str, rng: random.Random) -> dict | None:
    area, fn = REGISTRY[name]
    for _ in range(12):  # algunas combinaciones de números se descartan
        spec = fn(rng)
        if spec:
            break
    else:
        return None
    options, correct = spec.pop("packed")
    return {"area": area, "pool": "practica", "a": 1.0, "c": 0.25, "context": spec.get("context"), "options": options, "correct": correct,
            "origin": f"familia:{name}", **spec}


def make(name: str, seed: int) -> dict | None:
    """Variante reproducible: misma familia y semilla, misma pregunta."""
    item = _build(name, random.Random(f"{name}:{seed}"))
    if not item:
        return None
    item.update(id=f"G.{name}.{seed}.{signature(item)}", status="generado")
    return item


def is_generated(item_id: str) -> bool:
    return item_id.startswith("G.")


def family_of(item_id: str) -> str:
    return item_id.split(".")[1]


def templates(per_family: int = 2, seed: int = 2026) -> list[dict]:
    """Ejemplos de cada familia que se guardan en el banco para que un docente los revise.
    Aprobar un ejemplo aprueba la familia completa."""
    out = []
    for name, (area, _) in REGISTRY.items():
        rng, seen, made, tries = random.Random(f"{name}:{seed}"), set(), 0, 0
        while made < per_family and tries < 40:
            tries += 1
            item = _build(name, rng)
            if not item or signature(item) in seen:
                continue
            seen.add(signature(item))
            made += 1
            item.update(id=f"{area}-F-{name}-{made}", status="borrador", pool="plantilla")
            out.append(item)
    return out


def fresh(names, seen_ids, per_family: int, rng: random.Random) -> list[dict]:
    """Variantes nuevas de las familias dadas, distintas de todo lo que el estudiante ya vio."""
    used = {i.rsplit(".", 1)[1] for i in seen_ids if is_generated(i)}
    out = []
    for name in names:
        if name not in REGISTRY:
            continue
        made = 0
        for _ in range(per_family * 10):
            if made >= per_family:
                break
            item = make(name, rng.randrange(10 ** 9))
            if not item:
                continue
            sig = item["id"].rsplit(".", 1)[1]
            if sig in used:
                continue
            used.add(sig)
            out.append(item)
            made += 1
    return out


def capacity(name: str, samples: int = 400) -> int:
    """Cuántas variantes distintas se obtienen en 'samples' intentos (cota inferior del tamaño de la familia)."""
    rng = random.Random(f"cap:{name}")
    return len({signature(it) for it in (_build(name, rng) for _ in range(samples)) if it})
