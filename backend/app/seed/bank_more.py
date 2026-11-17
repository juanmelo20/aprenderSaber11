"""Tercera tanda de preguntas ORIGINALES para práctica: Lectura Crítica, Sociales, Ciencias (explicación de fenómenos)
e Inglés (lectura). Entran en borrador, como el resto del banco."""
from __future__ import annotations

from .bank_seed import I

# =============================== LECTURA CRÍTICA ===============================
Q1 = ("En los campos colombianos viven abejas nativas que no tienen aguijón. Son más pequeñas que la abeja común, que llegó de otros "
      "continentes, y forman sus colmenas en troncos huecos, grietas de muros o incluso dentro de la tierra. Durante siglos, comunidades "
      "campesinas e indígenas han guardado su miel, más líquida y ácida que la de la abeja común, y la han usado como remedio casero. Su papel "
      "más importante, sin embargo, es otro: al visitar las flores, llevan el polen de una planta a otra y permiten que muchas plantas silvestres "
      "y cultivos den fruto. La tala de bosques y el uso de algunos plaguicidas han reducido sus colonias. Por eso, en varias regiones se promueve "
      "la meliponicultura, la cría de estas abejas en cajas de madera, que permite cuidarlas sin destruir los árboles donde viven.")
I("LEC-141", "LEC", "locales", "practica", -1.0, "Según el texto, ¿en qué se diferencia la miel de las abejas nativas de la de la abeja común?",
  ["Es más líquida y más ácida.", "Es más espesa y más dulce.", "No se puede consumir.", "Solo se produce en cajas de madera."], "A",
  "El texto dice que su miel es 'más líquida y ácida que la de la abeja común'.", ["Busca la comparación entre las dos mieles en la tercera oración."], ctx=Q1)
I("LEC-142", "LEC", "locales", "practica", -0.6, "Según el texto, ¿qué es la meliponicultura?",
  ["La cría de abejas nativas sin aguijón en cajas de madera.", "El estudio de las propiedades medicinales de la miel.", "La tala controlada de los bosques.", "El uso de plaguicidas en los cultivos."], "A",
  "La última oración la define: 'la cría de estas abejas en cajas de madera'.", ["La definición aparece justo después de la palabra, separada por una coma."], ctx=Q1)
I("LEC-143", "LEC", "global", "practica", 0.1, "La expresión 'Su papel más importante, sin embargo, es otro' sirve para",
  ["presentar un aporte de las abejas que el autor valora más que el uso medicinal de su miel.", "contradecir lo que se dijo sobre las colmenas.", "dar un ejemplo de cómo se usa la miel.", "concluir que la miel de estas abejas no sirve."], "A",
  "Después de hablar de la miel, el conector 'sin embargo' introduce algo que el autor considera más importante: la polinización.", ["¿Qué se dice antes del conector y qué se dice después?"], ctx=Q1)
I("LEC-144", "LEC", "global", "practica", -0.1, "¿Cuál opción expresa mejor la idea principal del texto?",
  ["Las abejas nativas sin aguijón son valiosas por la polinización y su cría se promueve porque sus colonias han disminuido.", "La miel de las abejas nativas es mejor remedio que los medicamentos.",
   "La abeja común debe reemplazarse por la abeja nativa.", "Los plaguicidas son la única causa de la desaparición de las abejas."], "A",
  "El texto reúne qué son estas abejas, por qué importan (polinización) y por qué se busca protegerlas. Las otras opciones exageran o toman un solo detalle.",
  ["Una idea principal recoge todo el texto.", "Desconfía de palabras absolutas como 'única' o 'mejor'."], ctx=Q1)
I("LEC-145", "LEC", "critica", "practica", 0.6, "Un agricultor dice: 'Esas abejas no me sirven, porque producen poca miel'. Con base en el texto, la mejor respuesta sería:",
  ["Su principal aporte no es la miel, sino la polinización, que ayuda a que los cultivos den fruto.", "Su miel es más dulce que la de la abeja común.",
   "Producen más miel cuando viven en troncos huecos.", "Como no tienen aguijón, son más fáciles de vender."], "A",
  "El argumento del agricultor mide la utilidad solo por la miel; el texto dice que su papel más importante es polinizar.", ["¿Qué dice el texto que es lo más importante de estas abejas?"], ctx=Q1)

Q2 = ("Muchos padres creen que leerles en voz alta a sus hijos solo tiene sentido mientras los niños no saben leer. Apenas aprenden, el libro "
      "pasa a ser una tarea escolar que se hace en silencio y a solas. Es una lástima. Leer juntos no sirve solo para aprender las letras: es un "
      "rato en el que se conversa sobre lo que les pasa a los personajes, se preguntan palabras desconocidas y se descubre que una historia "
      "puede discutirse. Además, quien escucha puede seguir un relato más complejo que el que podría leer por sí mismo. No se necesita una "
      "biblioteca en casa ni mucho tiempo: bastan quince minutos, un cuento prestado y las ganas de hacerlo. Lo que se pierde al abandonar esa "
      "costumbre no es una técnica, sino un espacio de encuentro.")
I("LEC-146", "LEC", "locales", "practica", -0.9, "Según el texto, ¿qué ocurre en muchos hogares cuando los niños aprenden a leer?",
  ["La lectura se vuelve una tarea solitaria y en silencio.", "Los niños empiezan a leerles en voz alta a sus padres.", "Los niños dejan de leer por completo.", "Los padres compran más libros."], "A",
  "El texto dice que 'el libro pasa a ser una tarea escolar que se hace en silencio y a solas'.", ["Lee la oración que empieza con 'Apenas aprenden'."], ctx=Q2)
I("LEC-147", "LEC", "global", "practica", -0.2, "¿Cuál es la tesis del autor?",
  ["Conviene seguir leyendo en voz alta en familia aunque los niños ya sepan leer.", "Los niños deben aprender a leer antes de entrar al colegio.",
   "Leer en silencio es más útil que leer en voz alta.", "Las familias necesitan una biblioteca en casa para leer."], "A",
  "Todo el texto defiende que la lectura compartida tiene valor más allá de aprender las letras.", ["¿Qué costumbre defiende el autor y en qué momento dice que se suele abandonar?"], ctx=Q2)
I("LEC-148", "LEC", "global", "practica", 0.4, "La oración 'No se necesita una biblioteca en casa ni mucho tiempo' responde a una posible objeción según la cual",
  ["leer en familia exige recursos y tiempo que muchas familias no tienen.", "los niños prefieren leer solos.", "los cuentos prestados son de mala calidad.", "las bibliotecas públicas están cerradas."], "A",
  "El autor se adelanta a quien diría que no tiene libros ni tiempo, y responde que basta con poco.", ["¿Qué excusa podría poner alguien para no leer con sus hijos?"], ctx=Q2)
I("LEC-149", "LEC", "critica", "practica", 0.5, "¿Cuál de los siguientes argumentos usa el autor para defender su tesis?",
  ["Quien escucha puede comprender historias más complejas que las que podría leer solo.", "Los estudios demuestran que leer en voz alta mejora las notas.",
   "Los niños que leen solos se aburren siempre.", "Leer en voz alta es una tradición en todas las culturas."], "A",
  "Ese argumento está en el texto ('quien escucha puede seguir un relato más complejo'). El texto no cita estudios ni habla de otras culturas.", ["Comprueba cuál de las opciones aparece realmente en el texto."], ctx=Q2)
I("LEC-150", "LEC", "critica", "practica", 0.2, "¿Qué tipo de texto es este?",
  ["Una columna de opinión que defiende una costumbre.", "Un cuento con personajes y conflicto.", "Una noticia sobre un hecho reciente.", "Un instructivo con pasos para aprender a leer."], "A",
  "El autor expresa valoraciones ('Es una lástima') y da razones para convencer: es un texto argumentativo de opinión.", ["¿El autor narra, informa un hecho o da su opinión con razones?"], ctx=Q2)

Q3 = ("Doña Inés tenía el único radio de la vereda. Los sábados por la noche, los vecinos se sentaban en el corredor de su casa a escuchar la "
      "radionovela, y ella subía el volumen para que alcanzara hasta el último banco. Cuando llegó la luz eléctrica, cada familia compró su propio "
      "aparato y los sábados el corredor se quedó vacío. Doña Inés no dijo nada. Siguió sacando el radio cada sábado, lo ponía sobre el banco del "
      "rincón y se sentaba a escuchar sola, con la puerta abierta. Un sábado de lluvia se fue la luz en toda la vereda. A las ocho, uno a uno, los "
      "vecinos fueron llegando al corredor, mojados, con la excusa de preguntar si ella tenía pilas. Doña Inés tenía.")
I("LEC-151", "LEC", "locales", "practica", -1.0, "¿Por qué el corredor de doña Inés se quedó vacío los sábados?",
  ["Porque, al llegar la luz eléctrica, cada familia compró su propio radio.", "Porque doña Inés dejó de poner la radionovela.",
   "Porque los vecinos se pelearon con ella.", "Porque la radionovela dejó de transmitirse."], "A",
  "El texto lo dice: 'Cuando llegó la luz eléctrica, cada familia compró su propio aparato'.", ["Busca qué cambió en la vereda justo antes de que el corredor se quedara vacío."], ctx=Q3)
I("LEC-152", "LEC", "locales", "practica", -0.5, "¿Qué hace doña Inés después de que los vecinos dejan de ir?",
  ["Sigue escuchando la radionovela cada sábado, con la puerta abierta.", "Guarda el radio y no vuelve a usarlo.", "Vende su radio.", "Va a escuchar la radionovela a otras casas."], "A",
  "'Siguió sacando el radio cada sábado [...] y se sentaba a escuchar sola, con la puerta abierta'.", ["Lee lo que viene después de 'Doña Inés no dijo nada'."], ctx=Q3)
I("LEC-153", "LEC", "global", "practica", 0.3, "La expresión 'con la excusa de preguntar si ella tenía pilas' sugiere que los vecinos",
  ["querían volver a reunirse, aunque no lo dijeran directamente.", "solo necesitaban pilas para sus linternas.", "estaban molestos por el apagón.", "querían comprarle el radio."], "A",
  "Una 'excusa' es una razón que se da para ocultar otra. Todos llegan a la hora de la radionovela: lo que buscan es el encuentro.", ["¿Qué significa que algo sea una 'excusa'?", "Fíjate en la hora a la que llegan."], ctx=Q3)
I("LEC-154", "LEC", "global", "practica", 0.6, "La frase final, 'Doña Inés tenía.', produce el efecto de",
  ["mostrar que ella estaba preparada y que la reunión de los sábados volvería.", "indicar que doña Inés se negó a ayudar.", "explicar la causa del apagón.", "contradecir lo que se dijo antes sobre el radio."], "A",
  "La respuesta breve cierra la historia: doña Inés nunca dejó de esperar a sus vecinos, y con las pilas el encuentro se reanuda.", ["Relaciona la frase con lo que doña Inés hizo todos esos sábados."], ctx=Q3)
I("LEC-155", "LEC", "critica", "practica", 0.7, "¿Cuál de estas ideas se relaciona mejor con el relato?",
  ["Algunos avances traen comodidad, pero pueden debilitar la vida en comunidad.", "La luz eléctrica no trajo ningún beneficio a la vereda.",
   "Todas las familias deberían tener pilas en casa.", "Escuchar radio es mejor que ver televisión."], "A",
  "Con la luz cada familia ganó su propio radio, pero se perdió el encuentro. El relato no dice que la luz no sirviera.", ["Descarta las opciones que el relato no permite afirmar."], ctx=Q3)

Q4 = ("¡QUE EL ZANCUDO NO SE CRÍE EN TU CASA!\nEl dengue se transmite por la picadura del zancudo Aedes aegypti, que pone sus huevos en agua "
      "limpia y quieta.\n1. Lava con cepillo, cada semana, tanques y albercas: los huevos se pegan a las paredes.\n2. Tapa bien los recipientes "
      "donde guardas agua.\n3. Voltea botellas, llantas y baldes que puedan acumular lluvia.\n4. Cambia cada tres días el agua de floreros y "
      "bebederos de animales.\nSi tienes fiebre alta, dolor detrás de los ojos y dolor en el cuerpo, consulta al puesto de salud. No te "
      "automediques.\nSecretaría de Salud Municipal")
I("LEC-156", "LEC", "locales", "practica", -0.7, "Según el afiche, ¿por qué hay que lavar los tanques con cepillo y no solo cambiarles el agua?",
  ["Porque los huevos del zancudo se pegan a las paredes.", "Porque el agua de los tanques se ensucia con la lluvia.", "Porque el cepillo mata a los zancudos adultos.", "Porque el zancudo no pone huevos en agua limpia."], "A",
  "La recomendación 1 lo explica: 'los huevos se pegan a las paredes'.", ["Lee lo que viene después de los dos puntos en la recomendación 1."], ctx=Q4)
I("LEC-157", "LEC", "locales", "practica", -0.8, "¿Qué recomienda el afiche a quien tenga fiebre alta y dolor detrás de los ojos?",
  ["Ir al puesto de salud y no tomar medicamentos por su cuenta.", "Voltear los recipientes con agua.", "Tomar un analgésico y descansar.", "Lavar los tanques cada semana."], "A",
  "La penúltima parte dice: 'consulta al puesto de salud. No te automediques'.", ["Busca la parte del afiche que habla de síntomas."], ctx=Q4)
I("LEC-158", "LEC", "global", "practica", -0.3, "El propósito principal del afiche es",
  ["que las personas eviten que el zancudo se reproduzca en sus casas.", "contar la historia del dengue en el municipio.", "vender productos para matar zancudos.", "informar cuántos casos de dengue hay."], "A",
  "El título y las cuatro recomendaciones apuntan a lo mismo: que el zancudo no se críe en las casas.", ["Lee el título del afiche."], ctx=Q4)
I("LEC-159", "LEC", "global", "practica", 0.3, "Las cuatro recomendaciones numeradas tienen en común que",
  ["buscan eliminar el agua limpia y quieta donde el zancudo pone sus huevos.", "describen los síntomas de la enfermedad.", "se deben hacer una sola vez al año.", "están dirigidas solo a quienes tienen animales."], "A",
  "Lavar, tapar, voltear y cambiar el agua sirven para que no haya agua quieta disponible para los huevos.", ["Relaciona cada recomendación con la segunda oración del afiche."], ctx=Q4)
I("LEC-160", "LEC", "critica", "practica", 0.6, "Una familia guarda agua lluvia en un balde destapado 'porque el agua está limpia'. Según el afiche, esa razón",
  ["no es válida, porque el zancudo justamente pone sus huevos en agua limpia y quieta.", "es válida, porque el zancudo solo se cría en agua sucia.",
   "es válida si el balde está en el patio.", "no es válida, porque el agua lluvia siempre está contaminada."], "A",
  "El afiche dice que el zancudo pone sus huevos 'en agua limpia y quieta': que el agua esté limpia no protege, al contrario.", ["¿Qué tipo de agua busca el zancudo, según el afiche?"], ctx=Q4)

Q5 = ("¿Está mal mentir para no lastimar a alguien? Quien defiende la mentira piadosa argumenta que lo importante no es la verdad en sí, sino el "
      "bienestar de las personas: si decir que el regalo nos encantó evita una tristeza inútil, la mentira hace más bien que mal. Quien la rechaza "
      "responde que esa cuenta es engañosa. Cada mentira, por pequeña que sea, trata al otro como alguien incapaz de soportar la verdad y decide "
      "por él qué le conviene saber. Además, si todos mintiéramos cuando creemos que es por el bien ajeno, ya nadie podría confiar en las palabras "
      "amables de los demás. Entre ambas posiciones queda una pregunta difícil: ¿la sinceridad obliga a decirlo todo, o solo a no afirmar lo que es falso?")
I("LEC-161", "LEC", "locales", "practica", -0.6, "Según el texto, quienes defienden la mentira piadosa consideran que lo más importante es",
  ["el bienestar de las personas.", "la verdad en sí misma.", "la confianza en las palabras de los demás.", "decir siempre todo lo que se piensa."], "A",
  "El texto dice que para ellos 'lo importante no es la verdad en sí, sino el bienestar de las personas'.", ["Lee la segunda oración."], ctx=Q5)
I("LEC-162", "LEC", "locales", "practica", 0.2, "Según quienes rechazan la mentira piadosa, el problema de mentir 'por el bien' del otro es que",
  ["se decide por él lo que le conviene saber, como si no pudiera soportar la verdad.", "siempre termina descubriéndose.", "produce más tristeza que la verdad.", "está prohibido por la ley."], "A",
  "El texto dice que cada mentira 'trata al otro como alguien incapaz de soportar la verdad y decide por él qué le conviene saber'.", ["Busca la parte que empieza con 'Quien la rechaza'."], ctx=Q5)
I("LEC-163", "LEC", "global", "practica", 0.4, "El argumento 'si todos mintiéramos cuando creemos que es por el bien ajeno, ya nadie podría confiar en las palabras amables' sostiene que la mentira piadosa,",
  ["si se generalizara, destruiría la confianza.", "hace más bien que mal.", "solo es aceptable entre amigos.", "es imposible de descubrir."], "A",
  "El argumento imagina qué pasaría si todos la practicaran: las palabras amables perderían su valor porque nadie sabría si son sinceras.", ["Fíjate en la palabra 'todos'."], ctx=Q5)
I("LEC-164", "LEC", "global", "practica", 0.5, "¿Cómo está organizado el texto?",
  ["Presenta una postura, luego la contraria con sus razones, y cierra con una pregunta abierta.", "Narra una historia y termina con una moraleja.",
   "Define la mentira y da ejemplos históricos.", "Defiende una sola postura de principio a fin."], "A",
  "Primero habla quien defiende la mentira piadosa, luego quien la rechaza, y al final queda una pregunta sin resolver.", ["¿Cuántas posturas aparecen y cómo termina el texto?"], ctx=Q5)
I("LEC-165", "LEC", "critica", "practica", 0.9, "La pregunta final distingue dos ideas de sinceridad. ¿Cuál situación corresponde a 'no afirmar lo que es falso' sin 'decirlo todo'?",
  ["Ante un regalo que no le gustó, alguien agradece el gesto sin decir que le encantó.", "Alguien dice que el regalo le encantó, aunque no le gustó.",
   "Alguien enumera todos los defectos del regalo.", "Alguien recibe el regalo sin decir nada y se va."], "A",
  "Agradecer el gesto es verdad y no obliga a dar una opinión sobre el regalo: no se miente ni se dice todo. Decir que le encantó sería afirmar algo falso.",
  ["Busca la opción en la que no se dice nada falso, pero tampoco se dice todo lo que se piensa."], ctx=Q5)

# =============================== SOCIALES ===============================
S1 = ("Tras varios robos cometidos por personas que se movilizaban en moto, la alcaldía de un municipio prohibió llevar parrillero hombre durante "
      "tres meses. La policía afirma que la medida facilita los controles. Los mototaxistas, muchos de ellos sin otro empleo, dicen que perderán "
      "buena parte de sus ingresos. Algunas familias se quejan de que ya no pueden llevar a sus hijos mayores al colegio en la moto de la casa. "
      "Un concejal propone, en cambio, aumentar el patrullaje en los barrios con más robos.")
I("SOC-137", "SOC", "perspectivas", "practica", -0.7, "¿Qué preocupa principalmente a los mototaxistas?",
  ["Perder buena parte de sus ingresos.", "Que aumenten los robos en moto.", "Que la policía no pueda hacer controles.", "Que el concejo no apruebe más patrullaje."], "A",
  "El texto dice que los mototaxistas, muchos sin otro empleo, temen perder buena parte de sus ingresos.", ["Busca la oración que habla de los mototaxistas."], ctx=S1)
I("SOC-138", "SOC", "perspectivas", "practica", 0.2, "La propuesta del concejal se diferencia de la medida de la alcaldía en que",
  ["busca reducir los robos sin restringir a todos los motociclistas.", "prohíbe del todo el uso de motos.", "extiende la restricción a todos los parrilleros.", "no tiene como objetivo reducir los robos."], "A",
  "Ambas buscan reducir los robos, pero el patrullaje en barrios específicos no limita a quienes usan la moto para trabajar o para llevar a sus hijos.", ["¿Comparten el objetivo? ¿En qué cambia el medio para lograrlo?"], ctx=S1)
I("SOC-139", "SOC", "sistemico", "practica", 0.4, "Un efecto no buscado de la medida podría ser",
  ["que aumenten las dificultades económicas de quienes viven del mototaxismo.", "que desaparezcan los robos en todo el país.", "que bajen los precios de las motos nuevas.", "que aumente el número de parrilleros."], "A",
  "La medida busca seguridad, pero también afecta el trabajo de quienes llevan pasajeros en moto: es una consecuencia no buscada.", ["Piensa en quiénes, además de los delincuentes, usan moto con parrillero."], ctx=S1)
I("SOC-140", "SOC", "perspectivas", "practica", 0.6, "Para evaluar si la medida funcionó, la información más útil sería",
  ["el número de robos en moto antes y durante los tres meses.", "la opinión de los mototaxistas sobre la medida.", "el número de motos vendidas en el municipio.", "la cantidad de multas impuestas por llevar parrillero."], "A",
  "El objetivo era reducir los robos: hay que comparar los robos antes y después. Las multas solo dicen cuántas personas incumplieron la norma.", ["¿Cuál era el objetivo de la medida?"], ctx=S1)

S2 = ("La secretaría de educación anunció que cerrará la escuela de una vereda porque solo tiene siete estudiantes y mantenerla cuesta casi lo mismo "
      "que una escuela de treinta. Los niños serían trasladados a una sede a una hora de camino, con transporte escolar. Las familias se oponen: dicen "
      "que en invierno el camino se vuelve peligroso y que la escuela es también el lugar donde se reúne la junta de acción comunal. La docente, que "
      "vive en la vereda, teme que los niños más pequeños abandonen el estudio.")
I("SOC-141", "SOC", "perspectivas", "practica", -0.6, "¿En qué se basa la decisión de la secretaría de educación?",
  ["En el alto costo de mantener una escuela con pocos estudiantes.", "En que la docente quiere irse de la vereda.", "En que el camino es peligroso en invierno.", "En una petición de la junta de acción comunal."], "A",
  "La secretaría argumenta que una escuela de siete estudiantes cuesta casi lo mismo que una de treinta.", ["Lee la razón que da la secretaría en la primera oración."], ctx=S2)
I("SOC-142", "SOC", "perspectivas", "practica", 0.0, "Las familias y la docente coinciden en preocuparse por",
  ["que los niños puedan seguir estudiando sin riesgos.", "el costo de mantener la escuela.", "el salario de la docente.", "el número de estudiantes de la otra sede."], "A",
  "Las familias temen por la seguridad del camino y la docente teme la deserción: a ambas les preocupa la continuidad y la seguridad de los niños.", ["Compara la preocupación de las familias con la de la docente."], ctx=S2)
I("SOC-143", "SOC", "sistemico", "practica", 0.4, "Que la escuela sea también el lugar de reunión de la junta de acción comunal muestra que su cierre afectaría",
  ["también la organización de la comunidad, no solo la educación.", "únicamente a los siete estudiantes.", "solamente a la secretaría de educación.", "el transporte escolar de otros municipios."], "A",
  "La escuela cumple más de una función en la vereda: cerrarla tendría efectos en la vida comunitaria.", ["¿Qué otra función cumple la escuela, además de la educación?"], ctx=S2)
I("SOC-144", "SOC", "sistemico", "practica", 0.7, "¿Qué alternativa atiende a la vez la preocupación por los costos y la de las familias?",
  ["Mantener la escuela abierta y que reciba también a los niños de una vereda vecina.", "Cerrar la escuela sin ofrecer transporte.", "Trasladar a la docente a la ciudad.", "Cobrar matrícula a las familias para pagar la escuela."], "A",
  "Si la escuela recibe más estudiantes, el costo por estudiante baja y los niños no tienen que caminar una hora.", ["Busca la opción que mejora el costo sin alejar a los niños."], ctx=S2)

S3 = ("Fuentes creadas para este ejercicio.\nFuente 1. Acta del cabildo de una villa, 1790: «Se fundó este pueblo en tierras baldías, por orden del "
      "gobernador, para reunir a los vecinos dispersos y que tuviesen iglesia y justicia».\nFuente 2. Relato recogido en 2015 a un mayor de la "
      "comunidad indígena de la región: «Nuestros abuelos contaban que allí ya vivían familias que sembraban maíz, y que las hicieron irse montaña "
      "arriba cuando llegaron los fundadores».")
I("SOC-145", "SOC", "perspectivas", "practica", -0.3, "¿En qué punto contradice la fuente 2 a la fuente 1?",
  ["En que las tierras donde se fundó el pueblo estaban deshabitadas.", "En el año en que se fundó el pueblo.", "En que el pueblo tuvo iglesia.", "En el nombre del gobernador."], "A",
  "La fuente 1 habla de 'tierras baldías'; la fuente 2 dice que allí ya vivían familias que sembraban maíz.", ["Busca en la fuente 1 cómo describe las tierras."], ctx=S3)
I("SOC-146", "SOC", "perspectivas", "practica", 0.4, "¿Por qué la fuente 1 podría no mencionar a las familias que ya vivían allí?",
  ["Porque la escribieron las autoridades que fundaron el pueblo y presenta su punto de vista.", "Porque en esa época las actas no se escribían.",
   "Porque las familias indígenas no sembraban.", "Porque la fuente 2 es más antigua."], "A",
  "Toda fuente tiene un autor con un punto de vista. Un acta oficial de la fundación difícilmente registraría que se desplazó a quienes vivían allí.", ["¿Quién escribió la fuente 1 y qué interés podía tener?"], ctx=S3)
I("SOC-147", "SOC", "perspectivas", "practica", 0.6, "Al usar la fuente 2 hay que tener en cuenta que",
  ["es un testimonio oral transmitido por generaciones: conserva la memoria de un grupo, pero puede cambiar con el tiempo.", "es un documento oficial firmado por el gobernador.",
   "fue escrita el mismo año de la fundación.", "no tiene ningún valor como fuente histórica."], "A",
  "La tradición oral es una fuente valiosa, sobre todo para grupos que no dejaron documentos escritos, pero se transmite de boca en boca y puede transformarse.", ["¿Cómo llegó ese relato hasta 2015?"], ctx=S3)
I("SOC-148", "SOC", "perspectivas", "practica", 0.8, "Para reconstruir mejor lo que ocurrió, un historiador debería",
  ["contrastar ambas fuentes con otras evidencias, como registros de tierras o hallazgos arqueológicos.", "quedarse con la fuente oficial porque es la más confiable.",
   "descartar las dos porque se contradicen.", "preferir siempre la fuente más reciente."], "A",
  "Cuando las fuentes se contradicen, se buscan otras evidencias independientes. Ninguna fuente es confiable solo por ser oficial o por ser reciente.", ["¿Qué hacer cuando dos fuentes dicen cosas distintas?"], ctx=S3)

S4 = ("En un país, el gobierno mantiene el precio de la gasolina por debajo de lo que cuesta en el mercado internacional y paga la diferencia con "
      "dinero del presupuesto nacional. Un informe muestra que la mayor parte de ese dinero beneficia a quienes más gasolina consumen, es decir, a "
      "hogares con varios vehículos y a empresas. El gobierno propone subir el precio poco a poco y usar el dinero ahorrado en programas sociales. "
      "Los transportadores advierten que subirán los pasajes y el precio de los alimentos.")
I("SOC-149", "SOC", "sistemico", "practica", 0.0, "Según el informe, ¿por qué el subsidio no beneficia por igual a todos los hogares?",
  ["Porque recibe más quien más gasolina consume.", "Porque solo lo reciben los hogares sin vehículo.", "Porque el gobierno lo paga con impuestos a la gasolina.", "Porque el precio internacional es igual al nacional."], "A",
  "Como el subsidio se da por cada galón, quien más consume (hogares con varios vehículos, empresas) recibe más dinero.", ["¿De qué depende cuánto subsidio recibe alguien?"], ctx=S4)
I("SOC-150", "SOC", "sistemico", "practica", 0.3, "La advertencia de los transportadores se basa en que",
  ["el combustible es parte del costo de transportar personas y mercancías.", "los alimentos se producen con gasolina.", "los pasajes dependen del precio internacional del café.", "los programas sociales suben los precios."], "A",
  "Si sube el combustible, sube el costo de mover buses y camiones, y ese costo suele trasladarse a pasajes y alimentos.", ["¿Qué tienen en común un pasaje de bus y el precio de los alimentos en la tienda?"], ctx=S4)
I("SOC-151", "SOC", "sistemico", "practica", 0.5, "Un efecto del subsidio que el texto permite inferir es que",
  ["el Estado dispone de menos dinero para otros gastos.", "la gasolina se vuelve más cara.", "los hogares sin vehículo reciben la mayor parte.", "el país deja de comprar gasolina."], "A",
  "El subsidio se paga con dinero del presupuesto nacional; ese dinero no se puede usar en otra cosa, como los programas sociales que propone el gobierno.", ["¿De dónde sale el dinero para mantener el precio bajo?"], ctx=S4)
I("SOC-152", "SOC", "perspectivas", "practica", 0.8, "¿Qué medida respondería a la preocupación de los transportadores sin abandonar la propuesta del gobierno?",
  ["Subir el precio gradualmente y dar un apoyo focalizado al transporte público y al de alimentos.", "Congelar el precio de la gasolina para siempre.",
   "Subir todo el precio de una vez.", "Eliminar los programas sociales."], "A",
  "Combina el ajuste gradual que propone el gobierno con un alivio dirigido a quienes temen el mayor impacto.", ["Busca la opción que no deja a ninguna de las dos partes sin atender."], ctx=S4)

# =============================== CIENCIAS NATURALES ===============================
N1 = ("En un día caluroso, Ana sirve agua con hielo en un vaso de vidrio seco. A los pocos minutos, la parte de afuera del vaso está cubierta de "
      "gotitas, aunque el vaso no tiene ninguna grieta.")
I("NAT-128", "NAT", "explicacion", "practica", -0.2, "Las gotas que aparecen por fuera del vaso provienen de",
  ["el vapor de agua del aire, que se condensa al enfriarse contra el vaso.", "el agua del interior, que atraviesa el vidrio.", "el hielo, que se derrite por fuera.", "una reacción química del vidrio con el frío."], "A",
  "El aire contiene vapor de agua. Al tocar la superficie fría del vaso, se enfría y pasa a estado líquido: es condensación.", ["El vaso no tiene grietas: el agua de adentro no puede salir.", "¿Qué contiene el aire, aunque no se vea?"], ctx=N1, componente="Químico")
I("NAT-129", "NAT", "explicacion", "practica", 0.4, "Si se hace lo mismo en un lugar con aire muy seco, se espera que",
  ["se formen menos gotas, porque hay menos vapor de agua en el aire.", "se formen más gotas, porque el aire seco es más frío.", "se formen las mismas gotas.", "el vaso se rompa por el cambio de temperatura."], "A",
  "Las gotas vienen del vapor del aire: con menos humedad, hay menos vapor que condensar.", ["Recuerda de dónde vienen las gotas."], ctx=N1, componente="Químico")
I("NAT-130", "NAT", "explicacion", "practica", 0.3, "¿Cuál de estos fenómenos se explica de la misma manera?",
  ["El rocío que aparece sobre la hierba en las madrugadas frías.", "La ropa que se seca al sol.", "La sal que se disuelve en el agua.", "El agua que hierve más rápido con la olla tapada."], "A",
  "El rocío también es vapor de agua del aire que se condensa al tocar superficies frías.", ["Busca otro caso en el que el vapor del aire se vuelve líquido."], ctx=N1, componente="Químico")

N2 = ("Dos camisas iguales, igual de mojadas, se cuelgan al mismo tiempo: una al sol, en un lugar con viento, y otra a la sombra, en un cuarto "
      "cerrado. La que está al sol y al viento se seca mucho antes.")
I("NAT-131", "NAT", "explicacion", "practica", -0.4, "El agua desaparece de las camisas porque",
  ["se evapora: pasa de líquido a vapor y se mezcla con el aire.", "la tela la convierte en aire.", "se filtra hacia el suelo.", "el sol la descompone en sal y oxígeno."], "A",
  "Secarse es evaporarse: el agua pasa a vapor y queda en el aire.", ["¿A qué estado pasa el agua cuando la ropa se seca?"], ctx=N2, componente="Químico")
I("NAT-132", "NAT", "explicacion", "practica", 0.2, "El sol acelera el secado porque",
  ["aporta energía que aumenta la evaporación.", "aumenta la humedad del aire.", "atrae el agua hacia arriba con su fuerza.", "hace que el agua se vuelva más pesada."], "A",
  "La evaporación necesita energía; el sol calienta la tela y el agua, y las moléculas escapan más rápido al aire.", ["¿Qué recibe la camisa del sol?"], ctx=N2, componente="Físico")
I("NAT-133", "NAT", "explicacion", "practica", 0.6, "El viento también acelera el secado porque",
  ["se lleva el aire húmedo que rodea la camisa y lo reemplaza por aire más seco.", "enfría la camisa y eso evapora más agua.", "empuja las gotas fuera de la tela.", "tiene menos oxígeno que el aire quieto."], "A",
  "Junto a la tela mojada el aire se carga de vapor y la evaporación se frena. El viento renueva ese aire y la evaporación sigue.", ["¿Qué le pasa al aire que está pegado a la tela mojada si no se mueve?"], ctx=N2, componente="Físico")

N3 = ("Para hacer pan se mezclan harina, agua, azúcar y levadura, y se deja reposar la masa. En una cocina tibia, la masa dobla su tamaño en una "
      "hora; dentro de la nevera, apenas crece. Al hornear el pan, se ven pequeños huecos en su interior.")
I("NAT-134", "NAT", "explicacion", "practica", 0.0, "La masa crece porque",
  ["la levadura, que es un ser vivo, consume azúcares y libera dióxido de carbono que queda atrapado en la masa.", "el agua se evapora y empuja la harina.",
   "la harina absorbe el aire de la cocina.", "el azúcar se expande con el calor."], "A",
  "La levadura es un hongo microscópico. Al alimentarse de azúcares produce dióxido de carbono; las burbujas de gas inflan la masa y dejan los huecos del pan.", ["La levadura está viva: ¿qué produce al alimentarse?"], ctx=N3, componente="Biológico")
I("NAT-135", "NAT", "explicacion", "practica", 0.4, "Dentro de la nevera la masa casi no crece porque",
  ["a baja temperatura la actividad de la levadura se vuelve muy lenta.", "en la nevera no hay aire.", "el azúcar se congela.", "el frío convierte el dióxido de carbono en agua."], "A",
  "Los procesos de los seres vivos dependen de la temperatura: con frío, la levadura trabaja muy despacio y produce poco gas.", ["Compara la temperatura de la cocina con la de la nevera."], ctx=N3, componente="Biológico")
I("NAT-136", "NAT", "explicacion", "practica", 0.3, "Si se prepara la misma masa sin levadura, se espera que",
  ["no crezca, porque no hay nada que produzca el gas.", "crezca más rápido.", "crezca igual, porque el azúcar produce el gas.", "se convierta en levadura con el tiempo."], "A",
  "Sin levadura no hay ser vivo que fermente el azúcar ni gas que infle la masa.", ["¿Quién produce el gas en la masa?"], ctx=N3, componente="Biológico")

# =============================== INGLÉS: LECTURA ===============================
E1 = ("Every Friday evening, the main street of San Pedro closes to cars and becomes a night market. Farmers from the villages sell cheese, fruit "
      "and coffee, and families from the town sell arepas and hot chocolate. Students from the music school play on a small stage. The market "
      "started three years ago because the farmers wanted to sell directly to people, without paying intermediaries. Now it is also a meeting "
      "place: many people go there not to buy, but to see their friends. The only complaint comes from some neighbours, who say it is too noisy "
      "after ten o'clock.")
I("ING-121", "ING", "lectura", "practica", -0.8, "What happens to the main street on Friday evenings?",
  ["It closes to cars.", "It becomes a car park.", "It is cleaned by the farmers.", "Farmers drive their trucks there."], "A",
  "'The main street of San Pedro closes to cars and becomes a night market'.", ["Lee la primera oración."], ctx=E1)
I("ING-122", "ING", "lectura", "practica", -0.2, "Why did the market start?",
  ["The farmers wanted to sell directly to people.", "The music school needed a stage.", "The neighbours asked for it.", "There were no shops in the town."], "A",
  "'The market started three years ago because the farmers wanted to sell directly to people'.", ["Busca la palabra 'because'."], ctx=E1)
I("ING-123", "ING", "lectura", "practica", 0.4, "Many people go 'not to buy, but to see their friends'. This shows that the market",
  ["is also a social meeting place.", "does not sell good products.", "is too expensive.", "is only for farmers."], "A",
  "La oración anterior lo dice: 'Now it is also a meeting place'.", ["¿Qué hacen esas personas en el mercado si no compran?"], ctx=E1)
I("ING-124", "ING", "lectura", "practica", 0.1, "What problem does the text mention?",
  ["Some neighbours think it is too noisy late at night.", "The farmers do not earn enough money.", "There is not enough food.", "The students do not want to play."], "A",
  "'The only complaint comes from some neighbours, who say it is too noisy after ten o'clock'.", ["Busca la palabra 'complaint' (queja)."], ctx=E1)

E2 = ("Dear Mr. Ramírez,\nI saw your notice asking for volunteers at the town library. I am in eleventh grade, and I would like to help on Saturday "
      "mornings, because I study during the week. I can organise books, help children with their homework and read stories to the younger ones. "
      "Last year I helped my aunt teach adults to read, so I have some experience. I don't have a computer at home, but I learn quickly and I would "
      "like to learn how the library's system works.\nYours sincerely,\nNatalia Ruiz")
I("ING-125", "ING", "lectura", "practica", -0.7, "Why is Natalia writing?",
  ["To offer to work as a volunteer at the library.", "To ask for a book.", "To complain about the library.", "To invite Mr. Ramírez to her school."], "A",
  "Ella responde a un aviso que pedía voluntarios y ofrece su ayuda.", ["Lee la primera oración de la carta."], ctx=E2)
I("ING-126", "ING", "lectura", "practica", -0.3, "Why can she only help on Saturdays?",
  ["Because she studies during the week.", "Because the library is closed on weekdays.", "Because she works with her aunt.", "Because she has no computer."], "A",
  "'I would like to help on Saturday mornings, because I study during the week'.", ["Busca la palabra 'because'."], ctx=E2)
I("ING-127", "ING", "lectura", "practica", 0.0, "What experience does she mention?",
  ["She helped her aunt teach adults to read.", "She worked in a library before.", "She studied computer science.", "She organised a book fair."], "A",
  "'Last year I helped my aunt teach adults to read, so I have some experience'.", ["Busca la palabra 'experience'."], ctx=E2)
I("ING-128", "ING", "lectura", "practica", 0.6, "What can we infer about Natalia?",
  ["She is willing to learn things she does not know yet.", "She is a professional librarian.", "She has worked with computers for years.", "She does not like working with children."], "A",
  "Reconoce que no tiene computador en casa, pero dice que aprende rápido y quiere aprender el sistema de la biblioteca.", ["Lee la última oración antes de la despedida."], ctx=E2)
