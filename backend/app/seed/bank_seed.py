"""Banco semilla de ítems ORIGINALES (no provienen de cuadernillos del ICFES).

Todos entran en estado 'borrador': sirven para probar la plataforma, pero deben ser revisados
y aprobados por un docente del área antes de usarse con estudiantes en producción.
El parámetro b (dificultad) es una estimación inicial; se recalibra con respuestas reales.
"""
from __future__ import annotations

import random

ITEMS: list[dict] = []


def I(id, area, comp, pool, b, stem, opts, correct, expl, hints, ctx=None, a=1.0, componente=None):
    # El orden de las opciones se baraja (siempre igual para cada pregunta) para que la clave no caiga
    # casi siempre en la misma letra. Por eso ninguna explicación ni pista debe mencionar letras.
    order = list(range(4))
    random.Random(f"orden:{id}").shuffle(order)
    correct = "ABCD"[order.index("ABCD".index(correct))]
    opts = [opts[i] for i in order]
    ITEMS.append({
        "id": id, "area": area, "competencia": comp, "pool": pool, "a": a, "b": b, "c": 0.25,
        "context": ctx, "stem": stem, "options": dict(zip("ABCD", opts)), "correct": correct,
        "explanation": expl, "hints": hints, "componente": componente, "status": "borrador", "origin": "semilla",
    })


# =============================== LECTURA CRÍTICA ===============================
T1 = ("En muchas fincas de la cordillera, el café se siembra bajo árboles de guamo y nogal. A este sistema se le llama "
      "café de sombra. Los árboles reducen la temperatura del cultivo, conservan la humedad del suelo y sirven de refugio "
      "a aves que se alimentan de insectos. Sin embargo, un cafetal de sombra produce menos granos por hectárea que uno a "
      "pleno sol, por lo que algunos productores talan los árboles para aumentar la cosecha. Estudios recientes advierten "
      "que, con temporadas secas más largas, los cafetales sin sombra pierden más plantas y exigen más riego y abono. Lo "
      "que parece una ganancia inmediata puede convertirse en un costo mayor en pocos años.")
T2 = ("Prohibir los celulares en el salón parece la solución más sencilla a la distracción. Quienes defienden la medida "
      "recuerdan que una notificación basta para interrumpir la concentración de todo un grupo. Pero la prohibición total "
      "parte de una idea discutible: que el aparato es el problema y no el uso que se le da. Un celular también es "
      "calculadora, diccionario y biblioteca, y en muchos colegios rurales es el único dispositivo con el que cuentan los "
      "estudiantes. Más útil que prohibir sería acordar con el grupo cuándo se usa y para qué. Una norma que los "
      "estudiantes ayudan a construir se cumple mejor que una que solo se les impone.")
T3 = ("Cuando el río creció, la abuela no corrió a subir los muebles como los demás. Se sentó en la mecedora del corredor "
      "y se puso a desgranar maíz. —El agua sabe hasta dónde llega —dijo, sin levantar la vista. Los vecinos pasaban con "
      "colchones al hombro y la miraban como se mira a quien ha perdido el juicio. A la madrugada, el río se detuvo a dos "
      "pasos del primer escalón, lamió la tierra un rato y empezó a devolverse. La abuela recogió las tusas, apagó la vela "
      "y se fue a dormir. Nadie en el pueblo volvió a decirle qué hacer cuando lloviera.")
T4 = ("AVISO DE LA JUNTA DE ACCIÓN COMUNAL\nJornada de vacunación de mascotas\nSábado 14, de 8:00 a. m. a 12:00 m., en la "
      "caseta comunal.\nPerros y gatos mayores de 3 meses.\nTraiga el carné de vacunas si lo tiene.\nGratis para los primeros "
      "80 animales; después, $5.000 por dosis.\nNo se vacunarán animales enfermos ni hembras preñadas.")

I("LEC-001", "LEC", "locales", "diagnostico", -1.2, "Según el texto, ¿por qué algunos productores talan los árboles de sus cafetales?",
  ["Porque los árboles atraen insectos que dañan el grano.", "Porque el cafetal a pleno sol produce más granos por hectárea.",
   "Porque los árboles consumen el abono del cultivo.", "Porque las temporadas secas son cada vez más largas."], "B",
  "El texto dice que el cafetal de sombra produce menos granos por hectárea y que por eso algunos productores talan los árboles para aumentar la cosecha.",
  ["Busca la oración que empieza con 'Sin embargo': allí está la razón.", "La pregunta es por la intención de los productores, no por lo que advierten los estudios."], ctx=T1)
I("LEC-002", "LEC", "global", "diagnostico", -0.2, "En el texto, la expresión 'Sin embargo' sirve para",
  ["dar un ejemplo de los beneficios de la sombra.", "introducir una desventaja que contrasta con los beneficios mencionados.",
   "repetir con otras palabras la idea anterior.", "presentar la conclusión de los estudios recientes."], "B",
  "Antes del conector se enumeran beneficios de la sombra; después aparece una desventaja (menos producción). 'Sin embargo' marca ese contraste.",
  ["Compara lo que se dice antes y después del conector: ¿van en la misma dirección?"], ctx=T1)
I("LEC-003", "LEC", "global", "practica", 0.0, "¿Cuál de las siguientes opciones resume mejor la idea principal del texto?",
  ["El café de sombra es el sistema más antiguo de la cordillera.", "Las aves son necesarias para controlar las plagas del café.",
   "Quitar la sombra aumenta la cosecha a corto plazo, pero puede salir más costoso con el tiempo.", "Los productores deben abandonar el cultivo de café por las sequías."], "C",
  "El texto contrapone la ganancia inmediata de talar con los costos posteriores (más riego, abono y plantas perdidas). Esa tensión es la idea central.",
  ["La idea principal debe cubrir todo el texto, no solo un detalle.", "Fíjate en la última oración: suele condensar el mensaje."], ctx=T1)
I("LEC-004", "LEC", "critica", "diagnostico", 1.0, "¿Cuál de los siguientes hallazgos debilitaría la advertencia con la que termina el texto?",
  ["Que las aves prefieren los cafetales con árboles de guamo.", "Que en temporadas secas largas los cafetales a pleno sol mantienen sus costos y su número de plantas.",
   "Que algunos productores no saben cuántas hectáreas tienen.", "Que el café de sombra se vende a mejor precio en el exterior."], "B",
  "La advertencia se apoya en que los cafetales sin sombra pierden plantas y cuestan más en sequía. Si eso no ocurriera, la advertencia perdería su sustento.",
  ["Primero identifica en qué dato se apoya la advertencia final.", "Debilitar un argumento es contradecir la evidencia que lo sostiene."], ctx=T1)

I("LEC-005", "LEC", "locales", "practica", -1.3, "Según el autor, ¿qué ocurre con el celular en muchos colegios rurales?",
  ["Está prohibido por los rectores.", "Es el único dispositivo con el que cuentan los estudiantes.", "Se usa solo como calculadora.", "Distrae más que en los colegios urbanos."], "B",
  "El texto afirma que en muchos colegios rurales el celular es el único dispositivo con el que cuentan los estudiantes.",
  ["La respuesta está escrita casi con las mismas palabras en el texto."], ctx=T2)
I("LEC-006", "LEC", "global", "diagnostico", -0.4, "¿Cuál es la tesis que defiende el autor?",
  ["Los celulares deben prohibirse porque interrumpen la concentración.", "Es mejor acordar con los estudiantes las reglas de uso del celular que prohibirlo.",
   "Los colegios rurales necesitan más computadores.", "Las normas escolares nunca se cumplen."], "B",
  "El autor reconoce el argumento a favor de prohibir, pero sostiene que 'más útil que prohibir sería acordar con el grupo cuándo se usa y para qué'.",
  ["La tesis es la postura del autor, no la de quienes él cita.", "Busca la oración donde el autor propone qué hacer."], ctx=T2)
I("LEC-007", "LEC", "global", "practica", 0.4, "La segunda oración del texto ('Quienes defienden la medida recuerdan que...') cumple la función de",
  ["presentar el argumento de la postura que el autor va a discutir.", "resumir la opinión del autor sobre los celulares.",
   "dar un ejemplo de una norma construida con los estudiantes.", "explicar cómo funcionan las notificaciones."], "A",
  "El autor expone primero la razón de quienes apoyan la prohibición y luego la discute con el 'Pero' que sigue.",
  ["Pregúntate quién habla en esa oración: ¿el autor o quienes defienden la medida?"], ctx=T2)
I("LEC-008", "LEC", "critica", "diagnostico", 0.8, "La última oración del texto se apoya en el supuesto de que",
  ["los estudiantes siempre desobedecen a los adultos.", "participar en la creación de una norma aumenta la disposición a cumplirla.",
   "las normas escritas son más claras que las habladas.", "los docentes no saben usar el celular."], "B",
  "Decir que una norma construida con los estudiantes 'se cumple mejor' supone que participar en ella genera compromiso con su cumplimiento.",
  ["Un supuesto es una idea que el autor da por cierta sin demostrarla.", "¿Qué tendría que ser verdad para que la última oración tenga sentido?"], ctx=T2)
I("LEC-009", "LEC", "critica", "simulacro", 1.3, "Un rector afirma: 'En mi colegio prohibimos los celulares y las notas mejoraron'. ¿Esta afirmación refuta la postura del autor?",
  ["Sí, porque demuestra que el celular es el problema.", "Sí, porque el autor dice que la prohibición nunca funciona.",
   "No, porque un solo caso no muestra que acordar reglas de uso habría dado peores resultados.", "No, porque los rectores no pueden opinar sobre el tema."], "C",
  "El autor no dice que prohibir sea inútil, sino que acordar sería más útil. Un caso aislado, sin comparación con la alternativa, no basta para refutarlo.",
  ["Revisa qué afirma exactamente el autor: ¿que prohibir no sirve, o que hay algo mejor?"], ctx=T2)

I("LEC-010", "LEC", "locales", "diagnostico", -1.5, "¿Qué hacía la abuela mientras el río crecía?",
  ["Subía los muebles con los vecinos.", "Desgranaba maíz en la mecedora.", "Cargaba colchones al hombro.", "Rezaba con una vela encendida."], "B",
  "El relato dice que se sentó en la mecedora del corredor y se puso a desgranar maíz.",
  ["Vuelve a la segunda oración del relato."], ctx=T3)
I("LEC-011", "LEC", "global", "diagnostico", -0.6, "Al comienzo del relato, la actitud de los vecinos hacia la abuela es de",
  ["admiración por su valentía.", "incredulidad: piensan que no está actuando con cordura.", "envidia porque su casa es más alta.", "indiferencia, porque no la conocen."], "B",
  "La miran 'como se mira a quien ha perdido el juicio', es decir, creen que su calma es una locura.",
  ["Interpreta la comparación 'como se mira a quien ha perdido el juicio'."], ctx=T3)
I("LEC-012", "LEC", "global", "practica", 0.2, "La última oración del relato sugiere que los vecinos",
  ["dejaron de hablarle a la abuela por terquedad.", "reconocieron que la abuela sabía más que ellos sobre el río.", "se fueron del pueblo después de la creciente.", "nunca volvieron a ver llover."], "B",
  "Que nadie volviera a decirle qué hacer indica que su conocimiento quedó demostrado y fue respetado.",
  ["Relaciona el final con lo que pasó en la madrugada.", "¿Por qué alguien deja de dar consejos a otra persona?"], ctx=T3)
I("LEC-013", "LEC", "critica", "practica", 0.6, "Con la expresión 'el río [...] lamió la tierra un rato', el narrador",
  ["describe con precisión científica la creciente.", "le atribuye al río un comportamiento de ser vivo, lo que refuerza la idea de que 'el agua sabe'.",
   "muestra que la abuela estaba equivocada.", "indica que el río estaba contaminado."], "B",
  "'Lamer' es una acción de un ser vivo. Esa personificación conecta con la frase de la abuela: el río parece actuar con conocimiento.",
  ["¿Un río puede 'lamer'? Piensa qué efecto busca el narrador con ese verbo."], ctx=T3)

I("LEC-014", "LEC", "locales", "practica", -1.0, "Según el aviso, ¿quiénes deben pagar por la vacuna?",
  ["Todos los dueños de gatos.", "Quienes no lleven el carné de vacunas.", "Quienes lleguen después de los primeros 80 animales.", "Quienes lleven más de una mascota."], "C",
  "El aviso indica que es gratis para los primeros 80 animales y que después cuesta $5.000 por dosis.",
  ["Ubica la línea del aviso que habla de precio."], ctx=T4)
I("LEC-015", "LEC", "locales", "diagnostico", -0.8, "Una persona lleva a la jornada un gato sano de dos meses. De acuerdo con el aviso, el gato",
  ["será vacunado gratis.", "será vacunado si paga $5.000.", "no será vacunado por su edad.", "será vacunado solo si lleva carné."], "C",
  "La jornada es para perros y gatos mayores de 3 meses; uno de dos meses no cumple la condición.",
  ["Revisa las condiciones que deben cumplir los animales."], ctx=T4)
I("LEC-016", "LEC", "global", "simulacro", -1.2, "El propósito principal del aviso es",
  ["explicar por qué las vacunas son importantes.", "informar las condiciones de la jornada para que la comunidad asista.", "vender vacunas a bajo precio.", "regañar a quienes no vacunan a sus mascotas."], "B",
  "El aviso entrega fecha, lugar, requisitos y costos: busca convocar e informar cómo participar.",
  ["Pregúntate para qué alguien pegaría este aviso en la caseta."], ctx=T4)
I("LEC-017", "LEC", "critica", "simulacro", 0.5, "¿Cuál dato, que el aviso NO incluye, sería más útil para quien quiere decidir si lleva a su mascota?",
  ["El nombre del presidente de la junta.", "Contra qué enfermedad es la vacuna que se aplicará.", "El número de casas del barrio.", "El color de la caseta comunal."], "B",
  "Para decidir si la mascota necesita esa dosis hay que saber qué vacuna se aplica; es la información relevante que falta.",
  ["Evalúa qué información cambiaría la decisión del lector."], ctx=T4)

# =============================== MATEMÁTICAS ===============================
MT1 = "Ventas de panela en una tienda (kg): lunes 12, martes 18, miércoles 15, jueves 9, viernes 21."
I("MAT-001", "MAT", "interpretacion", "diagnostico", -1.2, "¿Entre qué días consecutivos se presentó el mayor aumento en las ventas?",
  ["De lunes a martes.", "De martes a miércoles.", "De miércoles a jueves.", "De jueves a viernes."], "D",
  "Los cambios son: +6, −3, −6 y +12. El mayor aumento (12 kg) ocurre de jueves a viernes.",
  ["Calcula la diferencia entre cada día y el siguiente.", "Solo cuentan los cambios positivos."], ctx=MT1, componente="Estadística")
I("MAT-002", "MAT", "interpretacion", "diagnostico", 0.0, "Un tanque de 500 litros se desocupa a ritmo constante. Dos horas después de abrir la llave tiene 380 litros. ¿Cuál expresión representa los litros L que quedan después de t horas?",
  ["L = 500 − 120t", "L = 500 − 60t", "L = 380 − 60t", "L = 500 + 60t"], "B",
  "En 2 horas salieron 120 litros, es decir, 60 litros por hora. Empieza en 500 y disminuye 60 por cada hora: L = 500 − 60t.",
  ["¿Cuántos litros salieron en las dos horas?", "Divide lo que salió entre el tiempo para hallar el ritmo por hora."], componente="Álgebra y cálculo")
I("MAT-003", "MAT", "interpretacion", "diagnostico", 0.8, "En un colegio de 240 estudiantes, el 50 % llega en bus, el 25 % en moto y el resto se reparte por igual entre quienes llegan a pie y en bicicleta. ¿Cuántos estudiantes llegan en bicicleta?",
  ["30", "60", "25", "15"], "A",
  "Bus y moto suman 75 %; queda 25 %, que se reparte por igual: 12,5 % en bicicleta. El 12,5 % de 240 es 30.",
  ["¿Qué porcentaje queda después de bus y moto?", "Ese porcentaje se divide en dos partes iguales."], componente="Estadística")
I("MAT-004", "MAT", "formulacion", "diagnostico", -1.0, "Un jornal se paga a $60.000. Si un trabajador recibió $420.000, ¿cuántos jornales trabajó?",
  ["6", "7", "8", "9"], "B", "420.000 ÷ 60.000 = 7 jornales.",
  ["Necesitas saber cuántas veces cabe 60.000 en 420.000."], componente="Álgebra y cálculo")
I("MAT-005", "MAT", "formulacion", "diagnostico", 0.0, "Una camisa cuesta $80.000 y tiene un descuento del 15 %. ¿Cuánto se paga por ella?",
  ["$65.000", "$68.000", "$12.000", "$92.000"], "B",
  "El 15 % de 80.000 es 12.000. Se paga 80.000 − 12.000 = $68.000.",
  ["Calcula primero cuánto vale el descuento.", "El descuento se resta del precio original."], componente="Álgebra y cálculo")
I("MAT-006", "MAT", "formulacion", "diagnostico", 0.9, "Un terreno rectangular tiene 30 m de largo y un perímetro de 100 m. ¿Cuál es su área?",
  ["3.000 m²", "2.100 m²", "600 m²", "1.500 m²"], "C",
  "Perímetro = 2(largo + ancho) = 100, entonces largo + ancho = 50 y el ancho es 20 m. Área = 30 × 20 = 600 m².",
  ["Usa el perímetro para hallar el ancho.", "El perímetro es dos veces la suma del largo y el ancho."], componente="Geometría")
I("MAT-007", "MAT", "argumentacion", "diagnostico", 0.3, "Pedro afirma: 'Si multiplico un número por 2, siempre obtengo un número mayor que el original'. ¿Cuál de estos números muestra que la afirmación es falsa?",
  ["5", "1/2", "−3", "100"], "C",
  "2 × (−3) = −6, que es menor que −3. Un solo contraejemplo basta para mostrar que la afirmación no se cumple siempre.",
  ["Prueba cada número: multiplícalo por 2 y compara.", "Piensa qué pasa con los números negativos."], componente="Álgebra y cálculo")
I("MAT-008", "MAT", "argumentacion", "diagnostico", 1.1, "Las notas de cinco estudiantes son 3,0; 3,2; 3,4; 3,6 y 5,0. Un docente dice: 'La mayoría del grupo tiene una nota superior al promedio'. ¿Es correcta la afirmación?",
  ["Sí, porque el promedio es mayor que 3,0.", "Sí, porque tres notas son mayores que 3,2.", "No, porque solo una nota está por encima del promedio.", "No, porque el promedio no se puede calcular con decimales."], "C",
  "El promedio es 18,2 ÷ 5 = 3,64. Solo la nota 5,0 lo supera: un dato muy alto sube el promedio por encima de casi todo el grupo.",
  ["Calcula el promedio antes de decidir.", "Compara cada nota con el promedio que obtuviste."], componente="Estadística")
I("MAT-009", "MAT", "formulacion", "simulacro", 0.0, "Una receta para 4 personas lleva 300 g de arroz. ¿Cuánto arroz se necesita para 10 personas, manteniendo la proporción?",
  ["1.200 g", "600 g", "750 g", "1.000 g"], "C", "Por persona son 300 ÷ 4 = 75 g. Para 10 personas: 75 × 10 = 750 g.",
  ["Halla primero la cantidad para una persona."], componente="Álgebra y cálculo")
I("MAT-010", "MAT", "interpretacion", "simulacro", 0.5, "El costo de un domicilio, en pesos, está dado por C(x) = 2.500x + 8.000, donde x es la distancia en kilómetros. ¿Qué representa el 8.000?",
  ["El costo por cada kilómetro.", "El cargo fijo que se cobra sin importar la distancia.", "La distancia máxima del domicilio.", "El costo total de un domicilio de un kilómetro."], "B",
  "Cuando x = 0 el costo es 8.000: es el valor fijo. El 2.500 es lo que aumenta por cada kilómetro.",
  ["¿Cuánto vale C cuando x es cero?"], componente="Álgebra y cálculo")
I("MAT-011", "MAT", "argumentacion", "simulacro", 0.9, "Se lanza una moneda equilibrada tres veces y en las tres cae cara. Ana dice que en el cuarto lanzamiento 'es más probable que caiga sello'. ¿Tiene razón?",
  ["Sí, porque ya salieron demasiadas caras.", "Sí, porque la moneda debe equilibrar los resultados.", "No, porque cada lanzamiento es independiente y la probabilidad de sello sigue siendo 1/2.", "No, porque es seguro que volverá a caer cara."], "C",
  "La moneda no 'recuerda' los resultados anteriores. En cada lanzamiento la probabilidad de cara y de sello es 1/2.",
  ["¿El resultado de un lanzamiento cambia la moneda para el siguiente?"], componente="Estadística")

# =============================== SOCIALES Y CIUDADANAS ===============================
ST1 = ("Una alcaldía propone construir una vía que atraviesa una vereda. Un transportador afirma que la obra reducirá los "
       "costos para sacar las cosechas. Una líder comunal advierte que el trazado afectará la quebrada que abastece el acueducto veredal.")
I("SOC-001", "SOC", "pensamiento_social", "diagnostico", -1.2, "En Colombia, ¿cuál rama del poder público tiene como función principal hacer las leyes?",
  ["La rama ejecutiva.", "La rama legislativa.", "La rama judicial.", "Los organismos de control."], "B",
  "El Congreso de la República, que conforma la rama legislativa, es el encargado de hacer las leyes.",
  ["Piensa en qué institución se debaten y aprueban las leyes."])
I("SOC-002", "SOC", "pensamiento_social", "diagnostico", -0.3, "Una persona considera que una entidad le está vulnerando su derecho fundamental a la salud y necesita protección inmediata. ¿Qué mecanismo constitucional es el más adecuado?",
  ["La acción de tutela.", "El referendo.", "La acción popular.", "La revocatoria del mandato."], "A",
  "La acción de tutela protege de manera inmediata los derechos fundamentales cuando son vulnerados o amenazados.",
  ["Se trata de un derecho fundamental de una persona concreta y es urgente.", "Descarta los mecanismos que sirven para decisiones colectivas."])
I("SOC-003", "SOC", "pensamiento_social", "diagnostico", 0.6, "La Constitución de 1991 define a Colombia como un Estado social de derecho. Esto implica, principalmente, que el Estado",
  ["solo debe castigar a quienes incumplen las leyes.", "debe garantizar los derechos y unas condiciones de vida dignas para la población.", "puede suspender los derechos cuando lo considere necesario.", "debe ser administrado por los partidos más votados."], "B",
  "El carácter 'social' significa que el Estado no se limita a hacer cumplir la ley: está obligado a garantizar derechos y condiciones de vida dignas.",
  ["Fíjate en la palabra 'social': ¿qué le agrega al Estado de derecho?"])
I("SOC-004", "SOC", "perspectivas", "diagnostico", -0.8, "¿En qué se diferencian las posturas del transportador y de la líder comunal?",
  ["Uno prioriza el beneficio económico de la vía; la otra, la protección de la fuente de agua.", "Uno está a favor de la alcaldía y la otra está en contra de las cosechas.", "Ambos rechazan la vía, pero por razones distintas.", "Uno habla del pasado y la otra del futuro."], "A",
  "El transportador valora la reducción de costos; la líder, el riesgo para la quebrada que surte el acueducto. Son intereses distintos frente a la misma obra.",
  ["Identifica qué le importa a cada persona."], ctx=ST1)
I("SOC-005", "SOC", "perspectivas", "diagnostico", 0.1, "¿Qué información ayudaría más a evaluar el argumento de la líder comunal?",
  ["El número de camiones que tiene el transportador.", "Un estudio técnico sobre el efecto de la obra en la quebrada.", "La opinión del alcalde sobre la líder.", "El precio actual de las cosechas."], "B",
  "Su argumento es que la obra afectará la quebrada; un estudio técnico permite verificar si ese efecto ocurriría y qué tan grave sería.",
  ["¿Qué es exactamente lo que ella afirma que pasará?", "Busca la evidencia que confirmaría o descartaría esa afirmación."], ctx=ST1)
I("SOC-006", "SOC", "perspectivas", "diagnostico", 0.9, "Un periódico titula: 'Sube el desempleo por culpa de los migrantes'. La noticia solo cita la opinión de un comerciante. ¿Cuál es el principal problema de esta noticia?",
  ["Que habla de un tema económico.", "Que presenta como un hecho una relación de causa que solo se apoya en una opinión.", "Que el comerciante no es periodista.", "Que el titular es demasiado corto."], "B",
  "El titular afirma una causa ('por culpa de'), pero la única evidencia es una opinión. No hay datos ni otras fuentes que sustenten esa relación.",
  ["Compara lo que afirma el titular con la evidencia que ofrece la noticia."])
I("SOC-007", "SOC", "sistemico", "diagnostico", 0.0, "Para bajar el precio de la papa, un gobierno decide importar grandes cantidades. ¿Cuál es un efecto no deseado probable de esta medida?",
  ["Que aumente el precio de la papa en las tiendas.", "Que disminuyan los ingresos de los cultivadores locales.", "Que se reduzca el consumo de papa.", "Que desaparezcan los supermercados."], "B",
  "Con más papa en el mercado baja el precio, lo que beneficia a los consumidores pero reduce los ingresos de quienes la cultivan en el país.",
  ["Piensa en quién gana y quién pierde cuando el precio baja."])
I("SOC-008", "SOC", "sistemico", "diagnostico", 1.0, "Un municipio prohíbe que las motos circulen dos días a la semana para reducir la contaminación. ¿Cuál situación mostraría que la medida no cumple su propósito?",
  ["Que algunos motociclistas protesten.", "Que la calidad del aire no cambie porque la gente usa esos días otros vehículos igual de contaminantes.", "Que haya menos ruido en el centro.", "Que aumenten las ventas de cascos."], "B",
  "El propósito es reducir la contaminación. Si las personas sustituyen la moto por otro vehículo contaminante, el aire sigue igual y la medida falla.",
  ["Recuerda cuál era el objetivo de la medida.", "Una medida fracasa cuando no cambia aquello que quería cambiar."])
I("SOC-009", "SOC", "pensamiento_social", "practica", -0.6, "¿Cuál de las siguientes es una función de los concejos municipales?",
  ["Juzgar a quienes cometen delitos.", "Aprobar el presupuesto y el plan de desarrollo del municipio.", "Nombrar al alcalde.", "Comandar la Policía Nacional."], "B",
  "El concejo es la corporación que aprueba, mediante acuerdos, el presupuesto y el plan de desarrollo municipal. El alcalde se elige por voto popular.",
  ["Los concejales debaten y votan acuerdos."])
I("SOC-010", "SOC", "pensamiento_social", "practica", 0.4, "En Colombia el voto es secreto. Esta característica busca, principalmente,",
  ["que los votos se cuenten más rápido.", "proteger al votante de presiones o represalias por su decisión.", "evitar que voten los menores de edad.", "que solo voten quienes conocen a los candidatos."], "B",
  "Si nadie puede saber por quién votó una persona, es más difícil presionarla, comprarla o castigarla por su decisión.",
  ["¿Qué podría pasar si todos supieran por quién vota cada persona?"])
I("SOC-011", "SOC", "perspectivas", "practica", -0.2, "Un historiador describe la colonización antioqueña del siglo XIX como una 'gesta de progreso'. Otro señala que desplazó a comunidades indígenas que habitaban esas tierras. La diferencia entre ambas interpretaciones se explica porque",
  ["uno de los dos inventa los hechos.", "cada uno centra su atención en actores y consecuencias distintas del mismo proceso.", "hablan de épocas diferentes.", "solo uno de ellos es historiador."], "B",
  "Ambos estudian el mismo proceso, pero uno mira a los colonos y sus logros y el otro a quienes fueron desplazados. El punto de vista cambia la valoración.",
  ["¿A quiénes tiene en cuenta cada historiador?"])
I("SOC-012", "SOC", "perspectivas", "practica", 0.7, "En una negociación salarial, el sindicato cita el aumento del costo de vida y la empresa cita la caída de sus ventas. ¿Qué tienen en común ambos argumentos?",
  ["Los dos buscan cerrar la empresa.", "Los dos se apoyan en datos económicos para defender su propio interés.", "Los dos proponen el mismo aumento.", "Ninguno tiene relación con el salario."], "B",
  "Cada parte selecciona el dato económico que favorece su posición: uno para pedir más aumento, la otra para ofrecer menos.",
  ["Fíjate en qué tipo de razones da cada parte."])
I("SOC-013", "SOC", "sistemico", "practica", -0.4, "Una comunidad tala el bosque de la parte alta de una montaña para ampliar sus cultivos. A mediano plazo, ¿qué consecuencia es más probable para quienes viven en la parte baja?",
  ["Mayor riesgo de avalanchas y menos agua en verano.", "Mejor calidad del aire.", "Aumento del turismo.", "Suelos más fértiles en la parte baja."], "A",
  "El bosque retiene el suelo y regula el agua. Sin él aumentan los deslizamientos en invierno y disminuye el caudal en verano.",
  ["Piensa qué función cumple el bosque con el agua y con el suelo."])
I("SOC-014", "SOC", "sistemico", "practica", 0.6, "Un colegio decide expulsar de inmediato a cualquier estudiante que participe en una pelea. Desde un enfoque de derechos, una crítica válida a esta medida es que",
  ["las peleas no son un problema escolar.", "no garantiza el debido proceso ni una sanción proporcional, y afecta el derecho a la educación.", "los estudiantes deben resolver todo sin normas.", "las sanciones deberían ser solo económicas."], "B",
  "Toda sanción debe respetar el debido proceso y ser proporcional a la falta. Expulsar automáticamente pone en riesgo el derecho a la educación.",
  ["Piensa qué derechos tiene el estudiante sancionado."])
I("SOC-015", "SOC", "pensamiento_social", "simulacro", 0.0, "¿Qué mecanismo de participación permite a los ciudadanos decidir, mediante votación, si un alcalde continúa en su cargo?",
  ["El cabildo abierto.", "La revocatoria del mandato.", "La consulta previa.", "La iniciativa legislativa."], "B",
  "La revocatoria del mandato permite a los ciudadanos dar por terminado el mandato de alcaldes y gobernadores mediante el voto.",
  ["El nombre del mecanismo describe lo que hace."])
I("SOC-016", "SOC", "perspectivas", "simulacro", 0.3, "¿Cuál de las siguientes sería una fuente primaria para estudiar la vida cotidiana en un pueblo colombiano en 1900?",
  ["Un libro de texto escolar publicado este año.", "Cartas escritas por habitantes del pueblo en esa época.", "Un documental reciente sobre el siglo XX.", "Un artículo de enciclopedia en internet."], "B",
  "Una fuente primaria es producida por quienes vivieron la época. Las cartas son testimonio directo; las demás opciones son interpretaciones posteriores.",
  ["Primaria significa producida en el momento de los hechos."])
I("SOC-017", "SOC", "sistemico", "simulacro", 0.8, "Para reducir accidentes, un municipio instala reductores de velocidad frente a un colegio. Los conductores empiezan a desviarse por una calle residencial estrecha. Esta situación muestra que",
  ["los reductores nunca funcionan.", "una solución puede trasladar el problema a otro lugar si no se evalúan sus efectos en conjunto.", "los conductores no conocen las normas.", "el colegio debe cambiar de sede."], "B",
  "La medida resolvió el riesgo frente al colegio, pero creó uno nuevo en otra calle. Las decisiones deben evaluarse por sus efectos en todo el sistema.",
  ["Compara el efecto esperado con el efecto que realmente apareció."])

# =============================== CIENCIAS NATURALES ===============================
NT1 = ("Un grupo de estudiantes quiere saber si la cantidad de luz afecta el crecimiento de las plantas de fríjol. Siembran tres "
       "grupos de plantas iguales, con la misma tierra y la misma cantidad de agua, y les dan 2, 6 y 10 horas de luz al día.")
NT2 = "Azúcar que se disuelve en 100 mL de agua según la temperatura: a 20 °C, 204 g; a 40 °C, 238 g; a 60 °C, 287 g; a 80 °C, 362 g."
NT3 = "pH medido en cuatro muestras: jugo de limón, 2; agua lluvia, 5,6; agua pura, 7; agua con jabón, 10."
I("NAT-001", "NAT", "uso", "diagnostico", -1.2, "¿Cuál organelo es el principal responsable de producir la energía (ATP) que utiliza la célula?",
  ["El ribosoma.", "La mitocondria.", "El núcleo.", "El aparato de Golgi."], "B",
  "En la mitocondria ocurre la respiración celular, proceso en el que se produce la mayor parte del ATP.",
  ["Es el organelo donde ocurre la respiración celular."], componente="Biológico")
I("NAT-002", "NAT", "uso", "diagnostico", 0.0, "Al disolver sal en agua se obtiene una mezcla en la que no se distinguen sus componentes a simple vista. Esta mezcla es",
  ["heterogénea.", "homogénea.", "un elemento.", "un compuesto nuevo."], "B",
  "Es una solución: mezcla homogénea, de aspecto uniforme. No se forma una sustancia nueva, porque la sal se recupera al evaporar el agua.",
  ["¿Se ve igual en todas sus partes?", "Piensa si la sal dejó de ser sal."], componente="Químico")
I("NAT-003", "NAT", "explicacion", "diagnostico", -0.5, "Un ciclista deja de pedalear en una vía plana y la bicicleta termina deteniéndose. Esto ocurre porque",
  ["se le acaba la fuerza que llevaba guardada.", "la fricción y la resistencia del aire actúan en contra del movimiento.", "la gravedad la empuja hacia atrás.", "los objetos en movimiento siempre se detienen solos."], "B",
  "Las fuerzas de fricción y la resistencia del aire se oponen al movimiento y reducen la velocidad hasta detener la bicicleta.",
  ["Pregúntate qué fuerzas actúan sobre la bicicleta cuando nadie pedalea."], componente="Físico")
I("NAT-004", "NAT", "explicacion", "diagnostico", 0.6, "Tras varios años de fumigar con el mismo insecticida, un agricultor nota que ya no controla la plaga. La mejor explicación es que",
  ["los insectos decidieron volverse resistentes.", "los pocos insectos resistentes sobrevivieron y se reprodujeron, y ahora son mayoría.", "el insecticida alimenta a los insectos.", "todos los insectos se acostumbraron poco a poco durante su vida."], "B",
  "Es selección natural: el insecticida elimina a los sensibles; los resistentes sobreviven, dejan descendencia y su proporción aumenta en cada generación.",
  ["Piensa en lo que pasa con los insectos que sobreviven a cada fumigación.", "La resistencia no se 'decide'; se hereda."], componente="Biológico")
I("NAT-005", "NAT", "explicacion", "diagnostico", 1.0, "Una puntilla de hierro dejada a la intemperie se cubre de óxido y su masa aumenta ligeramente. El aumento de masa se explica porque",
  ["el hierro absorbe calor del sol.", "el hierro se combina con oxígeno del aire, y el óxido contiene los átomos de ambos.", "el hierro se transforma en un metal más pesado.", "la puntilla se dilata con la humedad."], "B",
  "La oxidación es una reacción química: los átomos de oxígeno del aire quedan unidos al hierro, de modo que el óxido pesa más que el hierro inicial.",
  ["La masa no aparece de la nada: ¿de dónde vienen los átomos nuevos?"], componente="Químico")
I("NAT-006", "NAT", "indagacion", "diagnostico", -0.6, "¿Cuál es la variable que los estudiantes modifican a propósito en su experimento?",
  ["El tipo de tierra.", "La cantidad de agua.", "Las horas de luz que recibe cada grupo.", "La altura de las plantas."], "C",
  "Lo único que cambia entre los grupos son las horas de luz: es la variable independiente. La altura es lo que se mide.",
  ["¿Qué es distinto entre los tres grupos de plantas?"], ctx=NT1)
I("NAT-007", "NAT", "indagacion", "diagnostico", 0.2, "¿Por qué los estudiantes usan la misma tierra y la misma cantidad de agua en los tres grupos?",
  ["Para gastar menos materiales.", "Para que las diferencias de crecimiento puedan atribuirse solo a la luz.", "Porque las plantas de fríjol no necesitan agua.", "Para que todas las plantas crezcan igual."], "B",
  "Mantener iguales las demás condiciones (control de variables) permite concluir que cualquier diferencia se debe a la variable que se cambió.",
  ["Si también cambiaran el agua, ¿podrían saber qué causó la diferencia?"], ctx=NT1)
I("NAT-008", "NAT", "indagacion", "diagnostico", 1.0, "¿Cuál conclusión está sustentada por los datos?",
  ["La cantidad de azúcar disuelta se duplica cada 20 °C.", "Al aumentar la temperatura del agua, aumenta la cantidad de azúcar que se disuelve.", "A 100 °C se disuelven exactamente 400 g de azúcar.", "La temperatura no influye en la cantidad de azúcar que se disuelve."], "B",
  "Los cuatro datos muestran que a mayor temperatura se disuelve más azúcar. No se duplica (204 a 238 no es el doble) y no hay dato para 100 °C.",
  ["Verifica cada opción contra los números.", "Una conclusión no puede afirmar algo que los datos no muestran."], ctx=NT2)
I("NAT-009", "NAT", "uso", "practica", -0.8, "¿Cuál es la unidad de fuerza en el Sistema Internacional de Unidades?",
  ["El julio.", "El newton.", "El vatio.", "El kilogramo."], "B",
  "La fuerza se mide en newtons (N). El julio mide energía, el vatio potencia y el kilogramo masa.",
  ["Lleva el apellido del científico que formuló las leyes del movimiento."], componente="Físico")
I("NAT-010", "NAT", "uso", "practica", 0.4, "En la cadena alimentaria pasto → saltamontes → rana → culebra, la rana es un",
  ["productor.", "consumidor primario.", "consumidor secundario.", "descomponedor."], "C",
  "El pasto es productor; el saltamontes, que come pasto, es consumidor primario; la rana, que come saltamontes, es consumidor secundario.",
  ["Cuenta los eslabones desde el productor."], componente="Biológico")
I("NAT-011", "NAT", "explicacion", "practica", 0.0, "Al destapar una olla con agua hirviendo, la tapa tiene gotas de agua por dentro. Estas gotas se forman porque",
  ["el agua salta desde la olla hasta la tapa.", "el vapor de agua se enfría al tocar la tapa y se condensa.", "la tapa suda por el calor.", "el aire de la cocina es húmedo."], "B",
  "El vapor que sube pierde calor al tocar la tapa, que está más fría, y pasa de gas a líquido: condensación.",
  ["¿En qué estado sale el agua de la olla y en qué estado está en la tapa?"], componente="Físico")
I("NAT-012", "NAT", "explicacion", "practica", 0.8, "Tomar antibióticos sin fórmula médica o suspenderlos antes de tiempo favorece la aparición de bacterias resistentes porque",
  ["los antibióticos crean bacterias nuevas.", "sobreviven las bacterias menos sensibles y luego se multiplican.", "el cuerpo deja de producir defensas.", "las bacterias aprenden a esconderse en el estómago."], "B",
  "Un tratamiento incompleto elimina primero a las bacterias más sensibles; las más resistentes sobreviven y se reproducen.",
  ["Relaciónalo con lo que pasa cuando un tratamiento no elimina a todas las bacterias."], componente="CTS")
I("NAT-013", "NAT", "indagacion", "practica", 0.0, "Para comprobar si un abono mejora la producción de tomate, lo más adecuado es",
  ["aplicar el abono a todas las plantas y esperar.", "comparar plantas con abono y sin abono cultivadas en las mismas condiciones.", "preguntar a los vecinos qué abono usan.", "sembrar el tomate en una época distinta."], "B",
  "Se necesita un grupo de comparación (sin abono) en iguales condiciones para saber si la diferencia se debe al abono.",
  ["¿Contra qué vas a comparar la producción?"])
I("NAT-014", "NAT", "indagacion", "practica", 0.7, "De acuerdo con los datos, ¿cuál afirmación es correcta?",
  ["El agua lluvia es una sustancia básica.", "El jugo de limón es la muestra más ácida.", "El agua con jabón es ácida.", "El agua pura es más ácida que el agua lluvia."], "B",
  "En la escala de pH, valores menores que 7 son ácidos y entre más bajo el valor, más ácida la sustancia. El limón (pH 2) es el más ácido.",
  ["Recuerda: pH 7 es neutro; por debajo, ácido; por encima, básico."], ctx=NT3)
I("NAT-015", "NAT", "uso", "simulacro", 0.2, "En la ecuación 2H₂ + O₂ → 2H₂O, ¿cuántos átomos de hidrógeno hay en los productos?",
  ["2", "4", "6", "8"], "B",
  "Hay 2 moléculas de agua y cada una tiene 2 átomos de hidrógeno: 2 × 2 = 4.",
  ["Multiplica el coeficiente por el subíndice del hidrógeno."], componente="Químico")
I("NAT-016", "NAT", "explicacion", "simulacro", 0.5, "Dos esferas del mismo tamaño, una de hierro y otra de icopor, se sueltan en un tanque con agua: una se hunde y la otra flota. La diferencia se explica por",
  ["el color de cada esfera.", "la densidad de cada material comparada con la del agua.", "la forma de las esferas.", "la cantidad de agua que hay en el tanque."], "B",
  "Con igual volumen, el hierro tiene mucha más masa: es más denso que el agua y se hunde. El icopor es menos denso que el agua y flota.",
  ["Tienen el mismo tamaño: ¿qué propiedad cambia?"], componente="Físico")
I("NAT-017", "NAT", "indagacion", "simulacro", 0.9, "Un estudiante mide tres veces el tiempo de caída de un objeto y obtiene 1,9 s, 2,1 s y 2,0 s. Reporta 2,0 s. ¿Por qué es buena práctica repetir la medición?",
  ["Porque así el objeto cae más rápido.", "Porque el promedio de varias medidas reduce el efecto de los errores aleatorios.", "Porque el cronómetro se daña con una sola medida.", "Porque tres medidas siempre dan el mismo valor."], "B",
  "Cada medición tiene pequeños errores al azar; al promediar varias, esos errores tienden a compensarse y el resultado es más confiable.",
  ["Fíjate en que las tres medidas no son idénticas."])

# =============================== INGLÉS ===============================
ET1 = ("Maria lives in a small town near the mountains. Every morning she walks two kilometres to school with her brother. "
       "After school, she helps her mother in the family shop, and in the evening she does her homework.")
ET2 = ("Tom wanted to buy a new phone, so he worked on his uncle's farm every weekend for three months. When he finally had "
       "the money, he saw that his little sister needed glasses. He put the money on the kitchen table and said nothing.")
ET3 = ("The town library is open from Monday to Friday, 8 a.m. to 5 p.m. Students can borrow up to three books for two weeks. "
       "Books that are returned late cost 500 pesos per day.")
ET4 = ("Last year, a group of students started a small garden behind their school. At first, nothing grew because the soil was "
       "too dry. They asked an old farmer for advice, and he showed them how to collect rainwater. Now the garden gives "
       "vegetables for the school kitchen.")
I("ING-001", "ING", "lexico_pragmatico", "diagnostico", -1.5, "Which word matches the description? 'You wear it on your head when it is sunny.'",
  ["shoes", "hat", "belt", "gloves"], "B", "A 'hat' (sombrero o gorra) se usa en la cabeza. 'Head' significa cabeza.",
  ["Fíjate en la palabra 'head'."])
I("ING-002", "ING", "lexico_pragmatico", "diagnostico", -0.8, "Where can you see this notice? 'PLEASE TURN OFF YOUR PHONE DURING THE FILM.'",
  ["at a bus stop", "in a cinema", "in a supermarket", "on a farm"], "B", "'Film' es película: el aviso se encuentra en un cine (cinema).",
  ["La palabra clave es 'film'."])
I("ING-003", "ING", "lexico_pragmatico", "diagnostico", -0.2, "Complete the conversation. A: 'Would you like some coffee?' B: '___'",
  ["Yes, I do it.", "Yes, please.", "I like.", "Here it is yesterday."], "B", "A un ofrecimiento con 'Would you like...?' se responde 'Yes, please' o 'No, thanks'.",
  ["Es un ofrecimiento amable: ¿cómo se acepta con cortesía?"])
I("ING-004", "ING", "gramatica", "diagnostico", -0.9, "My sister ___ to school by bus every day.",
  ["go", "goes", "going", "gone"], "B", "Presente simple con tercera persona (she): el verbo lleva -es. 'Every day' indica rutina.",
  ["El sujeto es 'my sister' (she).", "'Every day' indica una rutina: presente simple."])
I("ING-005", "ING", "gramatica", "diagnostico", 0.0, "We ___ football when it started to rain.",
  ["play", "are playing", "were playing", "have played"], "C", "Una acción en progreso en el pasado (were playing) es interrumpida por otra (started): pasado continuo.",
  ["'Started' está en pasado: la otra acción también ocurre en el pasado.", "Era una acción que estaba en curso."])
I("ING-006", "ING", "gramatica", "diagnostico", 0.9, "If I ___ more time, I would learn to play the guitar.",
  ["have", "had", "will have", "would have"], "B", "Segundo condicional (situación hipotética): if + pasado simple, would + verbo.",
  ["Mira la segunda parte: 'would learn'.", "Es una situación imaginaria en el presente."])
I("ING-007", "ING", "lectura", "diagnostico", -0.4, "How does Maria get to school?",
  ["By bus.", "On foot.", "By bike.", "By motorbike."], "B", "El texto dice 'she walks two kilometres to school': va caminando (on foot).",
  ["Busca el verbo que describe cómo llega al colegio."], ctx=ET1)
I("ING-008", "ING", "lectura", "diagnostico", 0.7, "What can we infer about Tom?",
  ["He lost his money on the farm.", "He decided to use his money to help his sister.", "He bought the phone and the glasses.", "He was angry with his uncle."], "B",
  "Dejó el dinero en la mesa al ver que su hermana necesitaba gafas: se infiere que renunció al celular para ayudarla.",
  ["¿Qué vio Tom justo antes de dejar el dinero en la mesa?"], ctx=ET2)
I("ING-009", "ING", "lexico_pragmatico", "practica", -1.0, "Which word matches the description? 'A person who repairs cars.'",
  ["nurse", "mechanic", "farmer", "pilot"], "B", "'Mechanic' es mecánico: la persona que repara carros ('repairs cars').",
  ["'Repairs' significa repara."])
I("ING-010", "ING", "lexico_pragmatico", "practica", -0.3, "What does this notice mean? 'CLOSED ON SUNDAYS'",
  ["You can shop here every day.", "You cannot shop here on Sundays.", "The shop opens only on Sundays.", "The shop is closed all week."], "B",
  "'Closed' es cerrado: los domingos no hay atención.", ["'Closed' es lo contrario de 'open'."])
I("ING-011", "ING", "lexico_pragmatico", "practica", 0.3, "Complete the conversation. A: 'I'm sorry I'm late.' B: '___'",
  ["You're welcome.", "That's all right.", "Me too.", "Yes, I am."], "B", "Ante una disculpa se responde 'That's all right' (no hay problema). 'You're welcome' responde a 'thank you'.",
  ["La persona A se está disculpando."])
I("ING-012", "ING", "gramatica", "practica", -0.5, "There aren't ___ apples in the kitchen.",
  ["some", "any", "a", "much"], "B", "En oraciones negativas con sustantivos contables en plural se usa 'any'.",
  ["La oración es negativa (aren't)."])
I("ING-013", "ING", "gramatica", "practica", 0.5, "She has lived in Ocaña ___ 2015.",
  ["for", "since", "ago", "during"], "B", "Con presente perfecto, 'since' indica el momento en que empezó la acción (2015); 'for' indica duración (for ten years).",
  ["2015 es un punto de inicio, no una duración."])
I("ING-014", "ING", "lectura", "practica", 0.0, "How long can a student keep a book?",
  ["Three days.", "Two weeks.", "Five days.", "One month."], "B", "El texto dice 'for two weeks'. 'Three' es el número de libros, no el tiempo.",
  ["Distingue cuántos libros de cuánto tiempo."], ctx=ET3)
I("ING-015", "ING", "lectura", "practica", 0.9, "A student returns a book four days late. What happens?",
  ["The student pays 500 pesos.", "The student pays 2,000 pesos.", "The student cannot borrow books again.", "Nothing happens."], "B",
  "Son 500 pesos por día de retraso: 4 × 500 = 2.000 pesos.", ["El cobro es 'per day'.", "Multiplica por los días de retraso."], ctx=ET3)
I("ING-016", "ING", "lexico_pragmatico", "simulacro", 0.0, "Which word matches the description? 'You use them to cut paper.'",
  ["glue", "scissors", "ruler", "eraser"], "B", "'Scissors' son tijeras; 'cut' es cortar.", ["'Cut' significa cortar."])
I("ING-017", "ING", "gramatica", "simulacro", 0.3, "This is the ___ book I have ever read.",
  ["good", "better", "best", "most good"], "C", "Superlativo de 'good': the best. Se usa con 'the' y con 'I have ever...'.",
  ["Hay un 'the' antes del espacio: se necesita el superlativo."])
I("ING-018", "ING", "lectura", "simulacro", 0.8, "Why did the garden improve?",
  ["Because the students bought new soil.", "Because the students learned how to collect rainwater.", "Because it rained every day.", "Because the farmer worked in the garden."], "B",
  "El problema era la tierra seca; el agricultor les enseñó a recoger agua lluvia y desde entonces la huerta produce.",
  ["¿Cuál era el problema al comienzo y qué cambió?"], ctx=ET4)
