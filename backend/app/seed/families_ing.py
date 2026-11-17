"""Familias de Inglés: plantillas de gramática y listas de vocabulario, avisos y conversaciones.
Las explicaciones y pistas van en español, como en el resto del banco."""
from __future__ import annotations

from .math_families import _pack

SING = ["He", "She", "My brother", "The teacher", "Maria", "Our neighbour", "My mother", "Carlos"]
PLUR = ["They", "We", "My friends", "The students", "I", "You", "My parents", "The children"]
# (base, tercera persona, -ing, pasado, complemento)
VERBS = [("play", "plays", "playing", "played", "football after school"), ("study", "studies", "studying", "studied", "English at night"),
         ("work", "works", "working", "worked", "on a coffee farm"), ("live", "lives", "living", "lived", "in a small town"),
         ("watch", "watches", "watching", "watched", "TV in the evening"), ("go", "goes", "going", "went", "to school by bus"),
         ("help", "helps", "helping", "helped", "at home on Saturdays"), ("cook", "cooks", "cooking", "cooked", "lunch on Sundays"),
         ("read", "reads", "reading", "read", "books in the library"), ("walk", "walks", "walking", "walked", "to work"),
         ("teach", "teaches", "teaching", "taught", "maths at my school"), ("wash", "washes", "washing", "washed", "the car on Fridays"),
         ("buy", "buys", "buying", "bought", "bread at the bakery"), ("write", "writes", "writing", "wrote", "letters to the family"),
         ("eat", "eats", "eating", "ate", "fruit for breakfast"), ("make", "makes", "making", "made", "coffee for everyone")]


def present_simple(rng):
    base, third, ing, _, comp = rng.choice(VERBS)
    adv = rng.choice(["usually", "always", "often", "sometimes"])
    singular = rng.random() < 0.6
    subj = rng.choice(SING if singular else PLUR)
    correct = third if singular else base
    wrong = [base if singular else third, ing, f"{'is' if singular else 'are' if subj != 'I' else 'am'} {base}"]
    packed = _pack(rng, correct, wrong)
    return packed and {
        "competencia": "gramatica", "b": -0.6 if singular else -0.9,
        "stem": f"Choose the correct option. '{subj} {adv} ___ {comp}.'",
        "explanation": (f"Con he, she, it o un nombre en singular, el verbo en presente simple lleva -s o -es: '{third}'." if singular
                        else f"Con I, you, we y they el verbo en presente simple va en su forma base: '{base}'.") + f" '{adv}' indica un hábito, por eso se usa presente simple.",
        "hints": ["La palabra de frecuencia indica una rutina: presente simple.", "Fíjate si el sujeto es una sola persona (he/she) o varias."], "packed": packed}


def past_simple(rng):
    base, third, ing, past, comp = rng.choice([v for v in VERBS if v[0] not in ("read", "live", "teach")])
    for extra in (" on Saturdays", " on Sundays", " on Fridays", " at night", " in the evening", " after school", " for breakfast"):
        comp = comp.replace(extra, "")
    when = rng.choice(["Yesterday", "Last week", "Two days ago", "Last night", "Last Saturday"])
    subj = rng.choice(["he", "she", "my brother", "the teacher", "Maria", "our neighbour", "my mother", "Carlos", "they", "we", "my friends", "the students", "I", "you", "my parents", "the children"])
    packed = _pack(rng, past, [third, ing, f"will {base}", base])
    return packed and {
        "competencia": "gramatica", "b": 0.0 if past.endswith("ed") else 0.4,
        "stem": f"Choose the correct option. '{when}, {subj} ___ {comp}.'",
        "explanation": f"'{when}' señala una acción terminada: se usa pasado simple. El pasado de '{base}' es '{past}'" + ("." if past.endswith("ed") else " (verbo irregular)."),
        "hints": ["La expresión de tiempo te dice cuándo ocurrió la acción.", "Para acciones terminadas se usa el pasado simple."], "packed": packed}

COMPARATIVES = [("A bus", "a bicycle", "big", "bigger", "the biggest", "more big"), ("Gold", "silver", "expensive", "more expensive", "the most expensive", "expensiver"),
                ("A plane", "a train", "fast", "faster", "the fastest", "more fast"), ("My grandfather", "my father", "old", "older", "the oldest", "more old"),
                ("An elephant", "a horse", "heavy", "heavier", "the heaviest", "more heavy"), ("This exercise", "the last one", "easy", "easier", "the easiest", "more easy"),
                ("This film", "the book", "interesting", "more interesting", "the most interesting", "interestinger"), ("Today's weather", "yesterday's", "good", "better", "the best", "gooder"),
                ("A mountain", "a hill", "high", "higher", "the highest", "more high"), ("A motorbike", "a car", "cheap", "cheaper", "the cheapest", "more cheap"),
                ("A river", "a stream", "wide", "wider", "the widest", "more wide"), ("This road", "the old one", "bad", "worse", "the worst", "badder"),
                ("A city", "a village", "noisy", "noisier", "the noisiest", "more noisy"), ("Walking there", "taking the bus", "difficult", "more difficult", "the most difficult", "difficulter"),
                ("A lemon", "an orange", "sour", "sourer", "the sourest", "more sourer"), ("January", "February", "long", "longer", "the longest", "more long")]


def comparative(rng):
    a, b, adj, comp, sup, bad = rng.choice(COMPARATIVES)
    packed = _pack(rng, comp, [adj, sup, bad])
    return packed and {
        "competencia": "gramatica", "b": 0.1, "stem": f"Choose the correct option. '{a} is ___ than {b}.'",
        "explanation": f"Para comparar dos cosas se usa el comparativo seguido de 'than'. El comparativo de '{adj}' es '{comp}'. El superlativo ('{sup}') se usa para comparar una cosa con todo un grupo.",
        "hints": ["La palabra 'than' indica que se comparan dos cosas.", "Los adjetivos cortos añaden -er; los largos usan 'more'."], "packed": packed}


TIME_EXPR = [("at", "7 o'clock"), ("at", "night"), ("at", "noon"), ("at", "half past three"), ("on", "Monday"), ("on", "5 May"), ("on", "Sunday morning"),
             ("on", "my birthday"), ("in", "July"), ("in", "2019"), ("in", "the morning"), ("in", "the afternoon"), ("in", "December"), ("on", "Friday"), ("in", "the evening")]


def time_preposition(rng):
    prep, expr = rng.choice(TIME_EXPR)
    frame = rng.choice(["The meeting is ___ {e}.", "We have English class ___ {e}.", "The bus leaves ___ {e}.", "The match starts ___ {e}.", "I visit my grandmother ___ {e}."])
    if expr == "2019":
        frame = "My cousin was born ___ {e}."
    packed = _pack(rng, prep, [p for p in ("in", "on", "at", "to") if p != prep])
    return packed and {
        "competencia": "gramatica", "b": 0.2, "stem": "Choose the correct option. '" + frame.format(e=expr) + "'",
        "explanation": f"Se usa 'at' con horas y momentos exactos, 'on' con días y fechas, e 'in' con meses, años y partes del día. Por eso: '{prep} {expr}'.",
        "hints": ["¿La expresión es una hora, un día o un mes/año?", "at: horas; on: días y fechas; in: meses, años y partes del día."], "packed": packed}


COUNT = ["books", "plates", "chairs", "eggs", "pencils", "cups", "apples", "oranges", "tickets", "bottles"]
UNCOUNT = ["water", "money", "time", "homework", "sugar", "rice", "milk", "coffee", "bread", "information"]


def much_many(rng):
    countable = rng.random() < 0.5
    noun = rng.choice(COUNT if countable else UNCOUNT)
    frame = rng.choice(["How ___ {n} do you need?", "How ___ {n} did they buy?", "How ___ {n} {be} there?", "How ___ {n} do we have?"])
    correct = "many" if countable else "much"
    packed = _pack(rng, correct, ["much" if countable else "many", "more", "lot"])
    return packed and {
        "competencia": "gramatica", "b": 0.1, "stem": "Choose the correct option. '" + frame.format(n=noun, be="are" if countable else "is") + "'",
        "explanation": f"'{noun}' {'se puede contar (tiene plural)' if countable else 'no se puede contar por unidades'}: se pregunta con 'how {correct}'. 'Many' va con sustantivos contables en plural; 'much', con incontables.",
        "hints": ["¿Ese sustantivo se puede contar uno por uno?", "many + contables en plural; much + incontables."], "packed": packed}


PLACES = ["on the table", "in the kitchen", "in my bag", "in the classroom", "on the desk", "in that box"]
THINGS = [("a book", "is"), ("two pens", "are"), ("some water", "is"), ("three apples", "are"), ("a bottle", "is"), ("some bread", "is"),
          ("many keys", "are"), ("an umbrella", "is"), ("some coins", "are"), ("a lot of paper", "is"), ("four cups", "are"), ("some milk", "is")]


def there_is_are(rng):
    thing, be = rng.choice(THINGS)
    place = rng.choice(PLACES)
    packed = _pack(rng, be, [x for x in ("is", "are", "be", "have") if x != be])
    return packed and {
        "competencia": "gramatica", "b": -0.4, "stem": f"Choose the correct option. 'There ___ {thing} {place}.'",
        "explanation": f"'There is' se usa con singular e incontables; 'there are', con plural. '{thing}' pide '{be}'. Para decir 'hay' no se usa 'have'.",
        "hints": ["Mira si lo que viene después es una cosa o varias.", "En inglés 'hay' se dice 'there is' o 'there are', nunca 'there have'."], "packed": packed}


# (palabra interrogativa, resto de la pregunta, respuesta, distractores que no encajan con esa respuesta)
QUESTIONS = [("Where", "do you live?", "In a village near Ocaña.", ["When", "Who", "How many"]),
             ("When", "does the class start?", "At seven o'clock.", ["Where", "Who", "How many"]),
             ("Who", "is your English teacher?", "Mrs. Torres.", ["Where", "When", "How old"]),
             ("What", "do you do after school?", "I help my father on the farm.", ["Who", "How many", "How old"]),
             ("How old", "is your sister?", "She is nine.", ["How many", "Where", "What time"]),
             ("How many", "brothers do you have?", "Two.", ["How much", "How old", "Where"]),
             ("Why", "are you late?", "Because the bus broke down.", ["Where", "Who", "How old"]),
             ("What time", "do you get up?", "At half past five.", ["Where", "Who", "How many"]),
             ("How", "do you go to school?", "By motorbike.", ["Who", "How many", "How old"]),
             ("How much", "is this notebook?", "It's three thousand pesos.", ["How many", "How old", "Who"]),
             ("How often", "do you play football?", "Twice a week.", ["How old", "Who", "How much"]),
             ("How long", "is the film?", "About two hours.", ["How old", "How many", "Who"])]


def question_word(rng):
    word, rest, answer, wrong = rng.choice(QUESTIONS)
    packed = _pack(rng, word, wrong)
    return packed and {
        "competencia": "gramatica", "b": 0.0, "stem": f"Complete the question. A: '___ {rest}' B: '{answer}'",
        "explanation": f"La respuesta ('{answer}') da la información que pide '{word}'. La palabra interrogativa se elige según lo que responde la otra persona.",
        "hints": ["Lee primero la respuesta: ¿habla de un lugar, una hora, una persona, una cantidad?", "La palabra interrogativa debe corresponder a ese tipo de información."], "packed": packed}

VOCAB = {
    "places": [("People go there when they are ill and need a doctor.", "hospital"), ("You can borrow books there.", "library"), ("You buy bread and cakes there.", "bakery"),
               ("You buy medicine there.", "pharmacy"), ("Planes take off and land there.", "airport"), ("Farmers sell fruit and vegetables there.", "market"),
               ("People watch football matches there.", "stadium"), ("You keep your money there.", "bank"), ("You go there to send letters and parcels.", "post office"),
               ("Children learn to read and write there.", "school")],
    "jobs": [("This person grows crops and looks after animals.", "farmer"), ("This person looks after sick people in a hospital.", "nurse"),
             ("This person repairs cars and motorbikes.", "mechanic"), ("This person prepares food in a restaurant.", "cook"), ("This person looks after your teeth.", "dentist"),
             ("This person makes tables and chairs from wood.", "carpenter"), ("This person drives a bus or a taxi.", "driver"), ("This person helps students learn.", "teacher"),
             ("This person cuts people's hair.", "hairdresser"), ("This person puts out fires.", "firefighter")],
    "objects": [("You use it when it rains so you don't get wet.", "umbrella"), ("You use it to open a door.", "key"), ("You use them to cut paper.", "scissors"),
                ("You put it on your bed to keep warm.", "blanket"), ("You look at yourself in it.", "mirror"), ("You keep your money and cards in it.", "wallet"),
                ("You carry your books in it.", "backpack"), ("You climb it to reach high places.", "ladder"), ("You use it to dry yourself after a shower.", "towel"),
                ("You use it to tell the time.", "watch")],
    "food": [("It is white, and you add it to food to give it more flavour.", "salt"), ("Bees make it, and it is very sweet.", "honey"), ("It is made from milk, and it is often yellow.", "cheese"),
             ("Chickens lay them, and people often eat them for breakfast.", "eggs"), ("It is a hot liquid food, often made with vegetables.", "soup"),
             ("It is small and white, and people in Colombia eat it almost every day at lunch.", "rice"), ("You spread it on bread, and it is made from milk.", "butter"),
             ("It is a long yellow fruit.", "banana")],
}


def vocabulary(rng):
    cat = rng.choice(list(VOCAB))
    definition, word = rng.choice(VOCAB[cat])
    packed = _pack(rng, word, rng.sample([w for _, w in VOCAB[cat] if w != word], 3))
    return packed and {
        "competencia": "lexico_pragmatico", "b": -0.9, "stem": f"Which word matches the description? '{definition}'",
        "explanation": f"La descripción corresponde a '{word}'. Fíjate en las palabras clave de la descripción para descartar las demás opciones.",
        "hints": ["Busca en la descripción la palabra que conoces mejor y parte de ahí.", "Descarta las opciones que no tienen relación con la acción descrita."], "packed": packed}


NOTICES = [("NO SWIMMING. DEEP WATER.", "by a river"), ("QUIET PLEASE. PEOPLE ARE READING.", "in a library"), ("KEEP YOUR SEAT BELT FASTENED.", "on a plane"),
           ("FRESH BREAD EVERY MORNING.", "at a bakery"), ("STAFF MUST WASH THEIR HANDS BEFORE COOKING.", "in a restaurant kitchen"), ("SHOW YOUR TICKET TO THE DRIVER.", "on a bus"),
           ("DO NOT FEED THE ANIMALS.", "at a zoo"), ("VISITING HOURS: 2 P.M. TO 4 P.M. ONE VISITOR PER PATIENT.", "in a hospital"), ("TRY ON NO MORE THAN THREE ITEMS.", "in a clothes shop"),
           ("PLEASE WAIT BEHIND THE YELLOW LINE UNTIL THE TRAIN STOPS.", "at a train station"), ("KEEP OUT OF REACH OF CHILDREN. TAKE ONE TABLET A DAY.", "on a medicine box"),
           ("FRAGILE. THIS SIDE UP.", "on a parcel"), ("SLOW DOWN. SCHOOL AHEAD.", "on a road"), ("NO FLASH PHOTOGRAPHY NEAR THE PAINTINGS.", "in a museum"),
           ("ROOM KEYS MUST BE LEFT AT RECEPTION.", "in a hotel"), ("WEIGH YOUR FRUIT BEFORE YOU GO TO THE CASHIER.", "in a supermarket"),
           ("BOOTS MUST BE CLEANED BEFORE ENTERING THE CHANGING ROOM.", "at a football club"), ("LAST FILM STARTS AT 9 P.M.", "at a cinema"),
           ("EXAM IN PROGRESS. DO NOT ENTER.", "at a school"), ("FILL UP HERE. OPEN 24 HOURS.", "at a petrol station")]


def notice(rng):
    text, place = rng.choice(NOTICES)
    packed = _pack(rng, place, rng.sample([p for _, p in NOTICES if p != place], 3))
    return packed and {
        "competencia": "lexico_pragmatico", "b": -0.5, "stem": f"Where can you see this notice? '{text}'",
        "explanation": f"Las palabras clave del aviso indican dónde se encontraría: {place}.",
        "hints": ["Identifica una o dos palabras clave del aviso.", "Piensa en qué lugar tendría sentido dar esa instrucción."], "packed": packed}


TALK = [("Would you like some more rice?", "No, thanks. I'm full.", ["Yes, I like.", "I'm fine, and you?", "It's on the table."]),
        ("How was your weekend?", "It was great. We went to the river.", ["It's Saturday.", "Yes, I was.", "At the weekend."]),
        ("Can I borrow your pen, please?", "Sure, here you are.", ["Yes, I am.", "No, it isn't mine pen.", "I borrow it."]),
        ("What's the matter?", "I have a terrible headache.", ["It doesn't matter.", "Nothing, thanks to you.", "I'm matter."]),
        ("Excuse me, where is the bus station?", "Go straight on and turn left.", ["It leaves at six.", "Yes, it is.", "By bus."]),
        ("Thank you for your help.", "You're welcome.", ["Yes, please.", "I'm sorry.", "Good idea."]),
        ("Shall we play football this afternoon?", "Good idea. What time?", ["Yes, we shall playing.", "I played yesterday.", "It's my ball."]),
        ("I passed my exam!", "Congratulations!", ["What a pity!", "Never mind.", "Good luck!"]),
        ("I'm sorry I'm late.", "That's all right. Come in.", ["You're welcome.", "Me too.", "Yes, please."]),
        ("What does your father do?", "He's a farmer.", ["He's fine, thanks.", "He's doing the dishes now.", "He does."]),
        ("Could you speak more slowly, please?", "Of course. Sorry.", ["No, I speak English.", "Yes, I could spoke.", "Slowly, thanks."]),
        ("How much is this T-shirt?", "It's twenty thousand pesos.", ["It's too much big.", "It's blue.", "I have two."]),
        ("I can't find my keys.", "Have you looked in your bag?", ["Here you are welcome.", "They are keys.", "No, I can't."]),
        ("Do you mind if I open the window?", "Not at all. It's hot in here.", ["Yes, I do open.", "The window is open mind.", "I don't have a window."]),
        ("What time shall we meet?", "How about half past four?", ["At the park.", "With my sister.", "For two hours."]),
        ("My grandmother is in hospital.", "Oh, I'm sorry to hear that.", ["Well done!", "That's a good idea.", "Have a nice time!"]),
        ("Is this seat free?", "Yes, go ahead.", ["No, it costs money.", "Yes, it's a seat.", "I'm free on Monday."]),
        ("Have a good trip!", "Thanks. See you next week.", ["Yes, I have.", "Same to you trip.", "No, I don't have."]),
        ("Whose turn is it?", "I think it's mine.", ["It's on the left.", "Turn right.", "It's me turn."]),
        ("What do you think of the new teacher?", "She seems very nice.", ["I think so.", "She thinks a lot.", "Yes, I do."])]


def conversation(rng):
    prompt, reply, wrong = rng.choice(TALK)
    packed = _pack(rng, reply, wrong)
    return packed and {
        "competencia": "lexico_pragmatico", "b": 0.0, "stem": f"Complete the conversation. A: '{prompt}' B: '___'",
        "explanation": f"La respuesta natural a '{prompt}' es '{reply}'. Las otras opciones responden a otra pregunta o no son expresiones correctas en inglés.",
        "hints": ["¿La primera persona pregunta, ofrece, agradece o se disculpa?", "Elige la respuesta que tendría sentido en una conversación real."], "packed": packed}


FRIENDS = ["Laura", "Andrés", "Camila", "Julián", "Sofía", "Mateo", "Valentina", "Daniel"]
EVENTS = [("a football match", "the school field", "your sports shoes"), ("a birthday party", "my house", "a small gift"),
          ("a science fair", "the school library", "your project poster"), ("a picnic", "the park near the river", "something to drink"),
          ("a music concert", "the town square", "a jacket because it gets cold"), ("a study group for the exam", "the community centre", "your maths notebook"),
          ("a tree-planting day", "the school garden", "gloves and a hat"), ("a dance class", "the cultural centre", "comfortable clothes")]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIMES = ["8 a.m.", "9:30 a.m.", "10 a.m.", "2 p.m.", "3:30 p.m.", "4 p.m.", "5 p.m.", "6:30 p.m."]


def message(rng):
    sender, friend = rng.sample(FRIENDS, 2)
    event, place, bring = rng.choice(EVENTS)
    day = rng.choice(DAYS)
    k = rng.randrange(1, len(TIMES))
    time, meet = TIMES[k], rng.choice(TIMES[:k])  # se encuentran antes del evento
    text = (f"Hi {friend},\nThere is {event} on {day} at {time} at {place}. Can you come? Please bring {bring}. "
            f"We can meet at my house at {meet} and go together.\nSee you,\n{sender}")
    kind = rng.choice(["day", "place", "bring", "meet"])
    if kind == "day":
        stem, correct, wrong = "When is the event?", f"On {day} at {time}.", [f"On {d} at {time}." for d in rng.sample([x for x in DAYS if x != day], 2)] + [f"On {day} at {meet}."]
        expl = f"El mensaje dice 'on {day} at {time}'. La hora {meet} es la de encontrarse en la casa, no la del evento."
    elif kind == "place":
        others = [p for _, p, _ in EVENTS if p != place]
        stem, correct, wrong = "Where is the event?", place[0].upper() + place[1:] + ".", [p[0].upper() + p[1:] + "." for p in rng.sample(others, 2)] + [f"At {sender}'s house."]
        expl = f"El evento es en '{place}'. La casa de {sender} es solo el punto de encuentro."
    elif kind == "bring":
        others = [b for _, _, b in EVENTS if b != bring]
        stem, correct, wrong = f"What does {sender} ask {friend} to bring?", bring[0].upper() + bring[1:] + ".", [b[0].upper() + b[1:] + "." for b in rng.sample(others, 3)]
        expl = f"'Please bring {bring}': eso es lo que pide llevar."
    else:
        stem, correct, wrong = f"Why does {sender} want to meet {friend} before the event?", "To go to the event together.", [
            "To do homework together.", "To buy the tickets.", f"Because the event starts at {meet}."]
        expl = f"'We can meet at my house at {meet} and go together': se encuentran para ir juntos. El evento empieza a las {time}."
    dot = lambda t: t if t.endswith(".") else t + "."
    correct, wrong = dot(correct.rstrip(".") if correct.endswith("m..") else correct), wrong
    fix = lambda t: t[:-1] if t.endswith("..") else t
    packed = _pack(rng, fix(correct), [fix(w) for w in wrong])
    return packed and {
        "competencia": "lectura", "b": {"day": -0.4, "place": -0.5, "bring": -0.6, "meet": 0.2}[kind],
        "context": text, "stem": stem, "explanation": expl,
        "hints": ["Busca en el mensaje la palabra clave de la pregunta (when, where, bring, why).", "Cuidado: el mensaje tiene dos horas y dos lugares distintos."], "packed": packed}


FAMILIES = [message, present_simple, past_simple, comparative, time_preposition, much_many, there_is_are, question_word, vocabulary, notice, conversation]
