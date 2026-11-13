"""Estructura del examen Saber 11.

Competencias y porcentajes: Guía de orientación Saber 11.º 2026-2 (ICFES).
Los cortes de nivel de desempeño son PROVISIONALES y deben verificarse con la
documentación de resultados del ICFES antes de usarlos en informes formales.
"""

AREAS: dict[str, dict] = {
    "LEC": {
        "name": "Lectura Crítica",
        "questions": 41,
        "competencias": {
            "locales": ("Identifica y entiende los contenidos locales de un texto", 0.25),
            "global": ("Comprende cómo se articulan las partes de un texto para darle sentido global", 0.42),
            "critica": ("Reflexiona a partir de un texto y evalúa su contenido", 0.33),
        },
        "cuts": [36, 51, 66],
        "levels": ["1", "2", "3", "4"],
    },
    "MAT": {
        "name": "Matemáticas",
        "questions": 50,
        "competencias": {
            "interpretacion": ("Interpretación y representación", 0.34),
            "formulacion": ("Formulación y ejecución", 0.43),
            "argumentacion": ("Argumentación", 0.23),
        },
        "cuts": [36, 51, 71],
        "levels": ["1", "2", "3", "4"],
    },
    "SOC": {
        "name": "Sociales y Ciudadanas",
        "questions": 50,
        "competencias": {
            "pensamiento_social": ("Pensamiento social", 0.30),
            "perspectivas": ("Interpretación y análisis de perspectivas", 0.40),
            "sistemico": ("Pensamiento reflexivo y sistémico", 0.30),
        },
        "cuts": [41, 56, 71],
        "levels": ["1", "2", "3", "4"],
    },
    "NAT": {
        "name": "Ciencias Naturales",
        "questions": 58,
        "competencias": {
            "uso": ("Uso comprensivo del conocimiento científico", 0.30),
            "explicacion": ("Explicación de fenómenos", 0.30),
            "indagacion": ("Indagación", 0.40),
        },
        "cuts": [41, 56, 71],
        "levels": ["1", "2", "3", "4"],
    },
    "ING": {
        "name": "Inglés",
        "questions": 55,
        # Las 7 partes de la prueba agrupadas en tres frentes de trabajo.
        "competencias": {
            "lexico_pragmatico": ("Vocabulario, avisos y conversaciones (partes 1 a 3)", 0.33),
            "gramatica": ("Gramática y léxico en textos (partes 4 y 7)", 0.40),
            "lectura": ("Comprensión de lectura literal e inferencial (partes 5 y 6)", 0.27),
        },
        "cuts": [48, 58, 68, 79],
        "levels": ["Pre A1", "A1", "A2", "B1", "B+"],
    },
}

AREA_ORDER = ["LEC", "MAT", "SOC", "NAT", "ING"]


def comp_key(area: str, comp: str) -> str:
    return f"{area}.{comp}"


def comp_label(key: str) -> str:
    area, comp = key.split(".", 1)
    return AREAS[area]["competencias"][comp][0]


def level_for(area: str, score: int) -> str:
    spec = AREAS[area]
    idx = sum(1 for c in spec["cuts"] if score >= c)
    return spec["levels"][idx]


def public_catalog() -> dict:
    return {
        "order": AREA_ORDER,
        "areas": {
            k: {
                "name": v["name"],
                "levels": v["levels"],
                "competencias": {c: {"label": lab, "weight": w} for c, (lab, w) in v["competencias"].items()},
            }
            for k, v in AREAS.items()
        },
    }


# Sugerencias didácticas para el plan de clase del docente (texto propio, basado en
# práctica de recuperación, práctica distribuida e intercalada).
TEACHING_TIPS: dict[str, list[str]] = {
    "LEC.locales": [
        "Abra la clase con 5 minutos de preguntas literales sobre un párrafo corto, sin releer.",
        "Pida subrayar solo la frase que responde la pregunta y justificar por qué las demás no.",
    ],
    "LEC.global": [
        "Trabaje la función de cada párrafo: que el grupo escriba en una línea para qué sirve cada uno.",
        "Entregue textos con conectores borrados y discutan cuál conector cambia el sentido.",
    ],
    "LEC.critica": [
        "Contraste dos textos cortos sobre el mismo tema y pregunte qué supone cada autor sin decirlo.",
        "Pida identificar la tesis y un argumento que la debilitaría.",
    ],
    "MAT.interpretacion": [
        "Proyecte una tabla o gráfica real y haga tres preguntas de lectura antes de cualquier cálculo.",
        "Pida traducir un enunciado a tabla, a gráfica y a expresión: tres representaciones del mismo dato.",
    ],
    "MAT.formulacion": [
        "Resuelva un problema modelo en voz alta y luego dé uno gemelo con otros números, sin apuntes.",
        "Mezcle en la misma hoja porcentajes, proporciones y promedios para que deban elegir el procedimiento.",
    ],
    "MAT.argumentacion": [
        "Presente una solución con un error y pida encontrarlo y explicar por qué es un error.",
        "Use afirmaciones del tipo 'siempre / a veces / nunca' y exija un contraejemplo.",
    ],
    "SOC.pensamiento_social": [
        "Ubique cada concepto (Estado, derechos, ramas del poder) en un caso cercano del municipio.",
        "Haga una línea de tiempo corta y pregunte qué cambió y qué siguió igual.",
    ],
    "SOC.perspectivas": [
        "Entregue dos fuentes con posturas opuestas y pida identificar quién habla y qué interés tiene.",
        "Juego de roles: cada grupo defiende a un actor del conflicto con argumentos de la fuente.",
    ],
    "SOC.sistemico": [
        "Ante una medida (por ejemplo, subir un precio), dibujen a quién beneficia y a quién afecta.",
        "Pida anticipar una consecuencia no deseada de una solución propuesta.",
    ],
    "NAT.uso": [
        "Empiece con 5 preguntas rápidas de conceptos de la semana anterior (recuperación, sin cuaderno).",
        "Pida explicar un concepto con un ejemplo de la finca, la cocina o el río.",
    ],
    "NAT.explicacion": [
        "Muestre un fenómeno (video corto o demostración) y pida la explicación con causa y efecto.",
        "Compare dos explicaciones de estudiantes y decidan cuál usa mejor la evidencia.",
    ],
    "NAT.indagacion": [
        "Entregue una tabla de resultados y pregunte qué conclusión sí se puede sacar y cuál no.",
        "Pida identificar la variable que se cambia, la que se mide y las que se dejan fijas.",
    ],
    "ING.lexico_pragmatico": [
        "Tarjetas de vocabulario por tema con repaso espaciado: hoy, en dos días y en una semana.",
        "Avisos reales (signs): dónde lo verías y qué te pide hacer.",
    ],
    "ING.gramatica": [
        "Textos con huecos: que justifiquen la opción por la pista que hay antes y después del hueco.",
        "Mini dictados de 3 frases para fijar tiempos verbales y preposiciones frecuentes.",
    ],
    "ING.lectura": [
        "Lectura corta con preguntas who/what/where antes de las de inferencia.",
        "Pida señalar la línea exacta del texto que sustenta cada respuesta.",
    ],
}
