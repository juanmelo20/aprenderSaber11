"""Más preguntas ORIGINALES de Lectura Crítica (ocho textos nuevos, cinco preguntas por texto).
Entran en borrador, igual que el resto del banco semilla."""
from __future__ import annotations

from .bank_seed import I

P1 = ("Los páramos son ecosistemas de alta montaña que se encuentran por encima del bosque andino. Su vegetación, en la que sobresalen los "
      "frailejones, actúa como una esponja: retiene el agua de la lluvia y de la niebla y la libera poco a poco hacia quebradas y ríos. Por eso, "
      "buena parte del agua que llega a los acueductos de muchas ciudades colombianas nace en ellos. Los frailejones crecen muy despacio, cerca "
      "de un centímetro por año, de modo que una planta de un metro puede tener un siglo. Cuando la ganadería, los cultivos o la minería dañan "
      "el suelo del páramo, este pierde su capacidad de almacenar agua, y recuperarlo puede tardar varias generaciones.")
I("LEC-101", "LEC", "locales", "practica", -1.0, "Según el texto, ¿qué función cumple la vegetación del páramo?",
  ["Impide que la niebla llegue a las ciudades.", "Retiene el agua y la entrega lentamente a quebradas y ríos.", "Protege a los frailejones de la ganadería.", "Acelera el crecimiento del bosque andino."], "B",
  "El texto la compara con una esponja: retiene el agua de la lluvia y la niebla y la libera poco a poco.", ["Busca la comparación que usa el texto para explicar qué hace la vegetación."], ctx=P1)
I("LEC-102", "LEC", "locales", "diagnostico", -0.4, "La afirmación de que 'una planta de un metro puede tener un siglo' se apoya en que los frailejones",
  ["viven por encima del bosque andino.", "almacenan agua durante muchos años.", "crecen cerca de un centímetro por año.", "tardan varias generaciones en recuperarse."], "C",
  "Un metro son cien centímetros; a un centímetro por año, la planta tardaría unos cien años.", ["La expresión 'de modo que' une esta afirmación con el dato anterior."], ctx=P1)
I("LEC-103", "LEC", "global", "practica", 0.0, "¿Qué función cumple la última oración dentro del texto?",
  ["Resume las características de los frailejones.", "Presenta un ejemplo de cómo el páramo almacena agua.", "Advierte sobre una consecuencia grave de dañar el páramo.", "Contradice lo que se dijo sobre los acueductos."], "C",
  "Después de explicar por qué el páramo es valioso, el texto cierra mostrando qué se pierde si se daña y cuánto tarda en recuperarse.", ["Fíjate en que las oraciones anteriores describen y la última habla de un riesgo."], ctx=P1)
I("LEC-104", "LEC", "global", "practica", -0.2, "¿Cuál opción expresa mejor la idea principal del texto?",
  ["Los frailejones son las plantas más antiguas de Colombia.", "Los páramos regulan el agua de la que dependen muchas poblaciones y son muy lentos de recuperar.", "La ganadería y la minería deben prohibirse en todo el país.", "El agua de los acueductos proviene únicamente de la niebla."], "B",
  "El texto une dos ideas: el páramo provee y regula agua, y su daño es muy difícil de revertir. Las demás opciones exageran o toman solo un detalle.", ["Una idea principal recoge todo el texto, no un solo dato.", "Descarta las opciones con palabras absolutas como 'únicamente' o 'todo'."], ctx=P1)
I("LEC-105", "LEC", "critica", "practica", 0.7, "Un concejal propone permitir ganadería en el páramo porque 'el pasto vuelve a crecer en un año'. Con base en el texto, la objeción más sólida es que",
  ["el pasto no crece en clima frío.", "el daño no es al pasto sino al suelo que almacena el agua, y este tarda generaciones en recuperarse.", "los frailejones son plantas protegidas por la ley.", "las ciudades no necesitan el agua del páramo."], "B",
  "El argumento del concejal habla del pasto; el texto dice que lo que se pierde es la capacidad del suelo de almacenar agua, y que recuperarla toma generaciones.", ["¿De qué recuperación habla el concejal y de cuál habla el texto?", "La mejor objeción usa información que sí está en el texto."], ctx=P1)

P2 = ("Cada cierto tiempo vuelve la propuesta de eliminar las tareas escolares. Sus defensores sostienen que los estudiantes llegan agotados a casa "
      "y que las tareas aumentan la desigualdad, pues no todos cuentan con un lugar tranquilo, conexión a internet o un adulto que los oriente. "
      "Tienen razón en el diagnóstico, pero no en el remedio. Una tarea breve y bien pensada permite practicar lo visto y descubrir qué no se "
      "entendió antes de que sea tarde. El problema no es la tarea, sino la tarea larga, repetitiva y sin revisión. En vez de prohibirlas, "
      "convendría limitarlas, hacerlas más cortas y abrir espacios en el colegio para quienes no pueden hacerlas en casa.")
I("LEC-106", "LEC", "locales", "practica", -0.9, "Según quienes proponen eliminar las tareas, estas aumentan la desigualdad porque",
  ["los docentes no las revisan.", "no todos los estudiantes tienen en casa las condiciones para hacerlas.", "son largas y repetitivas.", "los colegios no tienen espacios de estudio."], "B",
  "El texto menciona que no todos cuentan con un lugar tranquilo, internet o un adulto que los oriente.", ["Busca la palabra 'desigualdad' y lee lo que sigue después de 'pues'."], ctx=P2)
I("LEC-107", "LEC", "global", "diagnostico", 0.2, "Con la frase 'Tienen razón en el diagnóstico, pero no en el remedio', el autor quiere decir que",
  ["el problema que señalan existe, pero la solución que proponen no es la adecuada.", "los defensores de la propuesta no entienden el problema.", "las tareas son una enfermedad de la escuela.", "el problema no existe y la solución es innecesaria."], "A",
  "'Diagnóstico' se refiere al problema identificado (cansancio y desigualdad); 'remedio', a la solución (eliminar las tareas). El autor acepta lo primero y rechaza lo segundo.", ["¿Qué sería el 'diagnóstico' y qué sería el 'remedio' en esta discusión?"], ctx=P2)
I("LEC-108", "LEC", "global", "practica", 0.0, "La posición que defiende el autor es que las tareas",
  ["deben eliminarse porque agotan a los estudiantes.", "deben mantenerse tal como están.", "deben conservarse, pero más cortas, revisadas y con apoyo para quien no pueda hacerlas en casa.", "solo deben dejarse a quienes tienen internet."], "C",
  "La última oración resume su propuesta: limitarlas, acortarlas y abrir espacios en el colegio.", ["La postura del autor suele quedar clara al final del texto."], ctx=P2)
I("LEC-109", "LEC", "critica", "practica", 0.6, "¿Qué estrategia usa el autor para argumentar?",
  ["Ridiculiza a quienes piensan distinto.", "Reconoce parte de la razón de sus contradictores y luego muestra por qué su conclusión no se sigue.", "Cita estudios científicos con cifras.", "Narra una experiencia personal como prueba."], "B",
  "Primero concede ('tienen razón en el diagnóstico') y después refuta la solución. No cita estudios ni cuenta experiencias propias.", ["Observa qué hace con los argumentos del otro bando: ¿los ignora, los acepta en parte?"], ctx=P2)
I("LEC-110", "LEC", "critica", "practica", 0.9, "¿Cuál de los siguientes datos fortalecería más la posición del autor?",
  ["Una encuesta en la que la mayoría de estudiantes dice que no le gustan las tareas.", "Un estudio que muestre que las tareas breves y revisadas mejoran el aprendizaje, y las largas no.", "Un informe según el cual muchos hogares rurales no tienen internet.", "El testimonio de un docente que nunca deja tareas."], "B",
  "El autor distingue entre tareas breves y bien pensadas y tareas largas sin revisión: un estudio que confirme esa diferencia apoya directamente su tesis.", ["Recuerda cuál es la distinción central del autor.", "Un dato fortalece una postura si confirma justamente lo que esa postura afirma."], ctx=P2)

P3 = ("El profesor nuevo llegó a la vereda un lunes de lluvia, con una maleta amarrada con cabuya y unos zapatos que no eran para ese barro. "
      "Los niños lo miraron desde la puerta de la escuela sin saludar. Venían de despedir a tres maestros en dos años y habían aprendido a no "
      "encariñarse. Él no dijo nada sobre eso. Barrió el salón, destapó la gotera del rincón y escribió en el tablero una sola pregunta: «¿Qué "
      "saben hacer ustedes que yo no sepa?». Al final de la mañana tenía una lista de veintidós cosas, desde ordeñar hasta predecir la lluvia "
      "por el vuelo de las golondrinas. —Entonces empecemos por ahí —dijo—. Ustedes me enseñan primero.")
I("LEC-111", "LEC", "locales", "practica", -1.1, "Los niños no saludan al profesor nuevo porque",
  ["no les gusta la lluvia.", "han visto irse a varios maestros y prefieren no encariñarse.", "el profesor no los saludó primero.", "les da risa su maleta."], "B",
  "El texto lo dice: venían de despedir a tres maestros en dos años y habían aprendido a no encariñarse.", ["Busca la oración que explica lo que los niños 'habían aprendido'."], ctx=P3)
I("LEC-112", "LEC", "locales", "diagnostico", -0.3, "El detalle de 'unos zapatos que no eran para ese barro' sugiere que el profesor",
  ["es una persona descuidada.", "viene de otro lugar y no conoce las condiciones de la vereda.", "no piensa quedarse mucho tiempo.", "tiene mucho dinero."], "B",
  "El calzado inadecuado muestra que no estaba preparado para el terreno: es alguien de afuera. El texto no dice nada de dinero ni de sus planes.", ["¿Qué te dice ese detalle sobre cuánto conoce el lugar?", "Descarta lo que el texto no permite afirmar."], ctx=P3)
I("LEC-113", "LEC", "global", "practica", 0.1, "¿Qué busca el profesor al escribir la pregunta en el tablero?",
  ["Evaluar qué tan atrasados están los niños.", "Mostrar que él sabe más que ellos.", "Reconocer lo que los niños saben y ganarse su confianza.", "Ocupar la mañana mientras deja de llover."], "C",
  "Les pide que le enseñen primero: valora sus saberes y cambia la relación habitual entre maestro y estudiantes.", ["Relaciona la pregunta con lo último que dice el profesor."], ctx=P3)
I("LEC-114", "LEC", "global", "practica", 0.4, "El narrador de este relato",
  ["es uno de los niños de la escuela.", "es el profesor, que cuenta su llegada.", "está fuera de la historia y conoce lo que sienten los niños.", "solo cuenta lo que se puede ver, sin conocer lo que piensan los personajes."], "C",
  "Narra en tercera persona ('llegó', 'lo miraron') y sabe que los niños 'habían aprendido a no encariñarse', algo que no se ve desde afuera.", ["¿En qué persona están los verbos?", "¿El narrador sabe algo que solo los personajes podrían saber?"], ctx=P3)
I("LEC-115", "LEC", "critica", "practica", 0.6, "La actitud del profesor representa una idea de la educación según la cual",
  ["el maestro es el único que posee conocimiento valioso.", "aprender empieza por reconocer lo que la comunidad ya sabe.", "los saberes del campo deben reemplazar las materias escolares.", "los niños rurales no necesitan ir a la escuela."], "B",
  "Dice 'empecemos por ahí': usa lo que saben como punto de partida, no como reemplazo de la enseñanza.", ["'Empecemos por ahí' indica un comienzo, no un final.", "Cuidado con las opciones que llevan la idea al extremo."], ctx=P3)

P4 = ("RECIBO DEL ACUEDUCTO VEREDAL. Periodo: marzo\nConsumo del mes: 18 m³\nCargo fijo: $6.000\nConsumo básico (hasta 16 m³): $900 por m³\n"
      "Consumo adicional (más de 16 m³): $1.500 por m³\nFecha límite de pago: 20 de abril. Después de esa fecha se cobra un recargo de $2.000.\n"
      "El servicio se suspende con dos recibos vencidos.")
I("LEC-116", "LEC", "locales", "practica", -1.0, "Según el recibo, ¿qué ocurre si el usuario paga el 25 de abril?",
  ["Le suspenden el servicio.", "Debe pagar un recargo de $2.000.", "Le cobran la tarifa adicional por todo el consumo.", "No ocurre nada, porque el periodo es marzo."], "B",
  "La fecha límite es el 20 de abril; después se cobra un recargo de $2.000. La suspensión solo ocurre con dos recibos vencidos.", ["Compara la fecha de pago con la fecha límite."], ctx=P4)
I("LEC-117", "LEC", "locales", "diagnostico", 0.0, "¿Cuántos metros cúbicos de este recibo se cobran con la tarifa de consumo adicional?",
  ["2", "16", "18", "Ninguno"], "A",
  "El consumo fue de 18 m³. Los primeros 16 son básicos; los 2 restantes superan ese límite y se cobran a $1.500.", ["¿Hasta cuántos metros cúbicos llega el consumo básico?", "Resta ese límite del consumo del mes."], ctx=P4)
I("LEC-118", "LEC", "global", "practica", 0.3, "Que el metro cúbico adicional cueste más que el básico indica que la tarifa está diseñada para",
  ["castigar a quienes pagan tarde.", "que todos los usuarios paguen lo mismo.", "desincentivar el consumo alto de agua.", "cubrir el cargo fijo."], "C",
  "Quien pasa de 16 m³ paga más por cada metro adicional: es una forma de promover el ahorro. El pago tardío se castiga con el recargo, que es otra cosa.", ["¿Quién termina pagando más por metro cúbico: el que gasta poco o el que gasta mucho?"], ctx=P4)
I("LEC-119", "LEC", "critica", "practica", 0.5, "Un usuario que no ha pagado el recibo de marzo, pero tiene los anteriores al día, dice: 'Mañana me cortan el agua'. Según el recibo, su afirmación es",
  ["correcta, porque ya pasó la fecha límite.", "incorrecta, porque la suspensión ocurre con dos recibos vencidos.", "correcta, porque consumió más de 16 m³.", "incorrecta, porque el acueducto nunca suspende el servicio."], "B",
  "La última línea dice que el servicio se suspende con dos recibos vencidos; él solo tiene uno. Sí deberá pagar el recargo.", ["Lee la condición exacta para la suspensión.", "¿Cuántos recibos vencidos tiene este usuario?"], ctx=P4)
I("LEC-120", "LEC", "global", "practica", -0.3, "¿Cuál es el propósito principal de este texto?",
  ["Convencer a los usuarios de ahorrar agua.", "Informar cuánto se consumió, cómo se cobra y qué pasa si no se paga a tiempo.", "Explicar cómo funciona el acueducto de la vereda.", "Denunciar el aumento de las tarifas."], "B",
  "Un recibo informa: presenta el consumo, las tarifas, la fecha de pago y las consecuencias de no pagar.", ["Piensa en para qué recibe alguien este documento."], ctx=P4)

P5 = ("Solemos creer que una persona es libre cuando nadie le impide hacer lo que desea. Pero esa idea deja por fuera una pregunta incómoda: "
      "¿de dónde vienen nuestros deseos? Quien compra lo que la publicidad le repite, o piensa lo que piensa su grupo por miedo a quedarse solo, "
      "hace lo que quiere y, sin embargo, cuesta llamarlo libre. Tal vez la libertad no consista solo en la ausencia de obstáculos, sino también "
      "en la capacidad de examinar los propios deseos y preguntarse si uno los elegiría de nuevo. En ese sentido, la libertad no es un punto de "
      "partida sino una tarea.")
I("LEC-121", "LEC", "locales", "practica", -0.6, "Según la primera oración, la idea más común de libertad consiste en",
  ["examinar los propios deseos.", "que nadie le impida a uno hacer lo que desea.", "pensar lo mismo que el grupo.", "no desear nada."], "B",
  "El texto empieza así: 'una persona es libre cuando nadie le impide hacer lo que desea'. Las demás ideas aparecen después.", ["La pregunta se refiere solo a la primera oración."], ctx=P5)
I("LEC-122", "LEC", "global", "diagnostico", 0.5, "La pregunta '¿de dónde vienen nuestros deseos?' sirve en el texto para",
  ["confirmar la idea común de libertad.", "poner en duda la idea común de libertad.", "cambiar de tema hacia la publicidad.", "demostrar que nadie desea nada por sí mismo."], "B",
  "La pregunta abre la objeción: si los deseos pueden venir de afuera, hacer lo que uno desea no basta para ser libre.", ["Mira el conector que la introduce: 'Pero'.", "¿La pregunta apoya o cuestiona lo dicho en la primera oración?"], ctx=P5)
I("LEC-123", "LEC", "global", "practica", 0.7, "Al afirmar que 'la libertad no es un punto de partida sino una tarea', el autor sostiene que la libertad",
  ["se tiene desde el nacimiento y no puede perderse.", "es imposible de alcanzar.", "se construye con el esfuerzo de revisar lo que uno quiere.", "depende de que no existan leyes."], "C",
  "'Tarea' indica algo que se hace y se trabaja: examinar los propios deseos. No dice que sea imposible ni que venga dada.", ["Compara 'punto de partida' (algo que ya se tiene) con 'tarea' (algo por hacer)."], ctx=P5)
I("LEC-124", "LEC", "critica", "practica", 0.9, "¿Cuál situación ilustra mejor la idea de libertad que propone el autor?",
  ["Un joven compra los tenis que usan todos sus amigos para no sentirse excluido.", "Una joven se pregunta si quiere estudiar enfermería por decisión propia o por presión familiar, y decide después de pensarlo.", "Un señor hace siempre lo primero que se le antoja.", "Una persona vive sola en una isla, sin nadie que le prohíba nada."], "B",
  "El autor propone examinar los propios deseos y preguntarse si uno los elegiría de nuevo: es lo que hace la joven.", ["Busca el caso en que alguien revisa de dónde viene lo que quiere.", "La isla solo cumple con la 'ausencia de obstáculos'."], ctx=P5)
I("LEC-125", "LEC", "critica", "practica", 0.8, "El razonamiento del autor da por supuesto que",
  ["la publicidad debería prohibirse.", "los deseos de una persona pueden estar moldeados por otros sin que ella lo note.", "las personas nunca hacen lo que quieren.", "pertenecer a un grupo es siempre negativo."], "B",
  "Sus ejemplos (la publicidad, el miedo a quedarse solo) solo funcionan si se acepta que lo que deseamos puede venir de influencias externas.", ["Un supuesto es algo que el autor no demuestra pero necesita para que su argumento funcione."], ctx=P5)

P6 = ("Durante años se pensó que dormir era simplemente «apagar» el cerebro. Hoy se sabe que, mientras dormimos, el cerebro sigue activo: repasa "
      "lo aprendido durante el día y fortalece las conexiones entre neuronas que sostienen los recuerdos. Por eso, estudiar toda la noche antes de "
      "un examen suele dar peores resultados que estudiar menos y dormir bien. Los adolescentes necesitan entre ocho y diez horas de sueño, pero "
      "su reloj biológico tiende a retrasarse: les da sueño más tarde y les cuesta madrugar. Algunos colegios que retrasaron la hora de entrada "
      "han reportado menos ausencias y mejor atención en las primeras clases, aunque los resultados varían de un lugar a otro.")
I("LEC-126", "LEC", "locales", "practica", -1.0, "Según el texto, mientras dormimos el cerebro",
  ["se apaga para descansar.", "repasa lo aprendido y fortalece los recuerdos.", "retrasa el reloj biológico.", "deja de formar conexiones entre neuronas."], "B",
  "El texto corrige la idea de que el cerebro se 'apaga': sigue activo, repasa lo aprendido y fortalece conexiones.", ["Diferencia lo que 'se pensó' de lo que 'hoy se sabe'."], ctx=P6)
I("LEC-127", "LEC", "locales", "practica", -0.5, "¿Por qué a los adolescentes les cuesta madrugar, según el texto?",
  ["Porque estudian toda la noche.", "Porque necesitan menos horas de sueño que los adultos.", "Porque su reloj biológico se retrasa y les da sueño más tarde.", "Porque los colegios entran muy temprano."], "C",
  "El texto dice que su reloj biológico tiende a retrasarse: les da sueño más tarde y les cuesta madrugar.", ["Busca lo que viene después de los dos puntos en la oración sobre los adolescentes."], ctx=P6)
I("LEC-128", "LEC", "global", "diagnostico", 0.1, "En el texto, la expresión 'Por eso' introduce",
  ["una consecuencia de lo explicado sobre el sueño y la memoria.", "una idea contraria a la anterior.", "un ejemplo de reloj biológico.", "la opinión de los colegios."], "A",
  "Si el sueño fortalece los recuerdos, entonces trasnochar estudiando rinde menos: es una consecuencia de lo anterior.", ["¿Lo que viene después de 'Por eso' se desprende de lo que se dijo antes?"], ctx=P6)
I("LEC-129", "LEC", "critica", "practica", 0.6, "La aclaración final, 'aunque los resultados varían de un lugar a otro', cumple la función de",
  ["negar que entrar más tarde tenga algún efecto.", "matizar la afirmación para no presentarla como una regla que siempre se cumple.", "criticar a los colegios que cambiaron su horario.", "repetir la idea principal."], "B",
  "El autor informa resultados favorables, pero reconoce sus límites: no afirma que ocurra en todas partes.", ["'Aunque' introduce una reserva, no una negación total."], ctx=P6)
I("LEC-130", "LEC", "critica", "practica", 0.8, "¿Cuál de estas conclusiones NO está respaldada por el texto?",
  ["Dormir bien ayuda a recordar lo estudiado.", "Trasnochar antes de un examen suele ser mala estrategia.", "Está demostrado que todos los colegios mejorarán si entran más tarde.", "Los adolescentes tienden a tener sueño más tarde."], "C",
  "El texto habla de 'algunos colegios' y advierte que los resultados varían: no permite afirmar que todos mejorarán.", ["Compara cada opción con lo que el texto dice exactamente.", "Fíjate en palabras como 'todos' y 'demostrado'."], ctx=P6)

P7 = ("En la asamblea del municipio se discutió la pavimentación de la vía que atraviesa la reserva forestal. Doña Carmen, que vende quesos en "
      "el pueblo, pidió la obra: «Cuando llueve, el viaje de una hora se vuelve de cuatro y la leche se daña». Un guardabosques advirtió que una "
      "vía rápida trae más camiones, más tala y animales atropellados, y propuso mejorar el trazado antiguo que rodea la reserva. El ingeniero "
      "de la gobernación respondió que esa alternativa cuesta el doble. La alcaldesa cerró la sesión sin decidir: «Todos tienen parte de razón; "
      "lo que no tenemos todavía son cifras confiables».")
I("LEC-131", "LEC", "locales", "practica", -0.8, "¿Qué propone el guardabosques?",
  ["Pavimentar la vía que atraviesa la reserva.", "No hacer ninguna obra.", "Mejorar el camino antiguo que rodea la reserva.", "Prohibir el paso de camiones de leche."], "C",
  "Después de advertir los riesgos de la vía rápida, propone mejorar el trazado antiguo que rodea la reserva.", ["Su intervención tiene dos partes: una advertencia y una propuesta."], ctx=P7)
I("LEC-132", "LEC", "global", "practica", 0.2, "La intervención del ingeniero cumple en el texto la función de",
  ["apoyar la propuesta del guardabosques.", "presentar una dificultad de la alternativa propuesta.", "resolver la discusión.", "defender a doña Carmen."], "B",
  "Al decir que la alternativa cuesta el doble, señala un obstáculo para la propuesta del guardabosques, sin cerrar el debate.", ["¿A cuál propuesta se refiere 'esa alternativa'?"], ctx=P7)
I("LEC-133", "LEC", "global", "diagnostico", 0.3, "El texto presenta la discusión como",
  ["un enfrentamiento entre quienes tienen la razón y quienes no.", "un conflicto entre intereses legítimos que todavía no tiene solución.", "una decisión ya tomada por la alcaldesa.", "un problema sin importancia para el municipio."], "B",
  "Cada participante tiene razones válidas (la leche, el bosque, el costo) y la sesión termina sin decisión.", ["Mira cómo termina la sesión.", "¿El texto toma partido por alguno de los participantes?"], ctx=P7)
I("LEC-134", "LEC", "critica", "practica", 0.5, "De la frase de la alcaldesa se puede concluir que, para ella,",
  ["la obra no debe hacerse.", "la opinión del ingeniero es la única que cuenta.", "falta información para tomar una buena decisión.", "los asistentes no dijeron nada útil."], "C",
  "Reconoce que todos tienen parte de razón y señala lo que falta: 'cifras confiables'.", ["¿Qué dice la alcaldesa que 'no tenemos todavía'?"], ctx=P7)
I("LEC-135", "LEC", "critica", "practica", 0.9, "¿Cuál de las siguientes informaciones ayudaría más a tomar la decisión?",
  ["Una lista de las personas que asistieron a la asamblea.", "Un estudio que compare el costo y el impacto ambiental de las dos rutas.", "La historia de la fundación del municipio.", "El precio del queso en el pueblo vecino."], "B",
  "El desacuerdo es entre costo y daño ambiental de dos opciones: comparar ambas cosas con datos es justo lo que la alcaldesa echa de menos.", ["¿Sobre qué dos cosas no hay 'cifras confiables'?"], ctx=P7)

P8 = ("Señor director: El pasado viernes el periódico publicó que el puente de la vereda La Unión «quedó como nuevo» tras la reparación. Quienes "
      "lo cruzamos a diario sabemos que no es así. Se cambiaron las tablas, es cierto, pero los cables siguen oxidados y las barandas, sueltas. "
      "Entiendo que un periodista no puede revisar cada tornillo, pero sí puede preguntarle a la comunidad antes de repetir lo que dice el boletín "
      "de la alcaldía. No escribo para desmentir por gusto, sino porque una noticia que tranquiliza sin motivo puede costar un accidente. "
      "Atentamente, Rosa Elvira M., usuaria del puente.")
I("LEC-136", "LEC", "locales", "practica", -0.9, "¿Qué parte de la reparación reconoce la autora que sí se hizo?",
  ["El cambio de los cables.", "El arreglo de las barandas.", "El cambio de las tablas.", "La pintura del puente."], "C",
  "Dice: 'Se cambiaron las tablas, es cierto'. Los cables siguen oxidados y las barandas, sueltas.", ["Busca la expresión 'es cierto'."], ctx=P8)
I("LEC-137", "LEC", "global", "practica", 0.0, "El propósito principal de la carta es",
  ["agradecer a la alcaldía por la reparación.", "corregir una información publicada y pedir más cuidado al informar.", "solicitar la construcción de un puente nuevo.", "contar cómo es la vida en la vereda."], "B",
  "La autora desmiente que el puente 'quedó como nuevo' y le pide al periódico consultar a la comunidad.", ["¿A quién le escribe y sobre qué publicación?"], ctx=P8)
I("LEC-138", "LEC", "global", "practica", 0.4, "En la oración 'Entiendo que un periodista no puede revisar cada tornillo, pero sí puede preguntarle a la comunidad', la autora",
  ["disculpa por completo al periodista.", "acepta un límite razonable y enseguida señala lo que sí era exigible.", "acusa al periodista de mentir a propósito.", "cambia de tema."], "B",
  "Primero concede ('entiendo que...') y luego exige ('pero sí puede...'): es una concesión seguida de un reclamo.", ["Observa las dos mitades de la oración, antes y después de 'pero'."], ctx=P8)
I("LEC-139", "LEC", "critica", "diagnostico", 0.6, "La crítica central de la autora al periódico es que",
  ["publica noticias sobre veredas pequeñas.", "se basó solo en la versión oficial sin contrastarla con otras fuentes.", "no envió un ingeniero a revisar el puente.", "exagera los problemas de la comunidad."], "B",
  "Le reprocha 'repetir lo que dice el boletín de la alcaldía' sin preguntarle a la comunidad: usar una sola fuente.", ["¿De dónde sacó el periódico la información, según la autora?"], ctx=P8)
I("LEC-140", "LEC", "critica", "practica", 0.7, "Con la frase 'una noticia que tranquiliza sin motivo puede costar un accidente', la autora argumenta que",
  ["las noticias siempre deben alarmar a la gente.", "la información inexacta puede llevar a las personas a confiarse ante un riesgo real.", "los periódicos causan los accidentes.", "es mejor no publicar noticias sobre obras."], "B",
  "Si la gente cree que el puente está en buen estado, lo cruzará sin precaución: el error informativo tiene consecuencias prácticas.", ["¿Qué haría alguien que lee que el puente 'quedó como nuevo'?"], ctx=P8)
