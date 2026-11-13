"""Más preguntas ORIGINALES de Ciencias Naturales (explicación de fenómenos, sobre todo) y de lectura en Inglés.
Entran en borrador."""
from __future__ import annotations

from .bank_seed import I

# =============================== CIENCIAS NATURALES ===============================
N1 = ("Una estudiante pone una planta acuática en dos frascos con agua, bien tapados. Deja el frasco 1 junto a una ventana con buena luz y el "
      "frasco 2 dentro de un armario oscuro. Después de varias horas, en el frasco 1 se ven burbujas saliendo de las hojas; en el frasco 2, no.")
I("NAT-101", "NAT", "explicacion", "practica", -0.4, "Las burbujas del frasco 1 son principalmente de",
  ["dióxido de carbono producido por la respiración.", "oxígeno producido por la fotosíntesis.", "vapor de agua por el calor de la ventana.", "nitrógeno que la planta toma del agua."], "B",
  "Con luz, la planta hace fotosíntesis: usa dióxido de carbono y agua y libera oxígeno, que se ve como burbujas.", ["¿Qué proceso de la planta necesita luz?", "Ese proceso libera un gas."], ctx=N1, componente="Biológico")
I("NAT-102", "NAT", "explicacion", "diagnostico", 0.3, "¿Por qué en el frasco 2 no se observan burbujas?",
  ["Porque sin luz la planta no realiza fotosíntesis.", "Porque en la oscuridad la planta deja de respirar.", "Porque el agua del armario no tiene gases.", "Porque la planta muere a los pocos minutos sin luz."], "A",
  "La fotosíntesis depende de la luz. En la oscuridad la planta sigue viva y respirando, pero no produce oxígeno.", ["La única diferencia entre los frascos es la luz.", "Respirar y hacer fotosíntesis no son lo mismo."], ctx=N1, componente="Biológico")
I("NAT-103", "NAT", "indagacion", "practica", 0.2, "Para que la comparación entre los dos frascos sea válida, la estudiante debe asegurarse de que",
  ["las dos plantas sean del mismo tipo y tamaño, y los frascos tengan la misma cantidad de agua.", "el frasco 1 tenga más agua, porque recibe más luz.", "cada frasco tenga una planta de especie diferente.", "el frasco 2 se abra cada hora para revisar."], "A",
  "Solo debe cambiar la luz. Si también cambian la planta o el agua, no se sabría a qué se debe la diferencia.", ["¿Cuál es la única condición que debe ser distinta entre los frascos?"], ctx=N1, componente="Indagación")

N2 = ("En una finca se usó durante años el mismo insecticida contra una plaga. Al principio moría casi toda la plaga con cada aplicación. Con el "
      "tiempo, la misma dosis mataba cada vez menos insectos, hasta que dejó de ser útil.")
I("NAT-104", "NAT", "explicacion", "practica", 0.4, "La explicación más aceptada de este fenómeno es que",
  ["cada insecto se fue acostumbrando al veneno durante su vida.", "algunos insectos ya eran resistentes; sobrevivieron, se reprodujeron y sus descendientes heredaron la resistencia.", "el insecticida perdió su fórmula con los años.", "los insectos aprendieron a esconderse y enseñaron a sus crías."], "B",
  "Es selección natural: la variación ya existía en la población. El insecticida eliminó a los sensibles y dejó a los resistentes, que se multiplicaron.", ["La resistencia no aparece porque el insecto 'la necesite'.", "Piensa en cuáles insectos dejaron descendencia."], ctx=N2, componente="Biológico")
I("NAT-105", "NAT", "explicacion", "diagnostico", 0.7, "¿Cuál condición es indispensable para que ocurra lo descrito?",
  ["Que todos los insectos de la plaga fueran genéticamente idénticos.", "Que existieran diferencias heredables entre los insectos de la plaga.", "Que el insecticida se aplicara solo una vez.", "Que los insectos vivieran muchos años."], "B",
  "Sin variación heredable no hay nada que seleccionar: si todos fueran iguales, todos morirían o todos sobrevivirían.", ["La selección actúa sobre diferencias entre individuos.", "Esas diferencias deben poder pasar a los hijos."], ctx=N2, componente="Biológico")
I("NAT-106", "NAT", "uso", "practica", 0.3, "Una práctica que ayuda a retrasar la aparición de resistencia en las plagas es",
  ["aumentar la dosis del mismo insecticida cada año.", "alternar productos y combinar otros métodos de control, como enemigos naturales de la plaga.", "aplicar el mismo insecticida con más frecuencia.", "dejar de vigilar el cultivo."], "B",
  "Usar siempre el mismo producto selecciona a los resistentes. Alternar y combinar métodos reduce esa presión.", ["¿Qué pasa si siempre se selecciona con el mismo veneno?"], ctx=N2, componente="Ciencia, tecnología y sociedad")

N3 = ("En una ciudad ubicada a nivel del mar, el agua de una olla destapada hierve a unos 100 °C. En una ciudad a 2.600 metros de altura, el agua "
      "hierve cerca de los 92 °C, y los fríjoles tardan más en ablandarse.")
I("NAT-107", "NAT", "explicacion", "practica", 0.3, "El agua hierve a menor temperatura en la ciudad alta porque allí",
  ["el aire es más frío.", "la presión atmosférica es menor.", "el agua contiene menos minerales.", "las estufas calientan menos."], "B",
  "A mayor altura hay menos aire encima y la presión atmosférica es menor; el agua necesita menos temperatura para hervir.", ["¿Qué cambia en la atmósfera al subir una montaña?", "El punto de ebullición depende de la presión."], ctx=N3, componente="Físico")
I("NAT-108", "NAT", "explicacion", "practica", 0.6, "Los fríjoles tardan más en ablandarse en la ciudad alta porque",
  ["el agua hirviendo está a menor temperatura y transfiere menos energía al alimento.", "el agua hierve más despacio.", "los fríjoles de clima frío son más duros.", "el agua se evapora menos."], "A",
  "Mientras hierve, el agua no pasa de su temperatura de ebullición: allí son unos 92 °C, no 100 °C, y la cocción es más lenta.", ["Mientras el agua hierve, ¿su temperatura sigue subiendo?", "Compara 92 °C con 100 °C."], ctx=N3, componente="Físico")
I("NAT-109", "NAT", "uso", "practica", 0.5, "Una olla a presión cocina más rápido los alimentos porque en su interior",
  ["la presión aumenta y el agua alcanza temperaturas superiores a su punto de ebullición normal.", "no hay agua.", "la presión disminuye y el agua hierve antes.", "el vapor enfría el alimento."], "A",
  "Al no dejar escapar el vapor, la presión sube; con más presión, el agua hierve a mayor temperatura y cocina más rápido.", ["Es el caso contrario al de la ciudad alta."], ctx=N3, componente="Ciencia, tecnología y sociedad")

N4 = ("Durante una tormenta, una persona ve un relámpago y cuenta seis segundos hasta escuchar el trueno. Más tarde ve otro relámpago y solo "
      "cuenta dos segundos.")
I("NAT-110", "NAT", "explicacion", "practica", -0.3, "El trueno se escucha después de ver el relámpago porque",
  ["el trueno se produce varios segundos después que el relámpago.", "la luz viaja muchísimo más rápido que el sonido.", "el sonido viaja más rápido que la luz, pero rebota en las nubes.", "el ojo es más lento que el oído."], "B",
  "Ambos se producen casi al mismo tiempo. La luz llega prácticamente al instante; el sonido viaja a unos 340 m/s en el aire.", ["Los dos fenómenos ocurren a la vez: lo distinto es cómo viajan."], ctx=N4, componente="Físico")
I("NAT-111", "NAT", "uso", "diagnostico", 0.2, "Si el sonido viaja en el aire a unos 340 m/s, ¿a qué distancia aproximada cayó el primer rayo?",
  ["A unos 57 metros.", "A unos 340 metros.", "A unos 2 kilómetros.", "A unos 20 kilómetros."], "C",
  "Distancia = rapidez × tiempo = 340 m/s × 6 s = 2.040 m, cerca de 2 kilómetros.", ["Multiplica la rapidez del sonido por los segundos contados."], ctx=N4, componente="Físico")
I("NAT-112", "NAT", "indagacion", "practica", 0.1, "A partir de las dos observaciones se puede concluir que la tormenta",
  ["se está alejando.", "se está acercando.", "no se mueve.", "ya terminó."], "B",
  "El tiempo entre luz y sonido pasó de seis a dos segundos: el segundo rayo cayó más cerca.", ["Menos tiempo entre el relámpago y el trueno significa menos distancia."], ctx=N4, componente="Indagación")

N5 = ("En una sabana, los zorros se alimentan de conejos y los conejos se alimentan de pasto. Los ganaderos de la zona eliminan a casi todos los "
      "zorros porque atacaban a las gallinas.")
I("NAT-113", "NAT", "explicacion", "practica", -0.2, "¿Qué es más probable que ocurra primero con la población de conejos?",
  ["Disminuye, porque los conejos necesitan a los zorros.", "Aumenta, porque tiene menos depredadores.", "Se mantiene igual.", "Desaparece de inmediato."], "B",
  "Con menos depredadores sobreviven más conejos y la población crece.", ["¿Qué limitaba el número de conejos?"], ctx=N5, componente="Biológico")
I("NAT-114", "NAT", "explicacion", "practica", 0.5, "Si la situación se mantiene por varios años, un efecto probable sobre el ecosistema es que",
  ["el pasto abunde más que antes.", "el pasto disminuya por exceso de conejos y luego falte alimento para ellos y para el ganado.", "los conejos empiecen a comer gallinas.", "nada cambie, porque los ecosistemas no dependen de sus depredadores."], "B",
  "Demasiados herbívoros consumen el pasto más rápido de lo que se recupera. El efecto de quitar un depredador se propaga por toda la cadena.", ["Sigue la cadena: zorros, conejos, pasto.", "¿Qué pasa con el pasto si hay muchos más conejos?"], ctx=N5, componente="Biológico")
I("NAT-115", "NAT", "uso", "practica", 0.3, "En esta cadena alimentaria, el pasto cumple el papel de",
  ["consumidor primario.", "productor.", "descomponedor.", "consumidor secundario."], "B",
  "Los productores fabrican su propio alimento mediante la fotosíntesis. Los conejos son consumidores primarios y los zorros, secundarios.", ["¿Quién fabrica su alimento a partir de la luz?"], ctx=N5, componente="Biológico")

N6 = ("Un clavo de hierro nuevo se deja varias semanas a la intemperie. Con el tiempo se cubre de una capa rojiza y quebradiza. Al pesarlo con una "
      "balanza muy precisa, el clavo oxidado tiene un poco más de masa que el clavo nuevo.")
I("NAT-116", "NAT", "explicacion", "practica", 0.1, "La capa rojiza se forma porque",
  ["el hierro se derrite con el sol.", "el hierro reacciona con el oxígeno del aire, en presencia de humedad, y forma una sustancia nueva.", "el polvo del ambiente se pega al clavo.", "el clavo pierde pintura."], "B",
  "Es un cambio químico: el hierro reacciona con el oxígeno (favorecido por el agua) y forma óxido de hierro, con propiedades distintas.", ["La capa tiene propiedades distintas a las del hierro: ¿es la misma sustancia?"], ctx=N6, componente="Químico")
I("NAT-117", "NAT", "explicacion", "diagnostico", 0.8, "¿Por qué el clavo oxidado tiene más masa que el clavo nuevo?",
  ["Porque al óxido se le suman los átomos de oxígeno que antes estaban en el aire.", "Porque el hierro crea materia al oxidarse.", "Porque la masa no se conserva en las reacciones químicas.", "Porque el clavo absorbe luz solar."], "A",
  "La masa se conserva: el óxido contiene el hierro del clavo más el oxígeno que se unió a él. Si se contara también ese oxígeno, la masa total antes y después sería igual.", ["En una reacción no se crea ni se destruye materia.", "¿De dónde vienen los átomos que ahora hacen parte de la capa?"], ctx=N6, componente="Químico")
I("NAT-118", "NAT", "uso", "practica", 0.0, "Pintar una reja de hierro ayuda a evitar que se oxide porque la pintura",
  ["hace más fuerte al hierro.", "impide el contacto del hierro con el oxígeno y la humedad.", "enfría el metal.", "convierte el hierro en otro metal."], "B",
  "Sin contacto con el oxígeno y el agua, la reacción no ocurre: la pintura actúa como barrera.", ["¿Qué necesita el hierro para oxidarse?"], ctx=N6, componente="Ciencia, tecnología y sociedad")

N7 = ("Un médico receta un antibiótico durante siete días para una infección causada por bacterias. Al tercer día el paciente se siente bien y "
      "deja de tomarlo. Dos semanas después la infección regresa y el mismo antibiótico ya no le hace efecto.")
I("NAT-119", "NAT", "explicacion", "practica", 0.5, "¿Qué explica mejor que el antibiótico ya no funcione?",
  ["El cuerpo del paciente se volvió inmune al antibiótico.", "Sobrevivieron las bacterias más resistentes, que se multiplicaron y formaron una población difícil de eliminar.", "El antibiótico se venció en esas dos semanas.", "Las bacterias se transformaron en virus."], "B",
  "Al suspender el tratamiento mueren primero las bacterias más sensibles; las más resistentes quedan y se reproducen. Quien se vuelve resistente es la población de bacterias, no la persona.", ["¿Cuáles bacterias seguían vivas al tercer día?", "Es el mismo proceso de selección que ocurre con las plagas y los insecticidas."], ctx=N7, componente="Biológico")
I("NAT-120", "NAT", "uso", "practica", -0.2, "Los antibióticos no sirven para tratar la gripa común porque",
  ["la gripa es causada por virus y los antibióticos actúan contra bacterias.", "la gripa no es una enfermedad.", "los antibióticos solo funcionan en niños.", "la gripa es causada por hongos."], "A",
  "Los antibióticos atacan estructuras propias de las bacterias. Los virus no las tienen.", ["¿Qué tipo de microorganismo causa la gripa?"], ctx=N7, componente="Ciencia, tecnología y sociedad")
I("NAT-121", "NAT", "indagacion", "practica", 0.6, "Para comprobar en el laboratorio si una bacteria es resistente a un antibiótico, el procedimiento más adecuado es",
  ["preguntarle al paciente cómo se siente.", "cultivar la bacteria en dos cajas iguales, una con el antibiótico y otra sin él, y comparar su crecimiento.", "cultivar la bacteria solo en una caja con antibiótico.", "observar la bacteria una sola vez al microscopio."], "B",
  "Se necesita un control sin antibiótico para saber si la bacteria crece normalmente; si también crece con el antibiótico, es resistente.", ["¿Con qué se compara el cultivo que tiene antibiótico?"], ctx=N7, componente="Indagación")

N8 = ("En una cocina, una cuchara de metal y una cuchara de madera se dejan dentro de una olla con sopa caliente. Después de unos minutos, el mango "
      "de la cuchara de metal quema al tocarlo; el de la cuchara de madera, no.")
I("NAT-122", "NAT", "explicacion", "practica", -0.5, "La diferencia se debe a que",
  ["el metal conduce el calor mucho mejor que la madera.", "la madera está más fría que la sopa.", "el metal produce calor por sí mismo.", "la madera absorbe el agua de la sopa."], "A",
  "En el metal la energía pasa con facilidad de una partícula a la siguiente hasta el mango; la madera es mal conductor (aislante).", ["Las dos cucharas están en la misma sopa: ¿qué es distinto entre ellas?"], ctx=N8, componente="Físico")
I("NAT-123", "NAT", "explicacion", "practica", 0.4, "El calor llega hasta el mango de la cuchara de metal principalmente por",
  ["radiación, como la luz del sol.", "conducción, de partícula a partícula a lo largo del metal.", "convección, por el movimiento del aire.", "evaporación de la sopa."], "B",
  "En los sólidos el calor se transmite por conducción: las partículas que vibran más pasan energía a sus vecinas.", ["La cuchara es un sólido: sus partículas no se desplazan de un extremo al otro."], ctx=N8, componente="Físico")
I("NAT-124", "NAT", "uso", "diagnostico", 0.0, "Por esa misma propiedad, los mangos de las ollas suelen fabricarse de",
  ["cobre, porque brilla.", "plástico resistente o madera, porque son malos conductores del calor.", "aluminio, porque es liviano.", "hierro, porque es duro."], "B",
  "Un mango debe aislar: se usan materiales que conducen poco el calor para poder agarrar la olla.", ["¿Quieres que el mango conduzca el calor o que no lo conduzca?"], ctx=N8, componente="Ciencia, tecnología y sociedad")

N9 = ("Un bus frena de repente. Los pasajeros que van de pie se van hacia adelante, aunque nadie los empuja.")
I("NAT-125", "NAT", "explicacion", "practica", 0.0, "Los pasajeros se van hacia adelante porque",
  ["el freno los empuja hacia adelante.", "sus cuerpos tienden a seguir moviéndose con la velocidad que llevaban.", "el aire dentro del bus los arrastra.", "la gravedad aumenta al frenar."], "B",
  "Es la inercia (primera ley de Newton): un cuerpo en movimiento sigue moviéndose igual mientras una fuerza no lo cambie. El bus frena; los pasajeros tienden a seguir.", ["Antes de frenar, ¿a qué velocidad iban los pasajeros?", "¿Sobre quién actúa directamente la fuerza de los frenos?"], ctx=N9, componente="Físico")
I("NAT-126", "NAT", "uso", "practica", -0.3, "El cinturón de seguridad protege en un frenazo porque",
  ["aumenta la velocidad del carro.", "ejerce sobre la persona la fuerza que la detiene junto con el vehículo.", "elimina la inercia del cuerpo.", "hace más liviana a la persona."], "B",
  "Para cambiar el movimiento del cuerpo se necesita una fuerza: el cinturón la aplica y evita que la persona siga hacia adelante.", ["Algo tiene que frenar al pasajero: si no es el cinturón, ¿qué será?"], ctx=N9, componente="Ciencia, tecnología y sociedad")
I("NAT-127", "NAT", "explicacion", "practica", 0.6, "Si el bus, en lugar de frenar, arranca bruscamente, los pasajeros de pie",
  ["se van hacia adelante, igual que al frenar.", "se van hacia atrás, porque sus cuerpos tienden a permanecer en reposo.", "no sienten nada.", "se elevan del piso."], "B",
  "También es inercia: estaban en reposo y tienden a seguir así mientras el bus avanza bajo sus pies.", ["Aplica la misma idea, pero ahora el estado inicial es el reposo."], ctx=N9, componente="Físico")

# =============================== INGLÉS: LECTURA ===============================
E1 = ("Hi Sam,\nI started at my new school last Monday. It is bigger than my old one, and it has a library and a football field. I was nervous on "
      "the first day because I didn't know anyone, but a girl called Paula showed me the classrooms and we had lunch together. My favourite "
      "subject is science: the teacher lets us do experiments every week. The only problem is the bus. It leaves at 5:45 a.m., so I have to get "
      "up very early!\nWrite soon,\nLaura")
I("ING-101", "ING", "lectura", "practica", -0.8, "Why was Laura nervous on her first day?",
  ["Because the school was very big.", "Because she didn't know anyone.", "Because she missed the bus.", "Because she had a science test."], "B",
  "El texto dice: 'I was nervous on the first day because I didn't know anyone'.", ["Busca la palabra 'nervous' y lee lo que viene después de 'because'."], ctx=E1)
I("ING-102", "ING", "lectura", "diagnostico", -0.3, "What does Laura like about her science class?",
  ["The teacher is new.", "They do experiments every week.", "It is in the library.", "It is the first class of the day."], "B",
  "'The teacher lets us do experiments every week': por eso es su materia favorita.", ["La respuesta está en la oración que empieza con 'My favourite subject'."], ctx=E1)
I("ING-103", "ING", "lectura", "practica", 0.2, "What is the problem with the bus?",
  ["It is too expensive.", "It doesn't go to the new school.", "It leaves very early.", "It is always late."], "C",
  "El bus sale a las 5:45 a. m., así que Laura debe levantarse muy temprano.", ["Fíjate en la hora y en lo que Laura dice después de 'so'."], ctx=E1)
I("ING-104", "ING", "lectura", "practica", 0.5, "We can infer that Paula is",
  ["Laura's sister.", "a teacher at the school.", "a friendly student at the new school.", "Sam's best friend."], "C",
  "Paula le mostró los salones y almorzó con ella: es una compañera amable. El texto no dice que sea profesora ni familiar.", ["¿Qué hizo Paula por Laura?", "Inferir es concluir algo que el texto no dice con esas palabras."], ctx=E1)

E2 = ("SCHOOL TRIP TO THE COFFEE FARM\nDate: Friday 12 September. We leave at 6:30 a.m. from the school gate and return at 4:00 p.m.\n"
      "Cost: 15,000 pesos (transport and lunch included). Pay your teacher before Wednesday.\nBring: comfortable shoes, a hat and a bottle "
      "of water. Do not bring mobile phones.\nStudents need a signed permission letter from their parents. No letter, no trip!")
I("ING-105", "ING", "lectura", "practica", -0.9, "What time do the students come back?",
  ["At 6:30 a.m.", "At 12:00 noon.", "At 4:00 p.m.", "On Wednesday."], "C",
  "'We leave at 6:30 a.m. ... and return at 4:00 p.m.': 'return' significa regresar.", ["Busca el verbo 'return'."], ctx=E2)
I("ING-106", "ING", "lectura", "practica", -0.4, "What is included in the price?",
  ["Transport and lunch.", "A hat and water.", "Shoes and transport.", "Only lunch."], "A",
  "Entre paréntesis dice 'transport and lunch included'. El sombrero y el agua los lleva cada estudiante.", ["Lee lo que está entre paréntesis después del precio."], ctx=E2)
I("ING-107", "ING", "lectura", "diagnostico", 0.3, "A student who has paid but has no permission letter",
  ["can go on the trip.", "cannot go on the trip.", "must pay again.", "has to bring a phone."], "B",
  "'No letter, no trip!' significa que sin la carta firmada no se puede ir, aunque se haya pagado.", ["La última línea del aviso es una condición."], ctx=E2)
I("ING-108", "ING", "lectura", "practica", 0.1, "Which of these should students NOT bring?",
  ["A hat.", "Water.", "A mobile phone.", "Comfortable shoes."], "C",
  "El aviso dice 'Do not bring mobile phones'.", ["Busca la instrucción negativa: 'Do not...'."], ctx=E2)

E3 = ("Don Ernesto has grown coffee for forty years on a small farm in the mountains. Every morning he gets up before sunrise, checks the plants "
      "and picks the red cherries by hand. \"Machines are faster,\" he says, \"but they can't choose only the ripe ones.\" Last year the rain came "
      "late and he lost a third of his harvest. Now he is planting trees between the coffee plants. The trees give shade, keep the soil wet "
      "and bring back the birds. His grandson wants to sell the coffee online, and Don Ernesto, who has never used a computer, is learning.")
I("ING-109", "ING", "lectura", "practica", -0.2, "Why does Don Ernesto pick the coffee by hand?",
  ["Because machines are too expensive.", "Because he can choose only the ripe cherries.", "Because it is faster.", "Because his grandson told him to."], "B",
  "Él dice que las máquinas son más rápidas, pero 'they can't choose only the ripe ones' (no pueden escoger solo las maduras).", ["Lee lo que dice Don Ernesto entre comillas.", "'Ripe' significa maduro."], ctx=E3)
I("ING-110", "ING", "lectura", "practica", 0.4, "What happened last year?",
  ["He lost part of his harvest because the rain came late.", "He bought a new machine.", "He sold his farm.", "The birds ate the coffee."], "A",
  "'Last year the rain came late and he lost a third of his harvest': perdió una tercera parte de la cosecha.", ["Busca 'Last year'."], ctx=E3)
I("ING-111", "ING", "lectura", "diagnostico", 0.6, "Why is he planting trees between the coffee plants?",
  ["To sell wood.", "To protect the coffee: the trees give shade and keep the soil wet.", "To replace the coffee plants.", "To build a house for his grandson."], "B",
  "El texto explica: 'The trees give shade, keep the soil wet and bring back the birds'.", ["La razón aparece en la oración siguiente a 'planting trees'."], ctx=E3)
I("ING-112", "ING", "lectura", "practica", 0.8, "What does the last sentence suggest about Don Ernesto?",
  ["He doesn't want to change anything.", "He is willing to learn new things, even at his age.", "He is angry with his grandson.", "He wants to stop growing coffee."], "B",
  "Nunca ha usado un computador y está aprendiendo para vender el café por internet: está dispuesto a aprender.", ["'Is learning' muestra una actitud.", "¿Qué dice eso de una persona que lleva cuarenta años haciendo lo mismo?"], ctx=E3)

E4 = ("Every Saturday, a group of students from a school in a small town collects plastic bottles from houses and shops. They started two years "
      "ago with five students; now there are more than sixty. They sell the bottles to a recycling company and use the money to buy books for "
      "the school library. Last month they bought forty new books. \"At first, people laughed at us,\" says Daniela, one of the organisers. "
      "\"Now they keep the bottles for us and ask when we are coming.\"")
I("ING-113", "ING", "lectura", "practica", -0.6, "What do the students do with the money?",
  ["They buy books for the library.", "They give it to the shops.", "They buy more bottles.", "They pay the recycling company."], "A",
  "'They ... use the money to buy books for the school library'.", ["Busca la palabra 'money'."], ctx=E4)
I("ING-114", "ING", "lectura", "practica", 0.0, "How has the group changed in two years?",
  ["It has become smaller.", "It has grown from five students to more than sixty.", "It has stopped collecting bottles.", "It has moved to another town."], "B",
  "Empezaron cinco estudiantes y ahora son más de sesenta.", ["Compara 'two years ago' con 'now'."], ctx=E4)
I("ING-115", "ING", "lectura", "practica", 0.7, "What does Daniela's comment show?",
  ["People in the town still laugh at the students.", "People's attitude towards the project has become positive.", "The students want to stop the project.", "The shops don't have bottles."], "B",
  "Al principio se burlaban ('laughed at us'); ahora guardan las botellas y preguntan cuándo pasan: la actitud cambió.", ["Compara 'At first' con 'Now' en lo que dice Daniela."], ctx=E4)
I("ING-116", "ING", "lectura", "practica", 0.9, "What is the best title for this text?",
  ["A problem with plastic in rivers", "How to sell books online", "Students turn bottles into books", "The history of a recycling company"], "C",
  "El texto cuenta cómo los estudiantes recogen botellas y con ese dinero compran libros: el título lo resume.", ["Un buen título recoge la idea de todo el texto, no un detalle."], ctx=E4)

E5 = ("When Marta opened the door that morning, her dog Canela was not in the yard. She looked in the street, behind the house and near the "
      "river. Nothing. She made posters with Canela's photo and put them on every corner. Three days later, an old man knocked at her door. "
      "\"I think this is yours,\" he said. Canela was sitting next to him, with a piece of rope around her neck and a very happy face. The man "
      "didn't want any money. \"She kept me company for three days,\" he said. \"That was enough.\"")
I("ING-117", "ING", "lectura", "practica", -0.7, "What did Marta do to find her dog?",
  ["She called the police.", "She made posters and put them on every corner.", "She bought a new dog.", "She waited at home."], "B",
  "'She made posters with Canela's photo and put them on every corner'.", ["Busca lo que hizo después de no encontrarla."], ctx=E5)
I("ING-118", "ING", "lectura", "practica", 0.1, "Who brought Canela back?",
  ["A neighbour's child.", "An old man.", "Marta's father.", "Nobody; she came back alone."], "B",
  "'Three days later, an old man knocked at her door' y Canela estaba a su lado.", ["Lee lo que pasa 'three days later'."], ctx=E5)
I("ING-119", "ING", "lectura", "practica", 0.7, "Why didn't the man want any money?",
  ["Because he was rich.", "Because the dog's company was enough for him.", "Because Marta had no money.", "Because he wanted to keep the dog."], "B",
  "Él dice: 'She kept me company for three days. That was enough': la compañía fue suficiente.", ["Lee las últimas palabras del hombre.", "'Kept me company' significa 'me acompañó'."], ctx=E5)
I("ING-120", "ING", "lectura", "practica", 0.5, "How did Marta probably feel at the end?",
  ["Angry.", "Bored.", "Relieved and grateful.", "Frightened."], "C",
  "Buscó a su perra durante tres días y se la devolvieron sana: lo esperable es alivio y gratitud.", ["Piensa en cómo te sentirías si recuperas algo que creías perdido."], ctx=E5)
