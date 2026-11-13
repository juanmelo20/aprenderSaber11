"""Familias de ítems de Matemáticas (generación automática por plantilla).

Cada familia produce variantes con números distintos, clave calculada y distractores que
corresponden a errores frecuentes. Así el banco de práctica de esta área no se agota.
"""
from __future__ import annotations

import random


def _money(n: float) -> str:
    return "$" + f"{int(round(n)):,}".replace(",", ".")


def _th(n: int) -> str:
    return f"{int(n):,}".replace(",", ".")


def _num(x: float) -> str:
    s = f"{x:.2f}".rstrip("0").rstrip(".") if isinstance(x, float) and not float(x).is_integer() else str(int(x))
    return s.replace(".", ",")


def _pack(rng: random.Random, correct: str, distractors: list[str]) -> tuple[dict, str] | None:
    opts = []
    for d in distractors:
        if d != correct and d not in opts:
            opts.append(d)
    if len(opts) < 3:
        return None
    options = [correct] + opts[:3]
    rng.shuffle(options)
    letters = dict(zip("ABCD", options))
    return letters, next(k for k, v in letters.items() if v == correct)


def descuento(rng):
    price = rng.choice([40, 60, 80, 120, 150, 200]) * 1000
    pct = rng.choice([10, 15, 20, 25, 30])
    off = price * pct / 100
    packed = _pack(rng, _money(price - off), [_money(off), _money(price + off), _money(price - pct * 100), _money(price - off / 2)])
    return packed and {
        "competencia": "formulacion", "b": -0.3, "componente": "Álgebra y cálculo",
        "stem": f"Un artículo cuesta {_money(price)} y tiene un descuento del {pct} %. ¿Cuánto se paga por él?",
        "explanation": f"El {pct} % de {_money(price)} es {_money(off)}. Se paga {_money(price)} − {_money(off)} = {_money(price - off)}.",
        "hints": ["Calcula primero el valor del descuento.", "El descuento se resta del precio original."], "packed": packed}


def proporcion(rng):
    base = rng.choice([4, 5, 6, 8])
    grams = rng.choice([200, 300, 400, 600])
    target = rng.choice([x for x in (10, 12, 15, 20) if x % base != 0] or [10])
    if (grams * target) % base or grams % base:
        return None
    ans = grams / base * target
    packed = _pack(rng, f"{_th(ans)} g", [f"{_th(grams * target / 10)} g", f"{_th(grams + (target - base) * 10)} g", f"{_th(grams * 2)} g", f"{_th(ans * 2)} g"])
    return packed and {
        "competencia": "formulacion", "b": -0.6, "componente": "Álgebra y cálculo",
        "stem": f"Una receta para {base} personas lleva {grams} g de harina. Manteniendo la proporción, ¿cuánta harina se necesita para {target} personas?",
        "explanation": f"Por persona: {grams} ÷ {base} = {_num(grams / base)} g. Para {target} personas: {_num(grams / base)} × {target} = {_th(ans)} g.",
        "hints": ["Halla la cantidad para una sola persona.", "Luego multiplica por el número de personas."], "packed": packed}


def promedio_faltante(rng):
    n = 4
    target = rng.choice([35, 38, 40, 42])  # promedio deseado x10
    known = [rng.choice([30, 32, 36, 38, 40, 44]) for _ in range(n - 1)]
    need = target * n - sum(known)
    if not 10 <= need <= 50:
        return None
    f = lambda v: f"{v / 10:.1f}".replace(".", ",")
    packed = _pack(rng, f(need), [f(target), f(round(sum(known) / 3)), f(need - 4), f(need + 4), f(50)])
    return packed and {
        "competencia": "formulacion", "b": 0.5, "componente": "Estadística",
        "stem": f"Un estudiante tiene tres notas: {f(known[0])}; {f(known[1])} y {f(known[2])}. ¿Qué nota necesita en la cuarta evaluación para que su promedio sea exactamente {f(target)}?",
        "explanation": f"Para promediar {f(target)} en 4 notas, la suma debe ser {f(target * n)}. Las tres notas suman {f(sum(known))}; falta {f(need)}.",
        "hints": ["¿Cuánto deben sumar las cuatro notas para ese promedio?", "Resta lo que ya suman las tres notas."], "packed": packed}


def probabilidad(rng):
    red, blue, green = rng.choice([(3, 5, 2), (4, 4, 2), (6, 2, 2), (2, 5, 3), (5, 10, 5)])
    total = red + blue + green
    packed = _pack(rng, f"{red}/{total}", [f"{red}/{blue + green}", f"1/{red}", f"{blue}/{total}", f"1/3"])
    return packed and {
        "competencia": "formulacion", "b": -0.2, "componente": "Estadística",
        "stem": f"En una bolsa hay {red} balotas rojas, {blue} azules y {green} verdes, todas del mismo tamaño. Si se saca una al azar, ¿cuál es la probabilidad de que sea roja?",
        "explanation": f"Probabilidad = casos favorables ÷ casos posibles = {red} ÷ {total} = {red}/{total}.",
        "hints": ["Cuenta cuántas balotas hay en total.", "Los casos favorables son solo las rojas."], "packed": packed}


def lineal(rng):
    fixed = rng.choice([3000, 5000, 8000, 10000])
    rate = rng.choice([1200, 1500, 2000, 2500])
    packed = _pack(rng, "Lo que aumenta el costo por cada kilómetro recorrido.", [
        "El cargo fijo que se cobra en cualquier recorrido.", "El costo total de un recorrido de un kilómetro.",
        "La distancia máxima que cubre el servicio.", "El número de kilómetros recorridos."])
    return packed and {
        "competencia": "interpretacion", "b": 0.2, "componente": "Álgebra y cálculo",
        "stem": f"El costo de un servicio de transporte, en pesos, se calcula con C(x) = {_th(rate)}x + {_th(fixed)}, donde x es la distancia en kilómetros. ¿Qué representa el número {_th(rate)} en esta expresión?",
        "explanation": f"{_th(rate)} multiplica a x: por cada kilómetro adicional el costo sube {_money(rate)}. El {_th(fixed)} es el cargo fijo.",
        "hints": ["Compara el costo de 1 km con el de 2 km.", "¿Qué número cambia cuando cambia x?"], "packed": packed}


def tabla_variacion(rng):
    days = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    for _ in range(20):
        vals = [rng.randint(8, 30) for _ in days]
        diffs = [vals[i + 1] - vals[i] for i in range(4)]
        if sorted(diffs)[0] < sorted(diffs)[1] and min(diffs) < 0:
            break
    else:
        return None
    i = diffs.index(min(diffs))
    names = [f"De {days[k]} a {days[k + 1]}." for k in range(4)]
    letters = dict(zip("ABCD", names))
    listing = ", ".join(f"{d} {v}" for d, v in zip(days, vals))
    return {
        "competencia": "interpretacion", "b": -0.7, "componente": "Estadística",
        "context": f"Litros de leche recogidos en una finca: {listing}.",
        "stem": "¿Entre qué días consecutivos se presentó la mayor disminución?",
        "explanation": f"Los cambios día a día son {', '.join(('+' if d > 0 else '') + str(d) for d in diffs)}. La mayor disminución ({abs(min(diffs))} litros) ocurre {names[i].lower().rstrip('.')}.",
        "hints": ["Resta cada día del siguiente.", "Busca el cambio negativo más grande."], "packed": (letters, "ABCD"[i])}


def escala_area(rng):
    k = rng.choice([2, 3])
    word = {2: "duplican", 3: "triplican"}[k]
    packed = _pack(rng, f"Se multiplica por {k * k}.", [f"Se multiplica por {k}.", f"Se multiplica por {k * 2 if k == 3 else 8}.", "No cambia.", f"Aumenta en {k} unidades."])
    return packed and {
        "competencia": "argumentacion", "b": 0.6, "componente": "Geometría",
        "stem": f"Si se {word} el largo y el ancho de un rectángulo, ¿qué ocurre con su área?",
        "explanation": f"El área es largo × ancho. Si ambos se multiplican por {k}, el área se multiplica por {k} × {k} = {k * k}.",
        "hints": ["Prueba con un rectángulo de 2 por 3.", "Cada dimensión aporta su propio factor."], "packed": packed}


def media_atipico(rng):
    base = sorted(rng.sample(range(900, 1500, 50), 4))
    out = rng.choice([6000, 8000, 9000])
    vals = base + [out]
    mean = sum(vals) / 5
    above = sum(v > mean for v in vals)
    if above != 1:
        return None
    packed = _pack(rng, "No, porque el ingreso más alto eleva el promedio por encima de lo que ganan casi todos.", [
        "Sí, porque el promedio siempre describe a la mayoría.", "Sí, porque todos los ingresos son parecidos.",
        "No, porque el promedio solo sirve para números pequeños.", "Sí, porque el promedio es el valor que más se repite."])
    listing = "; ".join(_money(v * 1000) for v in vals)
    return packed and {
        "competencia": "argumentacion", "b": 1.0, "componente": "Estadística",
        "context": f"Ingresos mensuales de cinco familias de una vereda: {listing}.",
        "stem": f"Alguien afirma: 'En promedio ganan {_money(mean * 1000)}, así que la mayoría de las familias gana cerca de esa cifra'. ¿Es válida la conclusión?",
        "explanation": f"El promedio es {_money(mean * 1000)}, pero cuatro de las cinco familias ganan mucho menos: un dato atípico arrastra el promedio. La mediana describe mejor al grupo.",
        "hints": ["Compara cada ingreso con el promedio.", "¿Cuántas familias están por encima del promedio?"], "packed": packed}


FAMILIES = [descuento, proporcion, promedio_faltante, probabilidad, lineal, tabla_variacion, escala_area, media_atipico]


def generate(variants: int = 3, seed: int = 2026) -> list[dict]:
    """Variantes reproducibles (misma semilla, mismos ítems e identificadores)."""
    items = []
    for f_idx, family in enumerate(FAMILIES, start=1):
        rng = random.Random(seed * 100 + f_idx)
        made, tries, stems = 0, 0, set()
        while made < variants and tries < 60:
            tries += 1
            spec = family(rng)
            if not spec or spec["stem"] + str(spec.get("context")) in stems:
                continue
            stems.add(spec["stem"] + str(spec.get("context")))
            made += 1
            options, correct = spec.pop("packed")
            items.append({
                "id": f"MAT-F{f_idx}-{made}", "area": "MAT", "pool": "practica", "a": 1.0, "c": 0.25, "context": spec.get("context"),
                "options": options, "correct": correct, "status": "borrador", "origin": f"familia:{family.__name__}", **spec,
            })
    return items
