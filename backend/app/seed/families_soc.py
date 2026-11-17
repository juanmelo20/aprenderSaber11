"""Familias de Sociales y Ciudadanas. Base normativa: Constitución Política de Colombia de 1991
(arts. 23, 30, 86, 87, 88, 103) y Ley 134 de 1994. Cada situación corresponde a un único mecanismo u organismo."""
from __future__ import annotations

from .math_families import _pack

PEOPLE = ["Una señora", "Un campesino", "Una estudiante", "Un comerciante", "Una madre cabeza de hogar", "Un adulto mayor", "Una docente", "Un joven"]
PLACES = ["Hacarí", "Ocaña", "El Tarra", "Ábrego", "Convención", "Teorama", "San Calixto", "La Playa"]

# mecanismo: (nombre en la opción, explicación, [situaciones con {quien} y {lugar}])
MECHANISMS = {
    "tutela": ("La acción de tutela.",
               "La acción de tutela (artículo 86) protege de forma inmediata los derechos fundamentales de una persona cuando una autoridad o, en ciertos casos, un particular los vulnera o amenaza.",
               ["{quien} de {lugar} necesita una cirugía urgente que su médico ordenó y su entidad de salud se la niega sin dar razones.",
                "A {quien_min} de {lugar} le negaron la matrícula en el colegio público porque su familia no ha pagado una deuda con la tienda escolar.",
                "{quien} de {lugar} fue retirado de su trabajo en una entidad pública por su religión y quiere que se protejan sus derechos de inmediato."]),
    "cumplimiento": ("La acción de cumplimiento.",
                     "La acción de cumplimiento (artículo 87) sirve para pedir a un juez que ordene a una autoridad cumplir una ley o un acto administrativo que está desconociendo.",
                     ["Un acuerdo del concejo de {lugar} ordenó a la alcaldía publicar cada año en la cartelera municipal el informe de gastos del presupuesto. Han pasado dos años sin que lo haga, y {quien_min} quiere que un juez le ordene cumplir ese acto administrativo.",
                      "Una ley obliga a las alcaldías a crear un comité de participación de víctimas. En {lugar} la alcaldía lleva años sin crearlo, y {quien_min} quiere que un juez ordene cumplir lo que dice la ley."]),
    "popular": ("La acción popular.",
                "La acción popular (artículo 88) protege derechos e intereses colectivos, como el ambiente sano, el espacio público o la salubridad, que afectan a toda una comunidad.",
                ["Una empresa vierte residuos al río del que toma agua toda la vereda en {lugar}. {quien} quiere proteger el derecho colectivo a un ambiente sano.",
                 "En {lugar}, unos comerciantes ocuparon con construcciones el parque principal y los andenes. {quien} quiere que se proteja el espacio público de todos.",
                 "Un botadero de basura a cielo abierto en {lugar} afecta la salud de todos los habitantes del barrio. {quien} busca proteger la salubridad pública."]),
    "habeas": ("El habeas corpus.",
               "El habeas corpus (artículo 30) protege la libertad: quien es privado de ella de manera ilegal puede pedir a un juez que decida en un plazo de 36 horas.",
               ["El hermano de {quien_min} de {lugar} fue detenido hace tres días sin orden judicial y sin que lo presenten ante un juez.",
                "{quien} de {lugar} denuncia que su hijo sigue detenido aunque ya se cumplió el tiempo que la ley permite sin que un juez legalice la captura."]),
    "peticion": ("El derecho de petición.",
                 "El derecho de petición (artículo 23) permite presentar solicitudes respetuosas a las autoridades y obtener una respuesta de fondo y oportuna.",
                 ["{quien} de {lugar} quiere que la alcaldía le informe por escrito cuánto dinero se invirtió en la vía de su vereda.",
                  "{quien} de {lugar} necesita una copia de los documentos de un contrato de la alcaldía y quiere solicitarla formalmente."]),
    "revocatoria": ("La revocatoria del mandato.",
                    "La revocatoria del mandato (artículo 103 y Ley 134 de 1994) permite a los ciudadanos dar por terminado el periodo de un alcalde o gobernador que incumple su programa de gobierno.",
                    ["Los habitantes de {lugar} consideran que el alcalde incumplió el programa de gobierno con el que lo eligieron y quieren votar para que deje el cargo."]),
    "cabildo": ("El cabildo abierto.",
                "El cabildo abierto (artículo 103 y Ley 134 de 1994) es una reunión pública del concejo municipal en la que los habitantes discuten directamente asuntos de interés de la comunidad.",
                ["En {lugar}, la comunidad quiere discutir directamente con el concejo municipal la falta de transporte escolar."]),
}


def _quien(rng):
    q = rng.choice(PEOPLE)
    return q, q[0].lower() + q[1:]


def mecanismo(rng):
    key = rng.choice(list(MECHANISMS))
    name, expl, scenes = MECHANISMS[key]
    quien, quien_min = _quien(rng)
    scene = rng.choice(scenes).format(quien=quien, quien_min=quien_min, lugar=rng.choice(PLACES))
    # La acción popular y la de cumplimiento pueden confundirse en algunos casos: no se ponen juntas como opciones.
    clash = {"cumplimiento": {"popular"}, "popular": {"cumplimiento"}}.get(key, set())
    others = [MECHANISMS[k][0] for k in MECHANISMS if k != key and k not in clash]
    packed = _pack(rng, name, rng.sample(others, 3))
    return packed and {
        "competencia": "pensamiento_social", "b": {"tutela": -0.6, "peticion": -0.4, "popular": 0.3, "cumplimiento": 0.6, "habeas": 0.2,
                                                    "revocatoria": -0.2, "cabildo": 0.4}[key],
        "context": scene, "stem": "¿Cuál es el mecanismo previsto en la Constitución más adecuado para esta situación?",
        "explanation": expl,
        "hints": ["¿Lo que se busca proteger es un derecho de una persona, un derecho de toda la comunidad, o que se cumpla una norma?",
                  "Fíjate si se trata de la libertad, de pedir información o de una decisión que deben tomar los votantes."], "packed": packed}


ENTITIES = {
    "procuraduria": ("La Procuraduría General de la Nación.",
                     "La Procuraduría vigila la conducta de los servidores públicos y puede investigarlos y sancionarlos disciplinariamente.",
                     ["Un funcionario de la alcaldía de {lugar} falta al trabajo sin justificación y trata mal a los ciudadanos. ¿Qué entidad puede investigarlo disciplinariamente?",
                      "Un concejal de {lugar} habría usado su cargo para favorecer a un familiar en un nombramiento. ¿Qué entidad investiga su conducta como servidor público?"]),
    "contraloria": ("La Contraloría General de la República.",
                    "La Contraloría vigila la gestión fiscal: cómo se manejan los dineros y bienes públicos.",
                    ["En {lugar} se pagó un puente que nunca se terminó y no se sabe en qué se gastó el dinero. ¿Qué entidad vigila el uso de los recursos públicos?",
                     "Una auditoría encontró que un hospital público de {lugar} compró equipos con sobrecostos. ¿Qué entidad vigila el manejo de esos recursos?"]),
    "defensoria": ("La Defensoría del Pueblo.",
                   "La Defensoría del Pueblo promueve, divulga y defiende los derechos humanos, y orienta a las personas para que los reclamen.",
                   ["Varias familias desplazadas que llegaron a {lugar} necesitan orientación para que se respeten sus derechos humanos. ¿Qué entidad tiene esa función?",
                    "Una comunidad de {lugar} denuncia amenazas contra sus líderes sociales y pide acompañamiento en la defensa de sus derechos. ¿Qué entidad tiene esa misión?"]),
    "registraduria": ("La Registraduría Nacional del Estado Civil.",
                      "La Registraduría se encarga del registro civil, de la identificación de los colombianos (como la cédula) y de organizar las elecciones.",
                      ["Un joven de {lugar} cumplió 18 años y necesita tramitar su cédula de ciudadanía. ¿Qué entidad la expide?",
                       "Se acercan las elecciones de alcalde en {lugar} y hay que organizar las mesas de votación y los jurados. ¿Qué entidad organiza las elecciones?"]),
    "fiscalia": ("La Fiscalía General de la Nación.",
                 "La Fiscalía investiga los delitos y acusa a los presuntos responsables ante los jueces.",
                 ["A un comerciante de {lugar} le robaron su mercancía y quiere denunciar el delito para que se investigue. ¿Qué entidad investiga los delitos?",
                  "Se sospecha que una persona falsificó escrituras de tierras en {lugar}. ¿Qué entidad debe investigar ese posible delito y acusar ante un juez?"]),
    "banco_republica": ("El Banco de la República.",
                        "El Banco de la República es el banco central: emite la moneda y tiene como función mantener el poder adquisitivo del peso, es decir, controlar la inflación.",
                        ["Los precios en todo el país suben muy rápido y el peso pierde poder de compra. ¿Qué entidad tiene la función de controlar la inflación?",
                         "Se necesitan imprimir nuevos billetes para reemplazar los que están deteriorados. ¿Qué entidad emite la moneda en Colombia?"]),
    "corte_constitucional": ("La Corte Constitucional.",
                             "La Corte Constitucional tiene a su cargo la guarda de la integridad y supremacía de la Constitución: decide si las leyes se ajustan a ella.",
                             ["Un grupo de ciudadanos considera que una ley recién aprobada viola un derecho reconocido en la Constitución. ¿Qué tribunal decide si la ley se ajusta a la Constitución?"]),
    "congreso": ("El Congreso de la República.",
                 "El Congreso, rama legislativa, hace las leyes y ejerce control político sobre el gobierno.",
                 ["Se quiere crear una nueva ley que regule el transporte escolar en zonas rurales. ¿Qué institución tiene la función de hacer las leyes?"]),
}


def organismo(rng):
    key = rng.choice(list(ENTITIES))
    name, expl, scenes = ENTITIES[key]
    scene = rng.choice(scenes).format(lugar=rng.choice(PLACES))
    others = [ENTITIES[k][0] for k in ENTITIES if k != key]
    packed = _pack(rng, name, rng.sample(others, 3))
    return packed and {
        "competencia": "pensamiento_social", "b": {"registraduria": -0.8, "fiscalia": -0.4, "congreso": -0.6, "defensoria": 0.0, "procuraduria": 0.5,
                                                    "contraloria": 0.5, "banco_republica": 0.3, "corte_constitucional": 0.1}[key],
        "stem": scene, "explanation": expl,
        "hints": ["Pregúntate si el problema es la conducta de un funcionario, el uso del dinero público, un delito o un derecho humano.",
                  "Cada entidad tiene una función principal distinta: identifica cuál corresponde a la situación."], "packed": packed}


FAMILIES = [mecanismo, organismo]
