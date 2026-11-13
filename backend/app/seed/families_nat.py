"""Familias de Ciencias Naturales: problemas con datos que cambian y clave calculada."""
from __future__ import annotations

from .math_families import _num, _pack, _th


# ----------------------------- Uso comprensivo del conocimiento -----------------------------

def densidad(rng):
    rho = rng.choice([0.5, 0.8, 1.5, 2, 2.5, 4, 8])
    vol = rng.choice([10, 20, 40, 50, 100])
    mass = rho * vol
    packed = _pack(rng, f"{_num(rho)} g/cm³", [f"{_num(vol / mass)} g/cm³", f"{_th(int(mass * vol))} g/cm³", f"{_num(abs(mass - vol))} g/cm³", f"{_num(mass + vol)} g/cm³", f"{_num(rho * 10)} g/cm³"])
    return packed and {
        "competencia": "uso", "b": -0.3, "componente": "Físico",
        "stem": f"Un bloque de {_num(mass)} g ocupa un volumen de {vol} cm³. ¿Cuál es su densidad?",
        "explanation": f"Densidad = masa ÷ volumen = {_num(mass)} ÷ {vol} = {_num(rho)} g/cm³.",
        "hints": ["La densidad dice cuánta masa hay en cada unidad de volumen.", "Divide la masa entre el volumen, no al revés."], "packed": packed}


def ley_de_ohm(rng):
    cur, res = rng.choice([0.5, 1, 2, 3, 4]), rng.choice([2, 4, 6, 10, 12])
    volt = cur * res
    kind = rng.choice(["V", "I", "R"])
    if kind == "V":
        stem, ans, unit = f"Por una resistencia de {res} Ω circula una corriente de {_num(cur)} A. ¿Qué voltaje hay entre sus extremos?", volt, "V"
        wrong = [res / cur, res + cur, abs(res - cur), volt * 2]
        expl = f"V = I × R = {_num(cur)} × {res} = {_num(volt)} V."
    elif kind == "I":
        stem, ans, unit = f"Una resistencia de {res} Ω se conecta a una batería de {_num(volt)} V. ¿Qué corriente circula por ella?", cur, "A"
        wrong = [volt * res, res / volt, volt + res, cur * 2 + 1]
        expl = f"I = V ÷ R = {_num(volt)} ÷ {res} = {_num(cur)} A."
    else:
        stem, ans, unit = f"Al conectar un bombillo a una batería de {_num(volt)} V circula una corriente de {_num(cur)} A. ¿Cuál es la resistencia del bombillo?", res, "Ω"
        wrong = [volt * cur, cur / volt, volt + cur, res + 3]
        expl = f"R = V ÷ I = {_num(volt)} ÷ {_num(cur)} = {res} Ω."
    packed = _pack(rng, f"{_num(float(ans))} {unit}", [f"{_num(round(float(w), 2))} {unit}" for w in wrong])
    return packed and {
        "competencia": "uso", "b": 0.2, "componente": "Físico", "stem": stem, "explanation": expl,
        "hints": ["La ley de Ohm relaciona voltaje, corriente y resistencia: V = I × R.", "Despeja la cantidad que te piden antes de reemplazar."], "packed": packed}


def segunda_ley(rng):
    mass, acc = rng.choice([2, 4, 5, 8, 10, 20]), rng.choice([0.5, 1.5, 2, 3, 4])
    force = mass * acc
    thing = rng.choice(["una carretilla", "un carrito de mercado", "una caja sobre una superficie sin fricción", "un trineo"])
    packed = _pack(rng, f"{_num(force)} N", [f"{_num(round(mass / acc, 2))} N", f"{_num(mass + acc)} N", f"{_num(force * 10)} N", f"{_num(round(acc / mass, 2))} N"])
    return packed and {
        "competencia": "uso", "b": 0.0, "componente": "Físico",
        "stem": f"¿Qué fuerza neta se necesita para que {thing} de {mass} kg adquiera una aceleración de {_num(acc)} m/s²?",
        "explanation": f"Segunda ley de Newton: F = m × a = {mass} × {_num(acc)} = {_num(force)} N.",
        "hints": ["La fuerza neta es proporcional a la masa y a la aceleración.", "F = m × a."], "packed": packed}


def concentracion(rng):
    grams, ml = rng.choice([5, 10, 20, 30, 40]), rng.choice([250, 500, 1000, 2000])
    conc = grams / (ml / 1000)
    solute = rng.choice(["sal", "azúcar", "abono soluble", "bicarbonato"])
    packed = _pack(rng, f"{_num(conc)} g/L", [f"{_num(round(grams / ml, 3))} g/L", f"{_num(grams * ml / 1000)} g/L", f"{_num(round(ml / grams, 1))} g/L", f"{_num(conc * 2)} g/L"])
    return packed and {
        "competencia": "uso", "b": 0.3, "componente": "Químico",
        "stem": f"Se disuelven {grams} g de {solute} en agua hasta completar {_th(ml)} mL de solución. ¿Cuál es la concentración en gramos por litro?",
        "explanation": f"{_th(ml)} mL son {_num(ml / 1000)} L. Concentración = {grams} g ÷ {_num(ml / 1000)} L = {_num(conc)} g/L.",
        "hints": ["La unidad pedida es gramos por litro: convierte primero los mililitros a litros.", "Concentración = cantidad de soluto ÷ volumen de la solución."], "packed": packed}


def cruce_genetico(rng):
    trait, dom, rec = rng.choice([("el color de la flor", "flor morada", "flor blanca"), ("la textura de la semilla", "semilla lisa", "semilla rugosa"),
                                  ("la altura de la planta", "planta alta", "planta enana"), ("el color del pelaje", "pelaje negro", "pelaje café"),
                                  ("el color de la vaina", "vaina verde", "vaina amarilla")])
    cross, p_rec = rng.choice([("Aa × Aa", 25), ("Aa × aa", 50), ("AA × aa", 0), ("AA × Aa", 0), ("aa × aa", 100)])
    ask_rec = rng.random() < 0.6
    ans = p_rec if ask_rec else 100 - p_rec
    packed = _pack(rng, f"{ans} %", [f"{x} %" for x in (0, 25, 50, 75, 100) if x != ans][: 4])
    return packed and {
        "competencia": "uso", "b": 0.4, "componente": "Biológico",
        "stem": f"En cierta especie, {trait} depende de un gen con dos alelos: A ({dom}) domina sobre a ({rec}). Si se cruzan dos individuos {cross}, ¿qué probabilidad tiene cada descendiente de presentar {rec if ask_rec else dom}?",
        "explanation": f"El rasgo recesivo ({rec}) solo aparece en individuos aa. En el cruce {cross}, la probabilidad de aa es {p_rec} %, y la de mostrar el rasgo dominante es {100 - p_rec} %.",
        "hints": ["Arma el cuadro de Punnett con los alelos de cada progenitor.", "El rasgo recesivo solo se ve cuando el individuo recibe dos alelos a."], "packed": packed}


def energia_trofica(rng):
    energy = rng.choice([10, 20, 40, 50, 80]) * 1000
    level, divisor, name = rng.choice([(1, 10, "consumidores primarios (herbívoros)"), (2, 100, "consumidores secundarios"), (3, 1000, "consumidores terciarios")])
    ans = energy // divisor
    packed = _pack(rng, f"{_th(ans)} kJ", [f"{_th(energy // d)} kJ" for d in (1, 10, 100, 1000) if d != divisor] + [f"{_th(energy - energy // 10)} kJ"])
    return packed and {
        "competencia": "uso", "b": 0.5, "componente": "Biológico",
        "stem": f"En un ecosistema, los productores almacenan {_th(energy)} kJ de energía. Si en cada paso de la cadena alimentaria solo cerca del 10 % de la energía pasa al nivel siguiente, ¿cuánta energía llega a los {name}?",
        "explanation": f"Se toma el 10 % en cada paso, {level} {'vez' if level == 1 else 'veces'}: {_th(energy)} ÷ {_th(divisor)} = {_th(ans)} kJ. El resto se pierde sobre todo como calor.",
        "hints": ["Cuenta cuántos pasos hay desde los productores hasta el nivel que te preguntan.", "En cada paso solo queda una décima parte."], "packed": packed}


def acidez_suelos(rng):
    vals = rng.sample([4.5, 5.0, 5.5, 6.0, 6.5, 7.5, 8.0, 8.5], 3)
    ask_acid = rng.random() < 0.5
    if not ask_acid and sum(v > 7 for v in vals) != 1:
        return None
    names = ["la parcela 1", "la parcela 2", "la parcela 3"]
    target = vals.index(min(vals)) if ask_acid else next(i for i, v in enumerate(vals) if v > 7)
    letters = {"A": "La de " + names[0] + ".", "B": "La de " + names[1] + ".", "C": "La de " + names[2] + ".",
               "D": "Ninguna: el pH no informa sobre la acidez." if ask_acid else "Todas: cualquier pH distinto de 7 es básico."}
    return {
        "competencia": "uso", "b": -0.2, "componente": "Químico",
        "context": "Un técnico midió el pH de muestras de suelo de tres parcelas: " + "; ".join(f"{n[3:]}, pH {_num(v)}" for n, v in zip(names, vals)) + ".",
        "stem": "¿Cuál muestra es la más ácida?" if ask_acid else "¿Cuál muestra es básica (alcalina)?",
        "explanation": ("En la escala de pH, entre más bajo el valor, más ácida la muestra. El menor es " + _num(min(vals)) + ".") if ask_acid
        else "Un pH mayor que 7 indica una muestra básica; menor que 7, ácida. Solo una de las tres supera 7.",
        "hints": ["El 7 es el punto neutro de la escala de pH.", "Por debajo de 7 la muestra es ácida; por encima, básica."], "packed": (letters, "ABC"[target])}


# ----------------------------- Explicación de fenómenos -----------------------------

def flota_o_se_hunde(rng):
    rho = rng.choice([0.4, 0.6, 0.8, 0.9, 1.2, 1.5, 2.5, 7.8])
    vol = rng.choice([10, 20, 50, 100])
    mass = rho * vol
    floats = rho < 1
    packed = _pack(rng, f"{'Flota' if floats else 'Se hunde'}, porque su densidad ({_num(rho)} g/cm³) es {'menor' if floats else 'mayor'} que la del agua.", [
        f"{'Se hunde' if floats else 'Flota'}, porque su densidad ({_num(rho)} g/cm³) es {'mayor' if floats else 'menor'} que la del agua.",
        f"Se hunde, porque todo objeto de más de {_num(mass / 2)} g es demasiado pesado para flotar.",
        f"Flota, porque su volumen ({vol} cm³) es pequeño comparado con el del recipiente."])
    return packed and {
        "competencia": "explicacion", "b": 0.3, "componente": "Físico",
        "stem": f"Un objeto macizo de {_num(mass)} g y {vol} cm³ se deja con cuidado en un recipiente con agua (densidad 1 g/cm³). ¿Qué ocurre y por qué?",
        "explanation": f"Densidad del objeto: {_num(mass)} ÷ {vol} = {_num(rho)} g/cm³. Un cuerpo macizo flota si es menos denso que el líquido y se hunde si es más denso. No depende solo de la masa ni solo del volumen.",
        "hints": ["Ni la masa sola ni el volumen solo deciden si algo flota.", "Calcula la densidad del objeto y compárala con la del agua."], "packed": packed}


def circuito_en_serie(rng):
    volt, r1, r2 = rng.choice([(12, 2, 4), (12, 3, 3), (12, 4, 2), (24, 4, 4), (24, 6, 6), (24, 2, 6), (9, 3, 6), (6, 1, 2), (6, 2, 1), (12, 2, 2), (24, 3, 5), (24, 8, 4)])
    i1, i2 = volt / r1, volt / (r1 + r2)
    packed = _pack(rng, f"Disminuye de {_num(i1)} A a {_num(i2)} A, porque la resistencia total del circuito aumenta.", [
        f"Aumenta de {_num(i1)} A a {_num(volt / r2 + i1)} A, porque hay más elementos por donde circular.",
        f"Se mantiene en {_num(i1)} A, porque la batería es la misma.",
        "Se vuelve cero, porque dos resistencias en serie bloquean el paso de la corriente."])
    return packed and {
        "competencia": "explicacion", "b": 0.7, "componente": "Físico",
        "stem": f"Un circuito tiene una batería de {volt} V y una resistencia de {r1} Ω. Luego se conecta en serie una segunda resistencia de {r2} Ω. ¿Qué pasa con la corriente y por qué?",
        "explanation": f"Antes: I = {volt} ÷ {r1} = {_num(i1)} A. En serie las resistencias se suman ({r1} + {r2} = {r1 + r2} Ω), así que I = {volt} ÷ {r1 + r2} = {_num(i2)} A. El voltaje de la batería no cambia; cambia la resistencia total.",
        "hints": ["En un circuito en serie, las resistencias se suman.", "Con el mismo voltaje, ¿qué le pasa a la corriente si la resistencia crece?"], "packed": packed}


# ----------------------------- Indagación -----------------------------

EXPERIMENTS = [
    ("Para saber si la cantidad de abono influye en el crecimiento del fríjol, un grupo siembra plantas iguales y a cada una le aplica una dosis distinta de abono. Cada semana mide la altura.",
     "la dosis de abono", "la altura de las plantas", "la cantidad de agua de riego", "el color de la maceta del salón vecino"),
    ("Para averiguar si la temperatura del agua cambia el tiempo en que se disuelve una pastilla efervescente, unos estudiantes ponen pastillas iguales en vasos con agua a distintas temperaturas y cronometran.",
     "la temperatura del agua", "el tiempo que tarda en disolverse la pastilla", "la cantidad de agua en cada vaso", "la marca del cronómetro de otro grupo"),
    ("Para estudiar si la longitud de la cuerda afecta el tiempo de oscilación de un péndulo, un estudiante cuelga la misma pesa de cuerdas de distinto largo y mide cuánto tarda en ir y volver.",
     "la longitud de la cuerda", "el tiempo de una oscilación", "la masa de la pesa", "la hora del día en que se escribe el informe"),
    ("Para comprobar si la luz influye en la germinación, unas estudiantes ponen semillas iguales en algodón húmedo: unas en un lugar iluminado y otras dentro de una caja cerrada. Cuentan cuántas germinan.",
     "la presencia de luz", "el número de semillas que germinan", "la humedad del algodón", "el nombre de quien cuenta las semillas"),
    ("Para saber si el tipo de suelo cambia la velocidad con que se filtra el agua, un grupo vierte la misma cantidad de agua sobre arena, arcilla y tierra negra, y mide cuánto tarda en pasar.",
     "el tipo de suelo", "el tiempo que tarda el agua en filtrarse", "la cantidad de agua vertida", "el precio del embudo"),
    ("Para investigar si la sal cambia la temperatura a la que hierve el agua, unos estudiantes calientan ollas con la misma cantidad de agua y distintas cucharadas de sal, y registran la temperatura de ebullición.",
     "la cantidad de sal", "la temperatura de ebullición", "la cantidad de agua en cada olla", "el color de las ollas de otra cocina"),
    ("Para averiguar si la inclinación de una rampa afecta la rapidez de un carrito, una estudiante suelta el mismo carrito desde rampas con distinta inclinación y mide el tiempo que tarda en bajar.",
     "la inclinación de la rampa", "el tiempo de bajada del carrito", "la longitud de la rampa", "la marca del cuaderno de apuntes"),
    ("Para saber si el ejercicio cambia la frecuencia cardiaca, un grupo mide el pulso de varios compañeros en reposo y después de trotar uno, dos y tres minutos.",
     "el tiempo de ejercicio", "la frecuencia cardiaca", "la forma de medir el pulso", "el color de los tenis"),
]


def variables_experimento(rng):
    text, indep, dep, ctrl, noise = rng.choice(EXPERIMENTS)
    kind = rng.choice(["independiente", "dependiente", "controlada"])
    correct = {"independiente": indep, "dependiente": dep, "controlada": ctrl}[kind]
    question = {"independiente": "¿Cuál es la variable independiente (la que los investigadores cambian a propósito)?",
                "dependiente": "¿Cuál es la variable dependiente (la que se mide como resultado)?",
                "controlada": "¿Cuál de las siguientes debe mantenerse igual en todos los casos para que la comparación sea justa?"}[kind]
    cap = lambda s: s[0].upper() + s[1:] + "."
    packed = _pack(rng, cap(correct), [cap(x) for x in (indep, dep, ctrl, noise) if x != correct])
    return packed and {
        "competencia": "indagacion", "b": {"independiente": -0.2, "dependiente": 0.0, "controlada": 0.4}[kind], "componente": "Indagación",
        "context": text, "stem": question,
        "explanation": f"Lo que se cambia a propósito es {indep} (independiente); lo que se mide es {dep} (dependiente); y {ctrl} debe mantenerse igual para que solo una cosa cambie a la vez.",
        "hints": ["Pregúntate: ¿qué cambiaron a propósito y qué midieron?", "Para comparar con justicia, solo debe cambiar una cosa a la vez."], "packed": packed}


def conclusion_de_tabla(rng):
    doses = [0, 10, 20, 30, 40]
    base = rng.randint(8, 14)
    peak = rng.random() < 0.5
    if peak:
        top = rng.choice([2, 3])
        vals = [base]
        for i in range(1, 5):
            vals.append(vals[-1] + rng.randint(3, 5) if i <= top else vals[-1] - rng.randint(3, 6))
        correct = f"El crecimiento aumentó hasta la dosis de {doses[top]} g y disminuyó con dosis mayores."
        wrong = ["A mayor dosis de abono, mayor crecimiento en todo el rango probado.", "El abono no tiene ninguna relación con el crecimiento de las plantas.",
                 f"La dosis de {doses[4]} g es la mejor, porque es la mayor cantidad de abono."]
    else:
        vals = [base]
        for _ in range(4):
            vals.append(vals[-1] + rng.randint(2, 5))
        correct = "En el rango de dosis probado, a mayor dosis de abono se registró mayor crecimiento."
        wrong = ["Cualquier planta crecerá más mientras más abono reciba, sin límite.", "El abono no tiene ninguna relación con el crecimiento de las plantas.",
                 f"La dosis de {doses[1]} g produjo el mayor crecimiento."]
    plant = rng.choice(["maíz", "tomate", "fríjol", "cilantro"])
    packed = _pack(rng, correct, wrong)
    return packed and {
        "competencia": "indagacion", "b": 0.5 if peak else 0.2, "componente": "Indagación",
        "context": f"Unos estudiantes sembraron plantas de {plant} iguales y aplicaron a cada grupo una dosis distinta de abono. Crecimiento promedio en cuatro semanas: "
                   + "; ".join(f"{d} g: {v} cm" for d, v in zip(doses, vals)) + ".",
        "stem": "¿Cuál conclusión está respaldada por estos datos?",
        "explanation": ("Los datos suben y luego bajan: hay una dosis a partir de la cual más abono perjudica." if peak
                        else "Los datos solo permiten hablar de las dosis y de la planta que se probaron: no se puede asegurar qué pasa con dosis mayores ni con otras plantas.") + " Una conclusión válida no va más allá de lo que se midió.",
        "hints": ["Mira cómo cambia el crecimiento de una dosis a la siguiente.", "Descarta las conclusiones que hablan de casos que no se probaron."], "packed": packed}


def promedio_de_mediciones(rng):
    mean = rng.choice(range(12, 31)) / 10
    d = rng.choice([1, 2, 3]) / 10
    vals = [round(mean - d, 1), mean, round(mean + d, 1)]
    rng.shuffle(vals)
    if vals[0] == mean:
        return None
    what = rng.choice(["el tiempo que tarda en caer una pelota desde un balcón", "el tiempo de diez oscilaciones de un péndulo, dividido entre diez", "el tiempo que tarda un carrito en bajar una rampa"])
    f = lambda v: f"{v:.1f}".replace(".", ",")
    packed = _pack(rng, f"{f(mean)} s, el promedio de las tres mediciones.", [
        f"{f(vals[0])} s, porque la primera medición es la más confiable.", f"{f(max(vals))} s, porque el valor más alto incluye todo el recorrido.",
        f"{f(sum(vals))} s, la suma de las tres mediciones.", f"{f(min(vals))} s, porque el valor más bajo tiene menos error."])
    return packed and {
        "competencia": "indagacion", "b": -0.1, "componente": "Indagación",
        "stem": f"Un estudiante midió tres veces {what} y obtuvo {f(vals[0])} s, {f(vals[1])} s y {f(vals[2])} s. ¿Qué valor conviene reportar?",
        "explanation": f"Repetir y promediar reduce el efecto de los errores al medir: ({f(vals[0])} + {f(vals[1])} + {f(vals[2])}) ÷ 3 = {f(mean)} s.",
        "hints": ["¿Para qué sirve repetir una medición varias veces?", "Ninguna medición sola es mejor que las otras: se combinan."], "packed": packed}


def grupo_control(rng):
    n = rng.choice([10, 15, 20, 30])
    scene, control, treated, noise = rng.choice([
        (f"Para probar un abono nuevo, una agrónoma siembra {2 * n} plantas de tomate iguales. A {n} les aplica el abono nuevo y a las otras {n} no les aplica ningún abono. Todas reciben la misma agua y luz.",
         "Las plantas que no reciben abono.", "Las plantas que reciben el abono nuevo.", "Las plantas de otra finca."),
        (f"Para saber si un enjuague reduce las bacterias de la boca, {2 * n} voluntarios se dividen en dos grupos de {n}: unos usan el enjuague y otros hacen buches con agua. Luego se cuentan las bacterias.",
         "Los voluntarios que usan solo agua.", "Los voluntarios que usan el enjuague.", "Los investigadores que cuentan las bacterias."),
        (f"Para evaluar un alimento concentrado, un criador separa {2 * n} pollos de la misma edad: {n} comen el concentrado nuevo y {n} siguen con el alimento de siempre. Cada semana se pesan.",
         "Los pollos que siguen con el alimento de siempre.", "Los pollos que comen el concentrado nuevo.", "Los pollos más pesados de los dos grupos."),
        (f"Para comprobar si la música afecta la concentración, {2 * n} estudiantes resuelven la misma prueba: {n} con música y {n} en silencio.",
         "Los estudiantes que resuelven la prueba en silencio.", "Los estudiantes que resuelven la prueba con música.", "Los estudiantes que obtienen mejor nota."),
    ])
    packed = _pack(rng, control, [treated, noise, "No hay grupo control, porque los dos grupos participan en el experimento."])
    return packed and {
        "competencia": "indagacion", "b": 0.1, "componente": "Indagación", "context": scene, "stem": "¿Cuál es el grupo control de este experimento?",
        "explanation": "El grupo control no recibe el tratamiento que se quiere probar y sirve de punto de comparación: sin él no se sabría si el cambio se debe al tratamiento.",
        "hints": ["El grupo control es el punto de comparación.", "Busca el grupo al que no se le aplica lo que se está probando."], "packed": packed}


FAMILIES = [densidad, ley_de_ohm, segunda_ley, concentracion, cruce_genetico, energia_trofica, acidez_suelos,
            flota_o_se_hunde, circuito_en_serie, variables_experimento, conclusion_de_tabla, promedio_de_mediciones, grupo_control]
