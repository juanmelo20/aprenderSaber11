"""Preguntas ORIGINALES reservadas para los simulacros tipo examen (general-2 y general-3).
Nunca aparecen en el diagnóstico ni en la práctica. Entran en borrador."""
from __future__ import annotations

from .bank_seed import I

# =============================== SIMULACRO TIPO EXAMEN 1 (general-2) ===============================
A1 = ("Solemos pensar en el olvido como un defecto de la memoria. Sin embargo, varios investigadores sostienen que olvidar también cumple una "
      "función. Si el cerebro guardara con la misma fuerza cada detalle de cada día, sería muy difícil encontrar lo importante entre tanta "
      "información. Al debilitar los recuerdos que no se usan, el cerebro facilita que los útiles se recuperen con rapidez. Por eso recordamos "
      "mejor lo que repasamos varias veces que lo que vimos una sola vez, aunque haya sido interesante. Esto no significa que todo olvido sea "
      "bueno: algunas enfermedades destruyen recuerdos que la persona necesita. Pero en un cerebro sano, olvidar es, en parte, una forma de ordenar.")
G = "general-2"
I("LEC-S2-01", "LEC", "locales", "simulacro", -0.6, "Según el texto, ¿por qué recordamos mejor lo que repasamos varias veces?",
  ["Porque el cerebro mantiene más fuertes los recuerdos que se usan.", "Porque lo que se repasa siempre es más interesante.",
   "Porque olvidar es una enfermedad.", "Porque el cerebro guarda cada detalle con la misma fuerza."], "A",
  "El texto explica que el cerebro debilita los recuerdos que no se usan; los que se repasan se mantienen.", ["Lee la oración que empieza con 'Por eso'."], ctx=A1, sim=G)
I("LEC-S2-02", "LEC", "global", "simulacro", -0.1, "¿Cuál es la idea principal del texto?",
  ["En un cerebro sano, olvidar ayuda a organizar la memoria.", "El olvido es siempre un defecto de la memoria.", "Las enfermedades de la memoria son cada vez más comunes.", "Hay que recordar cada detalle de cada día."], "A",
  "El texto discute la idea de que el olvido es solo un defecto y concluye que, en parte, es una forma de ordenar.", ["Lee la primera y la última oración."], ctx=A1, sim=G)
I("LEC-S2-03", "LEC", "global", "simulacro", 0.4, "La oración 'Esto no significa que todo olvido sea bueno' cumple la función de",
  ["limitar el alcance de lo que se afirmó antes.", "contradecir la tesis del texto.", "introducir un ejemplo de olvido útil.", "repetir la idea principal con otras palabras."], "A",
  "El autor evita que su idea se lleve al extremo: reconoce que hay olvidos dañinos, como los que causan algunas enfermedades.", ["¿Qué pasaría si alguien entendiera que todo olvido es bueno?"], ctx=A1, sim=G)
I("LEC-S2-04", "LEC", "critica", "simulacro", 0.3, "¿Qué recomendación de estudio se apoya mejor en el texto?",
  ["Repasar varias veces lo que se quiere recordar, en lugar de verlo una sola vez.", "Leer una sola vez, pero con mucha atención.",
   "Estudiar toda la noche anterior al examen.", "Intentar memorizar cada detalle de cada día."], "A",
  "El texto dice que recordamos mejor lo que repasamos varias veces que lo que vimos una sola vez.", ["Relaciona la recomendación con la oración que empieza con 'Por eso'."], ctx=A1, sim=G)
I("LEC-S2-05", "LEC", "critica", "simulacro", 0.8, "Alguien concluye del texto que 'es bueno olvidar todo lo que se aprende'. Esa conclusión es",
  ["incorrecta, porque el texto habla del olvido de lo que no se usa y advierte que no todo olvido es bueno.", "correcta, porque el texto dice que olvidar es ordenar.",
   "correcta, porque el olvido es una función del cerebro.", "incorrecta, porque el texto dice que el olvido es siempre una enfermedad."], "A",
  "La conclusión exagera el texto: el autor dice que olvidar lo que no se usa ayuda, y aclara que algunos olvidos son dañinos.", ["Compara la palabra 'todo' de la conclusión con lo que dice el texto."], ctx=A1, sim=G)

A2 = ("Cuando el abuelo murió, a Tomás le dejaron el reloj de bolsillo que llevaba siempre en el chaleco. Estaba detenido en las cuatro y diez. "
      "Su mamá lo llevó a la relojería del pueblo, pero el relojero lo abrió, miró un rato las piezas y lo cerró sin tocarlo. —No le falta nada "
      "—dijo—. Solo hay que darle cuerda todos los días. Tomás aprendió a hacerlo cada mañana, antes de ir al colegio, sentado en la misma silla "
      "donde el abuelo se sentaba a hacerlo. Años después, cuando ya tenía un celular que daba la hora exacta, siguió dándole cuerda al reloj. "
      "No era para saber la hora.")
I("LEC-S2-06", "LEC", "locales", "simulacro", -0.8, "¿Qué dijo el relojero sobre el reloj?",
  ["Que no le faltaba nada y solo necesitaba cuerda todos los días.", "Que estaba dañado y no se podía arreglar.", "Que había que cambiarle varias piezas.", "Que era demasiado antiguo para funcionar."], "A",
  "El relojero dice: 'No le falta nada. Solo hay que darle cuerda todos los días'.", ["Lee lo que dice el relojero entre guiones."], ctx=A2, sim=G)
I("LEC-S2-07", "LEC", "locales", "simulacro", -0.4, "¿Dónde se sentaba Tomás a darle cuerda al reloj?",
  ["En la silla donde el abuelo lo hacía.", "En la relojería del pueblo.", "En el colegio, antes de clase.", "En el corredor, junto a su mamá."], "A",
  "El texto dice que lo hacía 'sentado en la misma silla donde el abuelo se sentaba a hacerlo'.", ["Busca la palabra 'silla'."], ctx=A2, sim=G)
I("LEC-S2-08", "LEC", "global", "simulacro", 0.2, "En el relato, el celular aparece para",
  ["mostrar que Tomás ya no necesitaba el reloj para saber la hora.", "explicar por qué el reloj se detuvo.", "contar que Tomás vendió el reloj.", "mostrar que el celular era un regalo del abuelo."], "A",
  "El celular daba 'la hora exacta': si Tomás seguía dándole cuerda al reloj, no era por necesidad.", ["¿Qué hace el celular que también hacía el reloj?"], ctx=A2, sim=G)
I("LEC-S2-09", "LEC", "global", "simulacro", 0.5, "La frase final, 'No era para saber la hora', da a entender que",
  ["darle cuerda al reloj era para Tomás una manera de recordar a su abuelo.", "el reloj se atrasaba y no servía.", "Tomás no sabía leer la hora.", "el celular de Tomás estaba dañado."], "A",
  "El gesto, repetido cada mañana en la silla del abuelo, tiene un valor afectivo: mantiene vivo el recuerdo.", ["Si no era para saber la hora, ¿para qué lo hacía?"], ctx=A2, sim=G)
I("LEC-S2-10", "LEC", "critica", "simulacro", 0.7, "¿Cuál título expresa mejor el sentido del relato?",
  ["La cuerda de cada mañana", "El relojero del pueblo", "Cómo reparar un reloj de bolsillo", "El celular de Tomás"], "A",
  "El centro del relato es el gesto que Tomás repite cada mañana y que lo une con su abuelo; los otros títulos se fijan en detalles secundarios.", ["¿Qué acción se repite en el relato y le da sentido?"], ctx=A2, sim=G)

B1 = ("En los últimos años, muchos jóvenes de una vereda se han ido a la ciudad. Algunos buscan estudiar en la universidad; otros, trabajos mejor "
      "pagados. Los mayores que se quedan dicen que cada vez es más difícil encontrar quién ayude en las cosechas. Un joven que regresó cuenta que "
      "en la ciudad ganaba más, pero gastaba casi todo en arriendo y transporte. La alcaldía estudia crear un programa de créditos para que los "
      "jóvenes inicien proyectos productivos en el campo.")
I("SOC-S2-01", "SOC", "perspectivas", "simulacro", -0.6, "Según los mayores que se quedan, la salida de los jóvenes ha traído como consecuencia",
  ["que falte quién ayude en las cosechas.", "que aumente el precio de los arriendos en la vereda.", "que haya más universidades en el campo.", "que se cierre la alcaldía."], "A",
  "Los mayores dicen que 'cada vez es más difícil encontrar quién ayude en las cosechas'.", ["Busca lo que dicen los mayores."], ctx=B1, sim=G)
I("SOC-S2-02", "SOC", "perspectivas", "simulacro", 0.3, "El testimonio del joven que regresó aporta a la discusión la idea de que",
  ["un salario más alto en la ciudad no siempre significa estar mejor económicamente.", "en la ciudad no hay trabajo.", "en el campo se gana más que en la ciudad.", "la universidad no sirve para conseguir empleo."], "A",
  "Ganaba más, pero gastaba casi todo en arriendo y transporte: el ingreso más alto no se tradujo en una mejor situación.", ["Compara lo que ganaba con lo que gastaba."], ctx=B1, sim=G)
I("SOC-S2-03", "SOC", "sistemico", "simulacro", 0.5, "El programa de créditos que estudia la alcaldía supone que",
  ["algunos jóvenes se quedarían en el campo si tuvieran recursos para iniciar actividades rentables allí.", "los jóvenes se van porque no les gusta el campo.",
   "los mayores deberían irse también a la ciudad.", "la universidad debería cerrarse."], "A",
  "Ofrecer créditos para proyectos en el campo solo tiene sentido si la falta de oportunidades económicas es una de las razones para irse.", ["¿Qué problema intenta resolver un crédito?"], ctx=B1, sim=G)
I("SOC-S2-04", "SOC", "sistemico", "simulacro", 0.7, "Si la migración continúa durante muchos años, un efecto probable en la vereda sería",
  ["el envejecimiento de la población y una menor producción agrícola.", "un aumento de la población joven.", "la construcción de más escuelas.", "la caída de los arriendos en la ciudad."], "A",
  "Si se van sobre todo los jóvenes, quedan principalmente personas mayores y menos manos para trabajar la tierra.", ["¿Quiénes se van y quiénes se quedan?"], ctx=B1, sim=G)

B2 = ("En un colegio, durante la campaña para personero estudiantil, un candidato regaló dulces y prometió que, si ganaba, conseguiría que se "
      "acabaran las tareas. Otra candidata presentó propuestas sobre la convivencia y la biblioteca, y explicó cómo las llevaría al consejo "
      "directivo. Algunos estudiantes dicen que votarán por el primero porque «igual el personero no puede hacer nada». La docente de sociales "
      "propone un debate público entre los candidatos antes de la elección.")
I("SOC-S2-05", "SOC", "pensamiento_social", "simulacro", -0.3, "En el gobierno escolar, la función principal del personero estudiantil es",
  ["promover el ejercicio de los derechos y deberes de los estudiantes.", "decidir las tareas que dejan los docentes.", "administrar el presupuesto del colegio.", "nombrar a los docentes."], "A",
  "El personero es un estudiante de último grado elegido por sus compañeros para promover los derechos y deberes de los estudiantes.", ["Recuerda para qué se elige un personero cada año."], ctx=B2, sim=G)
I("SOC-S2-06", "SOC", "perspectivas", "simulacro", 0.2, "¿Qué problema tiene la promesa del primer candidato?",
  ["Ofrece algo que no depende del personero y que él no puede decidir.", "Es una propuesta demasiado detallada.", "Solo beneficia a los docentes.", "No menciona los dulces."], "A",
  "Las tareas las decide cada docente dentro del plan de estudios; un personero no tiene esa facultad.", ["¿Quién decide si hay tareas en un colegio?"], ctx=B2, sim=G)
I("SOC-S2-07", "SOC", "perspectivas", "simulacro", 0.5, "La frase «igual el personero no puede hacer nada» refleja",
  ["una desconfianza en la participación que puede llevar a votar sin evaluar las propuestas.", "un conocimiento exacto de las funciones del personero.", "un apoyo a la candidata.", "una crítica a la docente de sociales."], "A",
  "Si se cree que el cargo no sirve, se vota por cualquier motivo (como los dulces) en lugar de comparar propuestas.", ["¿Qué tipo de voto produce esa forma de pensar?"], ctx=B2, sim=G)
I("SOC-S2-08", "SOC", "sistemico", "simulacro", 0.4, "El debate que propone la docente contribuiría principalmente a",
  ["que los estudiantes voten conociendo y comparando las propuestas.", "que el primer candidato gane la elección.", "que se cancelen las elecciones.", "que la docente escoja al personero."], "A",
  "Un debate público permite contrastar propuestas y preguntar si son posibles: favorece un voto informado.", ["¿Para qué sirve escuchar a los candidatos al mismo tiempo?"], ctx=B2, sim=G)

C1 = ("Un grupo de estudiantes clava un palo vertical en el patio del colegio y, cada hora, marca en el piso dónde queda la punta de su sombra, "
      "desde las 8 de la mañana hasta las 4 de la tarde.")
I("NAT-S2-01", "NAT", "explicacion", "simulacro", 0.0, "La posición de la sombra cambia durante el día porque",
  ["la Tierra rota y, vista desde ella, la posición del Sol en el cielo cambia.", "el Sol gira alrededor de la Tierra una vez al día.",
   "el palo se inclina con el calor.", "la Tierra se acerca y se aleja del Sol cada hora."], "A",
  "La rotación de la Tierra sobre su eje hace que el Sol parezca moverse por el cielo, y con él cambian la dirección y el largo de la sombra.", ["¿Qué movimiento de la Tierra dura un día?"], ctx=C1, componente="Físico", sim=G)
I("NAT-S2-02", "NAT", "explicacion", "simulacro", 0.3, "Cerca del mediodía, la sombra es más corta porque",
  ["el Sol está más alto en el cielo.", "el Sol está más cerca de la Tierra.", "hay más luz en el patio.", "el palo se calienta y se encoge."], "A",
  "Cuanto más alto está el Sol, más verticales llegan sus rayos y más corta es la sombra.", ["Piensa en cómo llegan los rayos de luz al palo en la mañana y al mediodía."], ctx=C1, componente="Físico", sim=G)
I("NAT-S2-03", "NAT", "indagacion", "simulacro", 0.5, "Para saber si el recorrido de la sombra cambia a lo largo del año, los estudiantes deberían",
  ["repetir las marcas con el mismo palo, en el mismo lugar y a las mismas horas, en distintos meses.", "usar un palo más largo cada mes.",
   "medir la sombra una sola vez, al mediodía.", "cambiar el palo de lugar cada día."], "A",
  "Para comparar meses, todo lo demás debe mantenerse igual: el palo, el lugar y las horas.", ["¿Qué debe cambiar y qué debe quedar igual para comparar?"], ctx=C1, componente="Indagación", sim=G)

D1 = ("When Camilo was fifteen, his grandmother's farm had a problem: the cows drank from a tank, and nobody knew when it was empty until the "
      "animals were thirsty. Camilo built a simple alarm with a floating bottle, a piece of wire and an old bell. When the water went down, the "
      "bottle went down too and the bell rang. He didn't win any prize, but other farmers in the village asked him to build one for them. Today "
      "Camilo studies engineering, and he says the bell taught him something important: a good idea doesn't need to be expensive.")
I("ING-S2-01", "ING", "lectura", "simulacro", -0.5, "What was the problem on the farm?",
  ["Nobody knew when the water tank was empty.", "The cows were ill.", "The bell was broken.", "The farm had no water at all."], "A",
  "'Nobody knew when it was empty until the animals were thirsty'.", ["Lee lo que viene después de 'had a problem'."], ctx=D1, sim=G)
I("ING-S2-02", "ING", "lectura", "simulacro", 0.0, "How did the alarm work?",
  ["When the water went down, the bottle went down and the bell rang.", "The cows rang the bell when they were thirsty.",
   "A computer sent a message to Camilo.", "The wire filled the tank automatically."], "A",
  "'When the water went down, the bottle went down too and the bell rang'.", ["Busca la oración que empieza con 'When'."], ctx=D1, sim=G)
I("ING-S2-03", "ING", "lectura", "simulacro", 0.2, "What happened after Camilo built the alarm?",
  ["Other farmers asked him to build one for them.", "He won a national prize.", "His grandmother sold the cows.", "He stopped studying."], "A",
  "'He didn't win any prize, but other farmers in the village asked him to build one for them'.", ["Cuidado: el texto dice que no ganó premios."], ctx=D1, sim=G)
I("ING-S2-04", "ING", "lectura", "simulacro", 0.6, "What did Camilo learn?",
  ["Good ideas can be simple and cheap.", "Engineering is very expensive.", "Cows need a lot of water.", "Prizes are the most important thing."], "A",
  "'A good idea doesn't need to be expensive'.", ["Lee la última oración."], ctx=D1, sim=G)

# =============================== SIMULACRO TIPO EXAMEN 2 (general-3) ===============================
H = "general-3"
A3 = ("Se repite que las redes sociales nos han vuelto más intolerantes. Es una explicación cómoda, porque culpa a una herramienta y no a quienes la "
      "usan. Pero tiene algo de cierto. Las plataformas muestran primero lo que provoca más reacciones, y pocas cosas provocan tantas como la "
      "indignación. Un mensaje moderado pasa desapercibido; uno agresivo se comparte miles de veces. Así, sin que nadie lo decida, lo más ruidoso "
      "parece lo más común. La responsabilidad, entonces, es doble: las empresas deberían explicar cómo eligen lo que muestran, y cada usuario "
      "podría preguntarse, antes de compartir, si quiere informar o solo ganar una discusión.")
I("LEC-S3-01", "LEC", "locales", "simulacro", -0.6, "Según el texto, ¿qué tipo de mensajes se comparten más?",
  ["Los que provocan indignación.", "Los mensajes moderados.", "Los que explican cómo funcionan las plataformas.", "Los que escriben las empresas."], "A",
  "El texto dice que la indignación provoca muchas reacciones y que 'uno agresivo se comparte miles de veces'.", ["Busca qué provoca más reacciones."], ctx=A3, sim=H)
I("LEC-S3-02", "LEC", "global", "simulacro", 0.3, "¿Cuál es la posición del autor frente a la idea de que las redes nos volvieron intolerantes?",
  ["La considera en parte cierta y reparte la responsabilidad entre las plataformas y los usuarios.", "La acepta por completo y culpa solo a las redes.",
   "La rechaza, porque las redes no influyen en nada.", "No da ninguna opinión."], "A",
  "Primero dice que es 'una explicación cómoda', luego que 'tiene algo de cierto', y concluye que 'la responsabilidad es doble'.", ["Sigue los cambios de dirección del texto: 'Pero', 'entonces'."], ctx=A3, sim=H)
I("LEC-S3-03", "LEC", "global", "simulacro", 0.5, "La expresión 'lo más ruidoso parece lo más común' significa que",
  ["los mensajes extremos, por ser los más visibles, dan la impresión de representar lo que piensa la mayoría.", "las redes sociales hacen mucho ruido.",
   "la mayoría de la gente es agresiva.", "los mensajes moderados son los más compartidos."], "A",
  "Como lo agresivo se muestra más, uno termina creyendo que es lo que piensa casi todo el mundo, aunque no sea así.", ["Relaciona la frase con las dos oraciones anteriores."], ctx=A3, sim=H)
I("LEC-S3-04", "LEC", "critica", "simulacro", 0.6, "La propuesta de que las empresas expliquen cómo eligen lo que muestran supone que",
  ["conocer ese criterio ayudaría a entender por qué se ven ciertos contenidos.", "las empresas no usan ningún criterio.", "los usuarios no tienen ninguna responsabilidad.", "las redes sociales deben desaparecer."], "A",
  "Pedir que se explique el criterio solo tiene sentido si saberlo ayuda a los usuarios a entender lo que ven.", ["¿Para qué serviría que las empresas explicaran su criterio?"], ctx=A3, sim=H)
I("LEC-S3-05", "LEC", "critica", "simulacro", 0.9, "¿Cuál de estos hechos debilitaría el argumento del autor?",
  ["Un estudio que muestre que los mensajes moderados se comparten tanto como los agresivos.", "Un estudio que muestre que la indignación genera muchas reacciones.",
   "Una encuesta en la que los usuarios dicen que comparten sin pensar.", "Un informe según el cual las plataformas priorizan lo que genera reacciones."], "A",
  "El argumento descansa en que lo agresivo se difunde más que lo moderado. Si se difundieran igual, el razonamiento perdería su base.", ["¿Cuál es el dato del que depende el argumento?"], ctx=A3, sim=H)

A4 = ("CONVOCATORIA: BECAS «TALENTO RURAL» 2027 (texto creado para este ejercicio)\nDirigida a: estudiantes de grado 11 de colegios rurales del "
      "departamento.\nQué cubre: matrícula completa en programas técnicos y tecnológicos de instituciones aliadas, y un apoyo mensual para "
      "transporte.\nRequisitos: 1) Estar matriculado en grado 11 en un colegio rural. 2) Presentar la prueba Saber 11 antes del cierre. 3) Carta de "
      "motivación de máximo una página. 4) Certificado de residencia en zona rural.\nNo se exige un puntaje mínimo: se valoran el puntaje, la carta "
      "y la participación en proyectos de la comunidad.\nCierre: 30 de marzo. No se reciben documentos incompletos.")
I("LEC-S3-06", "LEC", "locales", "simulacro", -0.7, "¿Qué cubre la beca?",
  ["La matrícula completa en programas técnicos y tecnológicos aliados, y un apoyo mensual para transporte.", "La matrícula en cualquier universidad del país.",
   "Solo el transporte durante el grado 11.", "La inscripción a la prueba Saber 11."], "A",
  "La sección 'Qué cubre' lo dice textualmente.", ["Busca la sección 'Qué cubre'."], ctx=A4, sim=H)
I("LEC-S3-07", "LEC", "locales", "simulacro", 0.1, "Una estudiante de grado 11 vive en zona rural, pero estudia en un colegio urbano. ¿Puede aplicar?",
  ["No, porque debe estar matriculada en un colegio rural.", "Sí, porque vive en zona rural.", "Sí, si tiene un puntaje alto.", "No, porque la beca es solo para grado 10."], "A",
  "El requisito 1 exige estar matriculado en un colegio rural; vivir en zona rural es necesario, pero no suficiente.", ["Revisa los cuatro requisitos uno por uno."], ctx=A4, sim=H)
I("LEC-S3-08", "LEC", "global", "simulacro", 0.4, "La frase 'No se exige un puntaje mínimo' busca",
  ["animar a aplicar a quienes no tienen puntajes muy altos, porque también se valoran otros aspectos.", "indicar que el puntaje no se tendrá en cuenta.",
   "eliminar el requisito de presentar la prueba Saber 11.", "advertir que la beca es solo para quienes obtengan el mejor puntaje."], "A",
  "El puntaje se valora, pero junto con la carta y la participación comunitaria; no hay un mínimo que excluya de entrada.", ["Lee lo que viene después de los dos puntos."], ctx=A4, sim=H)
I("LEC-S3-09", "LEC", "critica", "simulacro", 0.6, "Un estudiante envía todo, menos la carta de motivación, porque cree que 'lo importante es el puntaje'. Según la convocatoria,",
  ["su solicitud no será recibida, porque no se aceptan documentos incompletos.", "su solicitud será recibida, porque el puntaje es lo más importante.",
   "podrá enviar la carta después del cierre.", "le darán la beca si su puntaje es alto."], "A",
  "La última línea dice que no se reciben documentos incompletos, y la carta es el requisito 3.", ["Lee la última línea de la convocatoria."], ctx=A4, sim=H)
I("LEC-S3-10", "LEC", "global", "simulacro", -0.2, "El propósito de este texto es",
  ["informar a los posibles aspirantes las condiciones para obtener la beca.", "contar la historia de un estudiante becado.", "opinar sobre la educación rural.", "explicar cómo se califica la prueba Saber 11."], "A",
  "Es una convocatoria: informa a quién va dirigida, qué ofrece, qué se necesita y hasta cuándo.", ["¿Qué tipo de texto es una convocatoria?"], ctx=A4, sim=H)

B3 = ("Una alcaldía destinó una parte del presupuesto para que los habitantes decidieran en qué invertirla. Cada vereda presentó proyectos y luego "
      "todos votaron. Ganó el arreglo de una vía terciaria, apoyado por las veredas más pobladas. Las veredas pequeñas, que habían propuesto un "
      "acueducto, se quejaron de que nunca podrán ganar una votación. Un líder propone que, el próximo año, una parte del dinero se reparta por "
      "igual entre todas las veredas y el resto se decida por votación.")
I("SOC-S3-01", "SOC", "pensamiento_social", "simulacro", -0.5, "El mecanismo que usó la alcaldía es un ejemplo de",
  ["participación ciudadana en las decisiones públicas.", "un referendo para reformar la Constitución.", "una acción de tutela.", "una decisión del Congreso."], "A",
  "Los habitantes propusieron y votaron en qué se invertía una parte del presupuesto: participaron directamente en una decisión pública.", ["¿Quién tomó la decisión sobre el dinero?"], ctx=B3, sim=H)
I("SOC-S3-02", "SOC", "perspectivas", "simulacro", 0.3, "La queja de las veredas pequeñas señala que",
  ["la regla de la mayoría puede dejar siempre sin atender a los grupos con menos votos.", "la votación fue un fraude.", "las veredas grandes no necesitaban la vía.", "el acueducto era más barato que la vía."], "A",
  "Si siempre ganan las veredas con más habitantes, las pequeñas nunca verán sus proyectos aprobados, aunque sean necesarios.", ["¿Por qué dicen que 'nunca' podrán ganar?"], ctx=B3, sim=H)
I("SOC-S3-03", "SOC", "sistemico", "simulacro", 0.5, "La propuesta del líder busca",
  ["equilibrar la decisión por mayoría con una garantía mínima para todas las veredas.", "eliminar la votación.", "que solo decidan las veredas pequeñas.", "que la alcaldía decida sin consultar."], "A",
  "Una parte se reparte por igual (garantía para todos) y otra se vota (decisión por mayoría).", ["¿Qué parte de la propuesta protege a las veredas pequeñas y cuál conserva la votación?"], ctx=B3, sim=H)
I("SOC-S3-04", "SOC", "sistemico", "simulacro", 0.6, "Que el acueducto no se haya escogido puede tener como consecuencia",
  ["que continúen los problemas de acceso al agua y de salud en las veredas pequeñas.", "que la vía terciaria no se construya.", "que aumente la población de las veredas pequeñas.", "que se acabe el presupuesto participativo."], "A",
  "El acueducto respondía a una necesidad de agua; si no se construye, esa necesidad sigue sin atenderse.", ["¿Qué necesidad atendía el acueducto?"], ctx=B3, sim=H)

B4 = ("La única cancha de un barrio la usan en las tardes jóvenes que juegan fútbol. Un grupo de adultos mayores le pidió a la junta de acción "
      "comunal usarla dos tardes por semana para hacer ejercicio dirigido. Los jóvenes dicen que la cancha siempre ha sido para el fútbol y que no "
      "tienen otro lugar. Los adultos mayores responden que el espacio es público y que también tienen derecho a la recreación. La junta debe decidir.")
I("SOC-S3-05", "SOC", "pensamiento_social", "simulacro", 0.0, "El argumento de los adultos mayores se basa en que",
  ["el espacio público es de todos y la recreación es un derecho de las personas de cualquier edad.", "los jóvenes no deberían jugar fútbol.", "la junta es dueña de la cancha.", "el ejercicio es más importante que el fútbol."], "A",
  "La Constitución reconoce el derecho de todas las personas a la recreación, y el espacio público es de uso común.", ["¿Qué dos ideas usan los adultos mayores?"], ctx=B4, sim=H)
I("SOC-S3-06", "SOC", "perspectivas", "simulacro", -0.2, "El argumento de los jóvenes se basa principalmente en",
  ["la costumbre de usar la cancha y la falta de otro lugar.", "que el espacio es público.", "que los adultos mayores no pueden hacer ejercicio.", "una norma de la alcaldía."], "A",
  "Dicen que 'siempre ha sido para el fútbol' (costumbre) y que 'no tienen otro lugar'.", ["Lee lo que dicen los jóvenes."], ctx=B4, sim=H)
I("SOC-S3-07", "SOC", "sistemico", "simulacro", 0.4, "¿Qué decisión de la junta tendría en cuenta los intereses de ambos grupos?",
  ["Acordar horarios de uso compartido y gestionar con la alcaldía otro espacio recreativo.", "Dejar la cancha solo para el fútbol.", "Prohibir el fútbol en la cancha.", "Cerrar la cancha hasta que haya otra."], "A",
  "Repartir horarios atiende a los dos grupos ahora, y buscar otro espacio responde a la falta de lugares.", ["Busca la opción que no deja a ningún grupo sin nada."], ctx=B4, sim=H)
I("SOC-S3-08", "SOC", "perspectivas", "simulacro", 0.6, "Para que ambos grupos vean la decisión como legítima, sería importante que la junta",
  ["escuche a los dos grupos antes de decidir y explique las razones de su decisión.", "decida en secreto para evitar discusiones.", "deje que decida el grupo más numeroso sin discutir.", "pida a la policía que tome la decisión."], "A",
  "Una decisión se acepta mejor cuando quienes se ven afectados fueron escuchados y conocen sus razones.", ["¿Qué hace que una decisión parezca justa a quienes no ganaron?"], ctx=B4, sim=H)

C2 = ("Antes de que existieran las vacunas, enfermedades como el sarampión afectaban a casi todos los niños. Una vacuna contiene el microorganismo "
      "debilitado o inactivado, o solo una parte de él, de modo que no causa la enfermedad. Después de vacunarse, el cuerpo produce defensas contra "
      "ese microorganismo. En una comunidad donde casi todos están vacunados, incluso quienes no pueden vacunarse, como algunos recién nacidos, "
      "tienen menos probabilidad de contagiarse.")
I("NAT-S3-01", "NAT", "explicacion", "simulacro", 0.0, "La vacuna protege porque",
  ["prepara al sistema inmunológico para reconocer el microorganismo y defenderse rápido si entra al cuerpo.", "mata a todos los microorganismos que hay en el cuerpo.",
   "reemplaza las defensas del cuerpo por otras artificiales.", "funciona como un antibiótico que dura toda la vida."], "A",
  "Al encontrarse con el microorganismo debilitado o una parte de él, el cuerpo produce defensas y guarda memoria; si llega el verdadero, responde rápido.", ["¿Qué produce el cuerpo después de vacunarse, según el texto?"], ctx=C2, componente="Biológico", sim=H)
I("NAT-S3-02", "NAT", "explicacion", "simulacro", 0.5, "Los recién nacidos no vacunados están más protegidos en una comunidad muy vacunada porque",
  ["hay menos personas que puedan contagiarse y transmitirles el microorganismo.", "reciben las defensas por el aire.", "el microorganismo no ataca a los recién nacidos.", "las vacunas de los demás los curan."], "A",
  "Si casi todos están protegidos, el microorganismo encuentra pocas personas a través de las cuales propagarse, y llega menos a quienes no pueden vacunarse.", ["Piensa en cómo pasa un microorganismo de una persona a otra."], ctx=C2, componente="Biológico", sim=H)
I("NAT-S3-03", "NAT", "uso", "simulacro", -0.3, "Según el texto, la vacuna no causa la enfermedad porque",
  ["contiene el microorganismo debilitado o inactivado, o solo una parte de él.", "contiene antibióticos.", "se aplica a personas sanas.", "el sarampión ya no existe."], "A",
  "El texto lo explica en la segunda oración.", ["Lee la segunda oración."], ctx=C2, componente="Biológico", sim=H)

D2 = ("For many years, an old bus stood broken in a field outside the village of Santa Rosa. Then a group of parents had an idea. They painted it "
      "in bright colours, put shelves inside and filled them with books that families donated. Now the bus is a small library that opens every "
      "afternoon. A retired teacher looks after it, and older students read to younger children there. The village still has no public library, "
      "but the parents say the bus is a good start.")
I("ING-S3-01", "ING", "lectura", "simulacro", -0.6, "What was the bus like before the parents' idea?",
  ["It was old and broken.", "It was new and colourful.", "It was a school bus that took children to town.", "It was already a library."], "A",
  "'An old bus stood broken in a field'.", ["Lee la primera oración."], ctx=D2, sim=H)
I("ING-S3-02", "ING", "lectura", "simulacro", -0.2, "Where do the books come from?",
  ["Families donated them.", "The government bought them.", "The retired teacher wrote them.", "The children bought them in town."], "A",
  "'Books that families donated'.", ["Busca la palabra 'books'."], ctx=D2, sim=H)
I("ING-S3-03", "ING", "lectura", "simulacro", 0.1, "Who looks after the library?",
  ["A retired teacher.", "The older students.", "The bus driver.", "The mayor of the village."], "A",
  "'A retired teacher looks after it'. Los estudiantes mayores leen a los niños, pero no la administran.", ["Busca 'looks after'."], ctx=D2, sim=H)
I("ING-S3-04", "ING", "lectura", "simulacro", 0.6, "What do the parents think?",
  ["The bus is a first step, although the village still needs a public library.", "The bus is better than any public library.",
   "The bus should be sold.", "The village does not need more books."], "A",
  "'The village still has no public library, but the parents say the bus is a good start'.", ["Lee la última oración."], ctx=D2, sim=H)
