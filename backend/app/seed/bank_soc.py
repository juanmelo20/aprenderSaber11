"""Más preguntas ORIGINALES de Sociales y Ciudadanas. Las referencias normativas son a la Constitución
Política de Colombia de 1991 y a la Ley 134 de 1994 (mecanismos de participación). Entran en borrador."""
from __future__ import annotations

from .bank_seed import I

C1 = ("En un municipio, un grupo de ciudadanos considera que el alcalde no ha cumplido el programa de gobierno con el que fue elegido. "
      "Lleva más de un año en el cargo y las obras prometidas no han empezado. Los ciudadanos quieren usar un mecanismo de participación "
      "previsto en la Constitución para que los votantes decidan si el alcalde continúa.")
I("SOC-101", "SOC", "pensamiento_social", "practica", -0.4, "¿Cuál mecanismo de participación corresponde a lo que buscan estos ciudadanos?",
  ["El cabildo abierto.", "La revocatoria del mandato.", "La acción de tutela.", "El referendo."], "B",
  "La revocatoria del mandato permite a los ciudadanos dar por terminado el mandato de un alcalde o gobernador. Se relaciona con el voto programático: quien elige impone como mandato el programa de gobierno.",
  ["Buscan que el alcalde deje el cargo antes de terminar su periodo.", "Es un mecanismo que solo aplica a alcaldes y gobernadores."], ctx=C1)
I("SOC-102", "SOC", "pensamiento_social", "diagnostico", 0.2, "Si los ciudadanos quisieran, en cambio, discutir directamente con el concejo municipal el atraso de las obras, el mecanismo adecuado sería",
  ["la consulta popular.", "el plebiscito.", "el cabildo abierto.", "la iniciativa legislativa."], "C",
  "El cabildo abierto es una reunión pública del concejo (o de la junta administradora local) en la que los habitantes participan directamente para discutir asuntos de interés de la comunidad.",
  ["Se trata de una reunión pública para discutir, no de una votación."], ctx=C1)
I("SOC-103", "SOC", "sistemico", "practica", 0.5, "Un efecto positivo de que exista un mecanismo como el que buscan los ciudadanos es que",
  ["los gobernantes tienen un incentivo para cumplir lo que prometieron en campaña.", "los alcaldes pueden ser cambiados cada vez que pierden popularidad en una encuesta.", "los ciudadanos ya no necesitan votar en las elecciones.", "el concejo municipal deja de ser necesario."], "A",
  "Saber que el mandato puede revocarse por incumplir el programa presiona al gobernante a cumplirlo. No reemplaza las elecciones ni a otras instituciones.",
  ["Piensa en cómo cambia el comportamiento de un gobernante que sabe que puede ser revocado."], ctx=C1)
I("SOC-104", "SOC", "perspectivas", "practica", 0.6, "El alcalde responde que las obras se atrasaron porque el departamento no giró los recursos. Para evaluar esta explicación, lo más pertinente sería",
  ["aceptarla, porque el alcalde conoce mejor la administración.", "rechazarla, porque los políticos siempre se excusan.", "consultar documentos oficiales sobre el giro de los recursos y la versión del departamento.", "preguntar a los amigos del alcalde."], "C",
  "Una explicación se evalúa contrastándola con otras fuentes y con evidencia, no aceptándola o rechazándola por quién la dice.",
  ["¿Qué fuente permitiría comprobar si los recursos llegaron o no?"], ctx=C1)

C2 = ("A una señora de 70 años su entidad de salud le niega un medicamento que su médico tratante ordenó y que ella necesita para seguir viviendo. "
      "Ha presentado dos solicitudes por escrito y no ha recibido respuesta. No tiene dinero para pagar un abogado.")
I("SOC-105", "SOC", "pensamiento_social", "practica", -0.6, "¿Qué mecanismo constitucional puede usar la señora para pedir la protección inmediata de sus derechos?",
  ["La acción de tutela.", "La revocatoria del mandato.", "El referendo.", "La consulta popular."], "A",
  "La acción de tutela (artículo 86 de la Constitución) protege los derechos fundamentales cuando son vulnerados o amenazados. Aquí están en juego la salud y la vida.",
  ["Se necesita un mecanismo rápido para proteger derechos fundamentales de una persona."], ctx=C2)
I("SOC-106", "SOC", "pensamiento_social", "diagnostico", 0.1, "Que la señora no pueda pagar un abogado",
  ["le impide usar ese mecanismo.", "no le impide usarlo, porque cualquier persona puede presentarlo por sí misma.", "la obliga a esperar a que un abogado del Estado la busque.", "solo le permite acudir a la alcaldía."], "B",
  "La Constitución establece que toda persona puede reclamar ante los jueces, por sí misma o por quien actúe a su nombre, la protección de sus derechos fundamentales. No se exige abogado.",
  ["La tutela fue pensada para que fuera sencilla y al alcance de cualquier persona."], ctx=C2)
I("SOC-107", "SOC", "sistemico", "practica", 0.5, "La Constitución ordena que este mecanismo se resuelva en un plazo máximo de diez días. La razón principal de un plazo tan corto es que",
  ["los jueces tienen poco trabajo.", "la protección de un derecho fundamental pierde sentido si llega tarde.", "así se ahorra dinero al Estado.", "las entidades de salud lo solicitaron."], "B",
  "Cuando está en riesgo un derecho como la vida o la salud, una decisión tardía puede ser inútil. Por eso el trámite es preferente y sumario.",
  ["¿Qué pasaría con la señora si la decisión tardara dos años?"], ctx=C2)
I("SOC-108", "SOC", "perspectivas", "practica", 0.7, "La entidad de salud argumenta que el medicamento es muy costoso y que pagarlo afecta los recursos para otros pacientes. Este argumento",
  ["muestra un interés real (cuidar recursos limitados) que debe ponderarse, pero no elimina el deber de proteger la vida de la paciente.", "demuestra que la señora no tiene derecho al medicamento.", "es irrelevante, porque el dinero nunca importa.", "prueba que el médico tratante se equivocó."], "A",
  "En un conflicto hay intereses de varias partes. Reconocer el de la entidad no significa que prevalezca sobre el derecho a la vida; el juez debe ponderarlos.",
  ["Reconocer un interés no es lo mismo que darle la razón.", "Descarta las opciones que ignoran por completo a una de las partes."], ctx=C2)

C3 = ("El presidente de un país con una organización del Estado como la de Colombia anuncia que, para ganar tiempo, él mismo cambiará una ley "
      "aprobada por el Congreso, sin que este la discuta. Dice que tiene el respaldo de la mayoría de los ciudadanos.")
I("SOC-109", "SOC", "pensamiento_social", "practica", -0.3, "¿Por qué el anuncio del presidente es contrario a la organización del Estado?",
  ["Porque hacer y reformar las leyes le corresponde al Congreso, no al presidente.", "Porque el presidente no puede opinar sobre las leyes.", "Porque las leyes no se pueden cambiar nunca.", "Porque solo los jueces pueden cambiar las leyes."], "A",
  "En la separación de poderes, la rama legislativa (el Congreso) hace las leyes; la ejecutiva las ejecuta y la judicial resuelve conflictos conforme a ellas.",
  ["Recuerda las tres ramas del poder público y qué hace cada una."], ctx=C3)
I("SOC-110", "SOC", "sistemico", "diagnostico", 0.4, "La separación de poderes existe principalmente para",
  ["que el gobierno trabaje más despacio.", "evitar que una sola persona o grupo concentre todo el poder y abuse de él.", "que haya más cargos públicos.", "que los ciudadanos no tengan que participar."], "B",
  "Dividir el poder en ramas que se controlan entre sí es una garantía contra el abuso: ninguna puede decidirlo todo sola.",
  ["¿Qué riesgo habría si quien hace las leyes fuera el mismo que las aplica y que juzga?"], ctx=C3)
I("SOC-111", "SOC", "perspectivas", "practica", 0.8, "El presidente justifica su decisión en que 'la mayoría lo respalda'. La debilidad de este argumento es que",
  ["las mayorías nunca tienen la razón.", "en un Estado de derecho, el apoyo popular no autoriza a un gobernante a saltarse las reglas que limitan su poder.", "el presidente no fue elegido por la mayoría.", "las encuestas siempre se equivocan."], "B",
  "La legitimidad de origen (haber sido elegido) no elimina los límites constitucionales. Las reglas protegen también a las minorías frente a las mayorías.",
  ["¿Las reglas del Estado dejan de valer cuando alguien es popular?"], ctx=C3)
I("SOC-112", "SOC", "pensamiento_social", "practica", 0.3, "Si el presidente insistiera y expidiera una norma contraria a la Constitución, la institución encargada de proteger la integridad de la Constitución es",
  ["la Registraduría Nacional.", "la Corte Constitucional.", "la Policía Nacional.", "el Banco de la República."], "B",
  "A la Corte Constitucional se le confía la guarda de la integridad y supremacía de la Constitución: decide si las normas se ajustan a ella.",
  ["Su nombre indica cuál es la norma que protege."], ctx=C3)

C4 = ("En una región, los arroceros toman agua del río para regar sus cultivos durante el verano. Aguas abajo, el acueducto de un pueblo capta del "
      "mismo río. En los meses secos, el caudal no alcanza para todos: el pueblo sufre cortes de agua y los arroceros dicen que, sin riego, "
      "pierden la cosecha de la que viven cientos de familias. La autoridad ambiental debe decidir cómo repartir el agua.")
I("SOC-113", "SOC", "perspectivas", "practica", -0.5, "¿Cuál es el interés principal de los arroceros en este conflicto?",
  ["Que el pueblo se quede sin agua.", "Asegurar el riego para no perder la cosecha y sus ingresos.", "Que la autoridad ambiental desaparezca.", "Vender el agua del río."], "B",
  "Su interés es económico y de subsistencia: sin riego pierden la cosecha. Eso no implica que quieran perjudicar al pueblo.",
  ["Distingue lo que un grupo necesita de lo que su acción causa a otros."], ctx=C4)
I("SOC-114", "SOC", "perspectivas", "diagnostico", 0.3, "Los habitantes del pueblo y los arroceros coinciden en que",
  ["el arroz no debería cultivarse.", "ambos dependen del mismo río y el agua no alcanza en verano.", "la autoridad ambiental favorece a los arroceros.", "el consumo humano no es importante."], "B",
  "Aunque sus intereses chocan, comparten el diagnóstico: el río es su fuente común y en los meses secos el caudal es insuficiente.",
  ["Busca un hecho que ninguna de las dos partes negaría."], ctx=C4)
I("SOC-115", "SOC", "sistemico", "practica", 0.6, "Una solución que solo ordene cerrar las tomas de los arroceros durante el verano tendría como efecto probable",
  ["resolver el problema sin perjudicar a nadie.", "garantizar agua al pueblo, pero afectar el empleo y los ingresos de las familias arroceras.", "aumentar el caudal del río todo el año.", "reducir el consumo de agua en el pueblo."], "B",
  "Toda medida tiene efectos en varias dimensiones: protege el consumo humano, pero traslada el costo a quienes viven del cultivo.",
  ["Pregúntate a quién beneficia y a quién perjudica la medida."], ctx=C4)
I("SOC-116", "SOC", "sistemico", "practica", 0.8, "¿Cuál de estas medidas atiende mejor los intereses de las dos partes?",
  ["Prohibir el cultivo de arroz en la región.", "Dejar que cada quien tome el agua que pueda.", "Dar prioridad al consumo humano y, a la vez, apoyar a los arroceros con riego más eficiente y turnos de uso.", "Suspender el acueducto en verano."], "C",
  "Combina la prioridad del consumo humano con acciones que reducen el daño a los productores. Las demás sacrifican por completo a una parte.",
  ["La mejor opción es la que no deja a un grupo sin nada."], ctx=C4)

C5 = ("Sobre una huelga en una empresa de transporte circulan dos textos. El comunicado de la empresa dice: «Un grupo minoritario de conductores "
      "paralizó el servicio y perjudicó a miles de usuarios; los salarios se pagan cumplidamente». El volante del sindicato dice: «La gran mayoría "
      "de los conductores paró porque llevamos dos meses sin recibir el pago de horas extras; la empresa se niega a dialogar».")
I("SOC-117", "SOC", "perspectivas", "practica", -0.2, "¿En qué punto se contradicen directamente las dos fuentes?",
  ["En que hubo una huelga.", "En cuántos conductores participaron y en si la empresa está al día con los pagos.", "En que la empresa es de transporte.", "En que los usuarios existen."], "B",
  "Una habla de 'grupo minoritario' y pagos cumplidos; la otra, de 'gran mayoría' y dos meses de deuda. En que hubo huelga sí coinciden.",
  ["Separa los hechos en los que coinciden de aquellos en los que dicen cosas opuestas."], ctx=C5)
I("SOC-118", "SOC", "perspectivas", "practica", 0.4, "Que cada texto resalte información distinta se explica mejor porque",
  ["una de las dos partes necesariamente miente en todo.", "cada parte tiene interés en presentar los hechos de la forma que más la favorece.", "los comunicados nunca contienen datos ciertos.", "los sindicatos y las empresas usan idiomas distintos."], "B",
  "Las fuentes tienen autores con intereses. La empresa destaca el daño a los usuarios; el sindicato, la deuda. Eso no prueba que todo sea falso, pero obliga a contrastar.",
  ["Pregúntate quién escribe cada texto y qué busca."], ctx=C5)
I("SOC-119", "SOC", "perspectivas", "diagnostico", 0.7, "Para saber cuál versión sobre los pagos es correcta, la fuente más útil sería",
  ["la opinión de un usuario molesto por el paro.", "los comprobantes de nómina de los últimos meses o un informe del Ministerio del Trabajo.", "otro comunicado de la empresa.", "un comentario anónimo en redes sociales."], "B",
  "Se necesita evidencia verificable o una fuente independiente de las dos partes. Repetir la versión de una de ellas no resuelve la contradicción.",
  ["¿Qué fuente no pertenece a ninguna de las dos partes o puede comprobarse?"], ctx=C5)
I("SOC-120", "SOC", "sistemico", "practica", 0.5, "Si el paro se prolonga varias semanas, ¿cuál efecto es más probable?",
  ["Solo se afecta la empresa.", "Se afectan los usuarios, los ingresos de los conductores y los de la empresa, lo que aumenta la presión para negociar.", "Los usuarios dejan de necesitar transporte.", "Los salarios aumentan automáticamente."], "B",
  "Un conflicto laboral prolongado tiene costos para todas las partes y para terceros; esos costos suelen empujar hacia la negociación.",
  ["Piensa en todos los grupos mencionados en el contexto."], ctx=C5)

C6 = ("Un municipio turístico prohíbe la entrega de bolsas y pitillos plásticos de un solo uso. Los comerciantes pequeños se quejan de que los "
      "empaques alternativos cuestan el triple. Los pescadores apoyan la medida porque el plástico daña sus redes y reduce la pesca. Una "
      "fábrica local de bolsas anuncia que despedirá a parte de sus trabajadores.")
I("SOC-121", "SOC", "sistemico", "practica", -0.3, "¿Cuál afirmación describe mejor los efectos de la medida?",
  ["Solo tiene efectos ambientales.", "Tiene efectos ambientales, económicos y sociales, positivos para unos grupos y negativos para otros.", "No tiene ningún efecto.", "Perjudica a todos los habitantes por igual."], "B",
  "El contexto muestra varias dimensiones: beneficio ambiental y para la pesca, costos para comerciantes, pérdida de empleos en la fábrica.",
  ["Enumera qué le pasa a cada grupo mencionado."], ctx=C6)
I("SOC-122", "SOC", "perspectivas", "practica", 0.2, "Los pescadores apoyan la medida principalmente por una razón",
  ["económica: el plástico afecta su actividad y sus ingresos.", "política: quieren apoyar al alcalde.", "religiosa.", "estética: les parece feo el plástico."], "A",
  "El texto dice que el plástico daña sus redes y reduce la pesca: su apoyo se relaciona con su sustento.",
  ["Lee qué les pasa a las redes y a la pesca."], ctx=C6)
I("SOC-123", "SOC", "sistemico", "practica", 0.7, "¿Cuál acción complementaria reduciría mejor los efectos negativos sin abandonar el objetivo ambiental?",
  ["Derogar la prohibición.", "Aplicar la medida por etapas y apoyar a comerciantes y a la fábrica para pasar a empaques reutilizables.", "Multar a los pescadores.", "Prohibir el turismo."], "B",
  "Una transición gradual con apoyo mantiene el objetivo y reparte mejor los costos. Derogar la medida abandona el objetivo.",
  ["Busca la opción que conserva la meta y atiende a los perjudicados."], ctx=C6)
I("SOC-124", "SOC", "pensamiento_social", "practica", 0.4, "El caso ilustra que las decisiones ambientales de un gobierno local",
  ["no deberían tener en cuenta la economía.", "suelen implicar tensiones entre la protección del ambiente y actividades económicas de las que vive la gente.", "siempre son rechazadas por toda la población.", "solo interesan a los turistas."], "B",
  "El concepto de desarrollo sostenible busca justamente equilibrar la protección ambiental con las necesidades económicas y sociales.",
  ["¿Qué dos cosas valiosas entran en tensión en el caso?"], ctx=C6)

C7 = ("La Constitución de 1991 define a Colombia como un Estado social de derecho y reconoce y protege la diversidad étnica y cultural de la nación. "
      "También establece que las lenguas de los grupos étnicos son oficiales en sus territorios, junto con el castellano.")
I("SOC-125", "SOC", "pensamiento_social", "practica", -0.4, "Una consecuencia de que las lenguas de los grupos étnicos sean oficiales en sus territorios es que",
  ["el castellano deja de ser idioma oficial del país.", "en esos territorios la enseñanza puede y debe tener en cuenta la lengua propia de la comunidad.", "todos los colombianos deben aprender esas lenguas.", "esas comunidades no pueden usar el castellano."], "B",
  "El reconocimiento oficial obliga al Estado a respetar y usar esas lenguas en sus territorios; la Constitución prevé educación bilingüe para las comunidades con tradición lingüística propia.",
  ["Fíjate en las palabras 'en sus territorios' y 'junto con el castellano'."], ctx=C7)
I("SOC-126", "SOC", "pensamiento_social", "diagnostico", 0.5, "Que Colombia sea un 'Estado social de derecho' significa, entre otras cosas, que el Estado",
  ["solo debe castigar los delitos.", "debe respetar la ley y, además, procurar condiciones de vida dignas para la población.", "puede actuar sin límites si busca el bien común.", "no interviene en salud ni en educación."], "B",
  "'De derecho' significa que el Estado está sometido a normas; 'social' añade el deber de garantizar derechos como salud, educación y trabajo para hacer real la dignidad humana.",
  ["La expresión tiene dos partes: 'social' y 'de derecho'."], ctx=C7)
I("SOC-127", "SOC", "perspectivas", "practica", 0.6, "Una empresa quiere construir una obra en el territorio de una comunidad indígena. La comunidad pide ser consultada antes. Su petición se apoya en la idea de que",
  ["las comunidades étnicas tienen derecho a participar en las decisiones que afectan su territorio y su cultura.", "ninguna empresa puede trabajar en Colombia.", "las obras siempre son dañinas.", "la comunidad es dueña de todo el departamento."], "A",
  "Proteger la diversidad étnica y cultural incluye que esas comunidades participen en decisiones que pueden afectar su modo de vida.",
  ["Relaciona la petición con lo que la Constitución 'reconoce y protege'."], ctx=C7)
I("SOC-128", "SOC", "sistemico", "practica", 0.7, "Antes de 1991, la Constitución vigente no reconocía la diversidad étnica de esta manera. El cambio tuvo como efecto que",
  ["desaparecieran las diferencias culturales.", "los grupos étnicos contaran con bases jurídicas para reclamar sus derechos colectivos.", "se prohibiera el castellano en algunas regiones.", "los grupos étnicos dejaran de ser ciudadanos colombianos."], "B",
  "El reconocimiento constitucional da fundamento a derechos como la educación propia, el territorio y la participación, que pueden exigirse ante el Estado.",
  ["¿Qué permite hacer una norma que reconoce un derecho?"], ctx=C7)

C8 = ("Una sequía prolongada redujo a la mitad la cosecha de papa en la principal zona productora del país. Semanas después, el precio de la papa "
      "en las plazas de mercado subió con fuerza. Algunos consumidores acusaron a los vendedores de «especular».")
I("SOC-129", "SOC", "pensamiento_social", "practica", -0.5, "La explicación económica más directa del aumento del precio es que",
  ["los vendedores se pusieron de acuerdo para engañar.", "al disminuir la oferta y mantenerse la demanda, el precio tiende a subir.", "la papa mejoró de calidad.", "los consumidores dejaron de comprar papa."], "B",
  "Con menos producto disponible y compradores que siguen queriendo la misma cantidad, el precio sube: es el efecto de una caída de la oferta.",
  ["¿Qué cambió: la cantidad de papa disponible o las ganas de comprarla?"], ctx=C8)
I("SOC-130", "SOC", "sistemico", "practica", 0.4, "Si el precio de la papa sigue alto durante meses, es probable que",
  ["las familias de menores ingresos reemplacen la papa por otros alimentos más baratos.", "la sequía termine más rápido.", "todos los agricultores del país se enriquezcan.", "el precio de todos los alimentos baje."], "A",
  "Ante un alimento caro, muchos hogares lo sustituyen (yuca, plátano, arroz). Los agricultores que perdieron la cosecha no se benefician del precio alto.",
  ["Piensa en lo que hace una familia cuando un alimento sube mucho."], ctx=C8)
I("SOC-131", "SOC", "perspectivas", "practica", 0.6, "Para saber si hubo especulación o si el aumento se debe a la sequía, sería más útil",
  ["preguntarle a un consumidor enojado.", "comparar cuánta papa llegó a las plazas y cómo cambiaron los precios al productor y al consumidor.", "contar cuántos vendedores hay.", "revisar el precio de la papa hace diez años."], "B",
  "Si llegó mucha menos papa y también subió el precio que recibe el productor, la causa es la escasez. Si solo subió el precio final, habría que investigar a los intermediarios.",
  ["Una acusación se comprueba con datos, no con el enojo de quien acusa."], ctx=C8)
I("SOC-132", "SOC", "sistemico", "practica", 0.8, "El gobierno estudia fijar por decreto un precio máximo muy bajo para la papa. Un riesgo de esa medida es que",
  ["llueva menos.", "a los productores no les resulte rentable llevarla al mercado y haya aún menos papa disponible.", "los consumidores compren menos.", "suba el precio del arroz de inmediato en todo el mundo."], "B",
  "Un precio máximo por debajo del costo desanima la oferta: puede aliviar el bolsillo por unos días y agravar la escasez después.",
  ["¿Qué haría un productor si le obligan a vender por menos de lo que le costó?"], ctx=C8)

C9 = ("El manual de convivencia de un colegio prohíbe a los estudiantes llevar el cabello largo o teñido. Un estudiante de grado once sostiene que la "
      "norma vulnera su derecho al libre desarrollo de la personalidad. El rector responde que el manual fue aprobado por el consejo directivo y "
      "que las normas del colegio se deben cumplir.")
I("SOC-133", "SOC", "pensamiento_social", "practica", 0.0, "¿Cuál principio permite resolver la tensión entre el manual y el derecho que invoca el estudiante?",
  ["El manual de convivencia está por encima de la Constitución dentro del colegio.", "Las normas de un colegio deben ajustarse a la Constitución y no pueden desconocer derechos fundamentales.", "Los estudiantes no tienen derechos mientras sean menores de edad.", "El rector decide libremente qué derechos se aplican."], "B",
  "La Constitución es norma de normas. Un manual de convivencia es válido, pero dentro de los límites que ella fija.",
  ["¿Cuál norma tiene mayor jerarquía en el país?"], ctx=C9)
I("SOC-134", "SOC", "perspectivas", "diagnostico", 0.4, "El argumento del rector se basa en",
  ["la autoridad del órgano que aprobó la norma y el deber de cumplirla.", "estudios sobre el efecto del cabello largo en el aprendizaje.", "la opinión de los estudiantes.", "una orden de un juez."], "A",
  "El rector no explica por qué la norma es necesaria: apela a que fue aprobada por el consejo directivo y a que las normas se cumplen.",
  ["¿El rector da razones sobre el contenido de la norma o sobre quién la aprobó?"], ctx=C9)
I("SOC-135", "SOC", "pensamiento_social", "practica", 0.3, "¿Qué figura del gobierno escolar tiene entre sus funciones promover el ejercicio de los derechos de los estudiantes y podría acompañar este reclamo?",
  ["El personero estudiantil.", "El tesorero de la asociación de padres.", "El celador.", "El secretario de educación departamental."], "A",
  "El personero es un estudiante del último grado, elegido por sus compañeros, encargado de promover el ejercicio de los derechos y deberes de los estudiantes.",
  ["Es un estudiante elegido por votación cada año."], ctx=C9)
I("SOC-136", "SOC", "sistemico", "practica", 0.7, "Una forma de resolver el conflicto que fortalece la convivencia democrática en el colegio sería",
  ["sancionar al estudiante para dar ejemplo.", "que el estudiante ignore el manual sin decir nada.", "revisar la norma con participación de estudiantes, docentes y familias, a la luz de los derechos constitucionales.", "eliminar el manual de convivencia."], "C",
  "La participación de la comunidad educativa en la revisión de las normas permite ajustarlas a los derechos sin renunciar a tener reglas.",
  ["Busca la salida que no impone ni desobedece, sino que discute la regla."], ctx=C9)
