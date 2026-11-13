"""Más familias de Matemáticas. Cada función recibe un generador aleatorio y devuelve una variante
(o None si los números elegidos no sirven). La clave siempre se calcula, nunca se escribe a mano."""
from __future__ import annotations

from .math_families import _money, _num, _pack, _th


# ----------------------------- Formulación y ejecución -----------------------------

def regla_tres_inversa(rng):
    w1, d1 = rng.choice([4, 6, 8, 10, 12]), rng.choice([6, 9, 12, 15, 18])
    cands = [x for x in (2, 3, 4, 5, 6, 8, 9, 12, 15, 18) if x != w1 and (w1 * d1) % x == 0]
    if not cands:
        return None
    w2 = rng.choice(cands)
    ans = w1 * d1 // w2
    job = rng.choice(["levantar una cerca", "recoger una cosecha de café", "pintar un salón comunal", "limpiar un potrero"])
    packed = _pack(rng, f"{ans} días", [f"{_num(d1 * w2 / w1)} días", f"{d1 + abs(w1 - w2)} días", f"{ans * 2} días", f"{ans + w2} días", f"{d1} días"])
    return packed and {
        "competencia": "formulacion", "b": 0.3, "componente": "Álgebra y cálculo",
        "stem": f"{w1} trabajadores tardan {d1} días en {job}. Si todos trabajan al mismo ritmo, ¿cuánto tardarían {w2} trabajadores en hacer el mismo trabajo?",
        "explanation": f"El trabajo total es {w1} × {d1} = {w1 * d1} jornadas. Repartido entre {w2} trabajadores: {w1 * d1} ÷ {w2} = {ans} días. Es proporción inversa: con {'más' if w2 > w1 else 'menos'} personas se tarda {'menos' if w2 > w1 else 'más'}.",
        "hints": ["¿Con más trabajadores se tarda más o menos?", "Calcula cuántas jornadas de una persona tiene el trabajo completo."], "packed": packed}


def interes_simple(rng):
    cap = rng.choice([500, 800, 1000, 1200, 1500, 2000]) * 1000
    rate = rng.choice([1, 2, 3, 4])
    months = rng.choice([3, 4, 5, 6, 10, 12])
    interest = cap * rate * months // 100
    packed = _pack(rng, _money(cap + interest), [_money(interest), _money(cap + cap * rate // 100), _money(cap + 2 * interest), _money(cap + interest // 2)])
    return packed and {
        "competencia": "formulacion", "b": 0.2, "componente": "Álgebra y cálculo",
        "stem": f"Una cooperativa presta {_money(cap)} con un interés simple del {rate} % mensual. ¿Cuánto se debe devolver en total al cabo de {months} meses?",
        "explanation": f"Interés de un mes: {_money(cap * rate // 100)}. En {months} meses: {_money(interest)}. Total: {_money(cap)} + {_money(interest)} = {_money(cap + interest)}.",
        "hints": ["Calcula primero el interés de un solo mes.", "La pregunta pide el total: capital más intereses."], "packed": packed}


def cerca_rectangulo(rng):
    length, width = rng.choice([12, 15, 20, 25, 30, 40]), rng.choice([6, 8, 10, 12, 14])
    price = rng.choice([4, 5, 6, 8]) * 1000
    perim = 2 * (length + width)
    packed = _pack(rng, _money(perim * price), [_money(length * width * price), _money((length + width) * price), _money(4 * length * price), _money(perim * price // 2 + price)])
    return packed and {
        "competencia": "formulacion", "b": -0.1, "componente": "Geometría",
        "stem": f"Un lote rectangular mide {length} m de largo y {width} m de ancho. Se va a cercar todo su borde con alambre que cuesta {_money(price)} por metro. ¿Cuánto cuesta el alambre?",
        "explanation": f"El borde es el perímetro: 2 × ({length} + {width}) = {perim} m. Costo: {perim} × {_money(price)} = {_money(perim * price)}.",
        "hints": ["Cercar el borde es recorrer el perímetro, no cubrir el área.", "Un rectángulo tiene dos largos y dos anchos."], "packed": packed}


def tiempo_recorrido(rng):
    v, t1 = rng.choice([30, 40, 50, 60]), rng.choice([2, 3, 4])
    t2 = rng.choice([x for x in (1.5, 2.5, 3.5, 5, 6) if x != t1])
    d1, d2 = v * t1, int(v * t2)
    packed = _pack(rng, f"{_num(t2)} horas", [f"{_num(t2 + 0.5)} horas", f"{_num(t2 * 2)} horas", f"{_num(max(0.5, t2 - 1))} horas", f"{_num(d2 / d1)} horas"])
    return packed and {
        "competencia": "formulacion", "b": 0.0, "componente": "Álgebra y cálculo",
        "stem": f"Una moto recorre {d1} km en {t1} horas a velocidad constante. A esa misma velocidad, ¿cuánto tarda en recorrer {d2} km?",
        "explanation": f"Velocidad: {d1} ÷ {t1} = {v} km/h. Tiempo: {d2} ÷ {v} = {_num(t2)} horas.",
        "hints": ["Halla primero cuántos kilómetros recorre en una hora.", "Tiempo = distancia ÷ velocidad."], "packed": packed}


def pitagoras(rng):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (7, 24, 25), (10, 24, 26), (15, 20, 25)])
    if rng.random() < 0.5:
        scene = rng.choice([
            f"Un poste de {b} m de alto se sostiene con un cable tensado desde su punta hasta un punto del suelo a {a} m de su base. ¿Cuánto mide el cable?",
            f"Una rampa avanza {b} m en horizontal y sube {a} m. ¿Cuánto mide la superficie inclinada de la rampa?",
            f"Un terreno rectangular mide {a} m por {b} m. ¿Cuánto mide el camino recto que lo cruza de una esquina a la opuesta?"])
        packed = _pack(rng, f"{c} m", [f"{a + b} m", f"{b + 1} m", f"{c + 2} m", f"{b - a} m", f"{a * b} m"])
        expl = f"Es la hipotenusa de un triángulo rectángulo: √({a}² + {b}²) = √{a * a + b * b} = {c} m."
    else:
        scene = f"Una escalera de {c} m se apoya en una pared. Su base queda a {a} m de la pared. ¿A qué altura toca la escalera la pared?"
        packed = _pack(rng, f"{b} m", [f"{c - a} m", f"{c + a} m", f"{b + 2} m", f"{c} m", f"{b - 1} m"])
        expl = f"La escalera es la hipotenusa: altura = √({c}² − {a}²) = √{c * c - a * a} = {b} m."
    return packed and {
        "competencia": "formulacion", "b": 0.5, "componente": "Geometría", "stem": scene, "explanation": expl,
        "hints": ["Dibuja la situación: se forma un triángulo rectángulo.", "Identifica cuál lado es la hipotenusa (el que queda frente al ángulo recto)."], "packed": packed}


def volumen_tanque(rng):
    l, w, h = rng.choice([1, 2, 3]), rng.choice([1, 1.5, 2]), rng.choice([0.5, 1, 1.5, 2])
    vol = l * w * h
    liters = int(round(vol * 1000))
    packed = _pack(rng, f"{_th(liters)} litros", [f"{_num(vol)} litros", f"{_th(liters // 10)} litros", f"{_th(int((l + w + h) * 1000))} litros", f"{_th(liters * 2)} litros"])
    return packed and {
        "competencia": "formulacion", "b": 0.4, "componente": "Geometría",
        "stem": f"Un tanque con forma de caja mide {_num(l)} m de largo, {_num(w)} m de ancho y {_num(h)} m de alto. Si 1 m³ equivale a 1.000 litros, ¿cuántos litros de agua le caben?",
        "explanation": f"Volumen: {_num(l)} × {_num(w)} × {_num(h)} = {_num(vol)} m³. En litros: {_num(vol)} × 1.000 = {_th(liters)} litros.",
        "hints": ["El volumen de una caja es largo × ancho × alto.", "No olvides convertir los metros cúbicos a litros."], "packed": packed}


def conteo_combinaciones(rng):
    a, b, c = rng.randint(2, 5), rng.randint(2, 5), rng.randint(2, 4)
    scene = rng.choice([
        (f"Un restaurante ofrece {a} sopas, {b} platos fuertes y {c} jugos. ¿Cuántos almuerzos distintos de una sopa, un plato fuerte y un jugo se pueden armar?", "almuerzos"),
        (f"Para el uniforme de un equipo hay {a} colores de camiseta, {b} de pantaloneta y {c} de medias. ¿Cuántos uniformes distintos se pueden formar?", "uniformes"),
        (f"Para ir de la vereda al colegio hay {a} caminos hasta el río, {b} puentes para cruzarlo y {c} calles desde el río hasta el colegio. ¿Cuántas rutas distintas hay?", "rutas")])
    packed = _pack(rng, str(a * b * c), [str(a + b + c), str(a * b + c), str(a * b), str((a + b) * c), str(a * b * c + a)])
    return packed and {
        "competencia": "formulacion", "b": 0.1, "componente": "Estadística", "stem": scene[0],
        "explanation": f"Cada elección se combina con todas las demás: {a} × {b} × {c} = {a * b * c} {scene[1]}.",
        "hints": ["Por cada opción de la primera elección, ¿cuántas hay de la segunda?", "Las elecciones independientes se multiplican, no se suman."], "packed": packed}


def ecuacion_plan(rng):
    fixed = rng.choice([10, 12, 15, 20]) * 1000
    per = rng.choice([50, 80, 100, 120])
    minutes = rng.choice(range(50, 310, 10))
    total = fixed + per * minutes
    packed = _pack(rng, f"{minutes} minutos", [f"{_num(total / per)} minutos", f"{_num((total + fixed) / per)} minutos", f"{minutes // 2} minutos", f"{minutes + fixed // 1000} minutos"])
    return packed and {
        "competencia": "formulacion", "b": 0.3, "componente": "Álgebra y cálculo",
        "stem": f"Un plan de celular cobra un cargo fijo de {_money(fixed)} al mes más {_money(per)} por cada minuto de llamada. Si la factura del mes fue de {_money(total)}, ¿cuántos minutos se usaron?",
        "explanation": f"Se resta el cargo fijo: {_money(total)} − {_money(fixed)} = {_money(total - fixed)}. Luego se divide entre el valor del minuto: {_th(total - fixed)} ÷ {per} = {minutes} minutos.",
        "hints": ["Parte de la factura no depende de los minutos.", "Plantea: cargo fijo + valor por minuto × minutos = factura."], "packed": packed}


# ----------------------------- Interpretación y representación -----------------------------

def mediana(rng):
    n = rng.choice([5, 7])
    vals = [rng.randint(12, 40) for _ in range(n)]
    med = sorted(vals)[n // 2]
    if vals[n // 2] == med or len(set(vals)) < n:
        return None
    what = rng.choice(["Edades de los integrantes de un grupo de danzas", "Puntos anotados por un equipo de baloncesto en sus últimos partidos",
                       "Kilos de mora recogidos cada día por una familia", "Minutos que tardaron varios estudiantes en llegar al colegio"])
    mean = sum(vals) / n
    packed = _pack(rng, str(med), [str(vals[n // 2]), _num(round(mean, 1)), str(max(vals)), str(min(vals)), str(med + 1)])
    return packed and {
        "competencia": "interpretacion", "b": -0.2, "componente": "Estadística",
        "context": f"{what}: {', '.join(map(str, vals))}.", "stem": "¿Cuál es la mediana de estos datos?",
        "explanation": f"Ordenados: {', '.join(map(str, sorted(vals)))}. El dato del centro es {med}.",
        "hints": ["Antes de buscar el centro hay que ordenar los datos.", "Con una cantidad impar de datos, la mediana es el que queda justo en la mitad."], "packed": packed}


def participacion_porcentual(rng):
    total = rng.choice([50, 100, 200, 400])
    theme, cats = rng.choice([
        ("deporte preferido", ["fútbol", "baloncesto", "voleibol", "atletismo"]),
        ("medio para llegar al colegio", ["a pie", "moto", "bus", "bicicleta"]),
        ("fruta preferida", ["mango", "guayaba", "naranja", "piña"])])
    for _ in range(30):
        pcts = [rng.choice(range(10, 55, 5)) for _ in range(3)]
        last = 100 - sum(pcts)
        if 5 <= last <= 50 and len(set(pcts + [last])) == 4:
            pcts.append(last)
            break
    else:
        return None
    counts = [p * total // 100 for p in pcts]
    i = rng.randrange(4)
    packed = _pack(rng, f"{pcts[i]} %", [f"{counts[i]} %", f"{100 - pcts[i]} %", f"{pcts[(i + 1) % 4]} %", f"{_num(round(total / counts[i], 1))} %"])
    return packed and {
        "competencia": "interpretacion", "b": -0.4, "componente": "Estadística",
        "context": f"En una encuesta a {total} estudiantes sobre su {theme}, las respuestas fueron: " + ", ".join(f"{c} {n}" for c, n in zip(cats, counts)) + ".",
        "stem": f"¿Qué porcentaje de los encuestados eligió {cats[i]}?",
        "explanation": f"{counts[i]} de {total} es {counts[i]} ÷ {total} = {pcts[i] / 100:.2f}".replace(".", ",") + f", es decir, {pcts[i]} %.",
        "hints": ["Un porcentaje compara una parte con el total.", "Divide la cantidad de esa respuesta entre el total de encuestados."], "packed": packed}


def tasa_de_cambio(rng):
    m, b0 = rng.choice([3, 4, 5, 6, 8, 12, 15]), rng.choice([10, 20, 25, 40, 50])
    scene, unit, xname = rng.choice([
        ("Un tanque que ya tenía agua se sigue llenando con una manguera. La tabla muestra los litros que contiene.", "litros", "minuto"),
        ("Laura tenía unos ahorros y cada semana guarda la misma cantidad. La tabla muestra sus ahorros en miles de pesos.", "mil pesos", "semana"),
        ("Una planta se mide cada semana. La tabla muestra su altura en milímetros.", "milímetros", "semana")])
    xs = [1, 2, 3, 4]
    rows = "; ".join(f"{xname} {x}: {b0 + m * x}" for x in xs)
    packed = _pack(rng, f"{m} {unit}", [f"{b0} {unit}", f"{b0 + m} {unit}", f"{_num(round((b0 + 4 * m) / 4, 1))} {unit}", f"{m * 2} {unit}"])
    return packed and {
        "competencia": "interpretacion", "b": 0.1, "componente": "Álgebra y cálculo",
        "context": f"{scene}\n{rows}.", "stem": f"Según la tabla, ¿cuánto aumenta la cantidad por cada {xname} que pasa?",
        "explanation": f"De un registro al siguiente la cantidad sube siempre lo mismo: {b0 + 2 * m} − {b0 + m} = {m} {unit}. El valor inicial ({b0}) no es el aumento.",
        "hints": ["Resta dos registros seguidos.", "No confundas lo que había al comienzo con lo que aumenta cada vez."], "packed": packed}


def rango_de_datos(rng):
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
    vals = rng.sample(range(15, 90), 6)
    hi, lo = max(vals), min(vals)
    product = rng.choice(["arepas vendidas en una tienda", "pasajeros transportados por una chiva", "libros prestados en la biblioteca"])
    packed = _pack(rng, str(hi - lo), [str(hi), str(hi + lo), str(sorted(vals)[-1] - sorted(vals)[-2]), str(lo), str(hi - lo + 10)])
    return packed and {
        "competencia": "interpretacion", "b": -0.6, "componente": "Estadística",
        "context": f"Cantidad de {product} en una semana: " + ", ".join(f"{d} {v}" for d, v in zip(days, vals)) + ".",
        "stem": "¿Cuál es la diferencia entre el día de mayor cantidad y el de menor cantidad?",
        "explanation": f"El mayor valor es {hi} ({days[vals.index(hi)]}) y el menor es {lo} ({days[vals.index(lo)]}). Diferencia: {hi} − {lo} = {hi - lo}.",
        "hints": ["Ubica primero el día con el número más alto y el día con el más bajo.", "Diferencia significa restar."], "packed": packed}


# ----------------------------- Argumentación -----------------------------

def sube_y_baja(rng):
    price = rng.choice([50, 80, 100, 150, 200]) * 1000
    pct = rng.choice([10, 20, 25, 50])
    up = price * (100 + pct) // 100
    final = up * (100 - pct) // 100
    packed = _pack(rng, f"No. Queda en {_money(final)}, porque la rebaja se calcula sobre el precio ya aumentado.", [
        f"Sí. Subir y bajar el mismo porcentaje se cancela y vuelve a {_money(price)}.",
        f"No. Queda en {_money(up)}, porque la rebaja no alcanza a compensar el aumento.",
        f"Sí. El {pct} % siempre representa la misma cantidad de dinero."])
    return packed and {
        "competencia": "argumentacion", "b": 0.8, "componente": "Álgebra y cálculo",
        "stem": f"Un artículo de {_money(price)} sube {pct} % y, un mes después, el nuevo precio baja {pct} %. Un vendedor afirma que el artículo volvió a costar lo mismo que al principio. ¿Tiene razón?",
        "explanation": f"Tras el aumento cuesta {_money(up)}. El {pct} % de {_money(up)} es {_money(up - final)}, más que lo que había subido ({_money(up - price)}). Precio final: {_money(final)}.",
        "hints": [f"Calcula el precio después del aumento.", "¿Sobre cuál precio se calcula la rebaja?"], "packed": packed}


def oferta_comparada(rng):
    unit = rng.choice([6, 9, 12, 15, 20]) * 1000
    pct = rng.choice([20, 25, 30, 40, 50])
    cost_a, cost_b = 2 * unit, 3 * unit * (100 - pct) // 100
    best, other = ("A", "B") if cost_a < cost_b else ("B", "A")
    lo, hi = min(cost_a, cost_b), max(cost_a, cost_b)
    packed = _pack(rng, f"En la tienda {best}: paga {_money(lo)} frente a {_money(hi)} en la {other}.", [
        f"En la tienda {other}: paga {_money(lo)} frente a {_money(hi)} en la {best}.",
        "En cualquiera de las dos: las dos ofertas equivalen al mismo descuento.",
        f"En la tienda {'B' if best == 'A' else 'A'}, porque {'un descuento en porcentaje' if best == 'A' else 'llevar un producto gratis'} siempre es la mejor oferta."])
    return packed and {
        "competencia": "argumentacion", "b": 0.6, "componente": "Álgebra y cálculo",
        "stem": f"Un jabón cuesta {_money(unit)} en dos tiendas. La tienda A ofrece 'lleve 3 y pague 2'. La tienda B ofrece {pct} % de descuento en cada unidad. ¿Dónde sale más barato comprar 3 jabones?",
        "explanation": f"En A se pagan 2 unidades: {_money(cost_a)}. En B, cada una queda en {_money(unit * (100 - pct) // 100)} y las 3 cuestan {_money(cost_b)}. 'Lleve 3 pague 2' equivale a un 33,3 % de descuento.",
        "hints": ["Calcula cuánto se paga en total por 3 unidades en cada tienda.", "¿A qué porcentaje de descuento equivale llevar 3 y pagar 2?"], "packed": packed}


def promedio_con_nuevo_dato(rng):
    n = rng.randint(4, 9)
    mean = rng.choice([3.2, 3.5, 3.6, 3.8, 4.0])
    new = rng.choice([x for x in (2.5, 3.0, 3.4, 3.7, 3.9, 4.2, 4.5, 5.0) if abs(x - mean) > 0.05])
    after = (n * mean + new) / (n + 1)
    rises = new > mean
    f = lambda v: f"{v:.1f}".replace(".", ",")
    packed = _pack(rng, f"{'Sí' if rises else 'No'}, porque la nueva nota ({f(new)}) es {'mayor' if rises else 'menor'} que el promedio que había ({f(mean)}).", [
        f"{'No' if rises else 'Sí'}, porque la nueva nota ({f(new)}) es {'menor' if rises else 'mayor'} que {'5,0' if rises else '3,0'}.",
        "Sí, porque al haber más estudiantes el promedio siempre aumenta.",
        "No se puede saber sin conocer la nota de cada uno de los estudiantes."])
    return packed and {
        "competencia": "argumentacion", "b": 0.5, "componente": "Estadística",
        "stem": f"El promedio de notas de {n} estudiantes es {f(mean)}. Llega un estudiante nuevo con nota {f(new)}. Alguien afirma que el promedio del grupo va a subir. ¿Es correcta la afirmación?",
        "explanation": f"Un dato {'mayor' if rises else 'menor'} que el promedio lo {'sube' if rises else 'baja'}. Nuevo promedio: ({n} × {f(mean)} + {f(new)}) ÷ {n + 1} = {after:.2f}".replace(".", ",") + ".",
        "hints": ["No hace falta conocer cada nota: basta comparar el dato nuevo con el promedio.", "¿Qué le pasa a un promedio cuando entra un dato más alto que él?"], "packed": packed}


def comparar_fracciones(rng):
    a, b = rng.choice([(3, 4), (2, 3), (4, 5), (1, 2), (3, 5)])
    c, d = rng.choice([(5, 8), (7, 12), (5, 9), (7, 10), (9, 16), (11, 20), (7, 8), (11, 12)])
    if a * d == c * b:
        return None
    luis_more = c * b > a * d
    lcm = b * d
    x, y = a * d, c * b
    who = rng.choice([("Ana", "Luis"), ("Marta", "Julián"), ("Sofía", "Andrés")])
    correct = (f"{'Sí recorrió más, aunque su razón no es válida' if luis_more else 'No recorrió más'}: con denominador común, {a}/{b} = {x}/{lcm} y {c}/{d} = {y}/{lcm}.")
    packed = _pack(rng, correct, [
        f"Sí recorrió más, y su razón es válida: una fracción con números más grandes siempre es mayor.",
        "No se puede saber, porque dos fracciones con distinto denominador no se pueden comparar.",
        f"{'No recorrió más' if luis_more else 'Sí recorrió más'}: con denominador común, {a}/{b} = {y}/{lcm} y {c}/{d} = {x}/{lcm}."])
    return packed and {
        "competencia": "argumentacion", "b": 0.7, "componente": "Álgebra y cálculo",
        "stem": f"{who[0]} recorrió {a}/{b} de un camino y {who[1]} recorrió {c}/{d} del mismo camino. {who[1]} dice: 'Yo recorrí más, porque {c} y {d} son números más grandes que {a} y {b}'. ¿Qué se puede afirmar?",
        "explanation": f"Para comparar se llevan a un mismo denominador: {a}/{b} = {x}/{lcm} y {c}/{d} = {y}/{lcm}. Es mayor {'la de ' + who[1] if luis_more else 'la de ' + who[0]}. El tamaño de los números de una fracción no decide cuál es mayor.",
        "hints": ["Lleva las dos fracciones al mismo denominador.", "Piensa en 1/2 y 3/8: ¿la de números más grandes es la mayor?"], "packed": packed}


def muestra_sesgada(rng):
    n = rng.choice([20, 30, 40, 50])
    place, topic, concl = rng.choice([
        ("a la salida de un partido de fútbol", "deporte favorito", "el fútbol es el deporte favorito de todo el municipio"),
        ("en la fila de una panadería a las 6 de la mañana", "hora a la que se levantan", "en el municipio casi todos madrugan"),
        ("en la biblioteca del colegio", "gusto por la lectura", "a la mayoría de los estudiantes del colegio les gusta leer"),
        ("en la terminal de transporte", "frecuencia con la que viajan", "los habitantes del municipio viajan con mucha frecuencia"),
        ("en una feria ganadera", "actividad económica de su familia", "casi todas las familias del municipio viven de la ganadería")])
    packed = _pack(rng, "No, porque las personas encuestadas se parecen entre sí por el lugar donde se les preguntó y no representan a toda la población.", [
        f"Sí, porque {n} personas son una cantidad suficiente para cualquier conclusión.",
        "Sí, porque la mayoría de los encuestados respondió lo mismo.",
        "No, porque una encuesta solo es válida si se le pregunta a toda la población."])
    return packed and {
        "competencia": "argumentacion", "b": 0.4, "componente": "Estadística",
        "stem": f"Un grupo de estudiantes encuestó a {n} personas {place} sobre su {topic}. Con los resultados concluyó que {concl}. ¿Es válida la conclusión?",
        "explanation": "El problema no es el número de encuestados sino dónde se eligieron: quienes están en ese lugar tienen más probabilidad de responder de cierta manera. Una muestra debe parecerse a la población sobre la que se concluye.",
        "hints": ["Piensa quiénes suelen estar en ese lugar a esa hora.", "¿La muestra se parece a toda la población de la que se habla?"], "packed": packed}


FAMILIES = [regla_tres_inversa, interes_simple, cerca_rectangulo, tiempo_recorrido, pitagoras, volumen_tanque, conteo_combinaciones, ecuacion_plan,
            mediana, participacion_porcentual, tasa_de_cambio, rango_de_datos,
            sube_y_baja, oferta_comparada, promedio_con_nuevo_dato, comparar_fracciones, muestra_sesgada]
