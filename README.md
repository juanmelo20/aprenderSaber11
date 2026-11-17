# Rumbo 11 (nombre provisional)

Plataforma de preparación para la prueba Saber 11: diagnóstico adaptativo corto por área, plan de mejora semanal por estudiante, tutor que da pistas y no respuestas, simulacros tipo examen, y tableros para el docente de cada área y para el colegio.

Versión 0.1. Funciona completa en el computador con los emuladores de Firebase. Todavía no está publicada en internet: para eso faltan las cuentas reales (ver "Publicar").

El nombre se cambia sin tocar código: variable `APP_NAME` en el servidor y `VITE_APP_NAME` en la web.

## Qué hay en cada carpeta

| Carpeta | Qué es |
|---|---|
| `backend/` | Servidor en Python (FastAPI). Aquí vive toda la lógica: diagnóstico, plan, calificación, tutor, licencias, autorizaciones. |
| `backend/app/engine/` | Los tres motores: `irt.py` (diagnóstico adaptativo, modelo 3PL), `bkt.py` (dominio por competencia), `planner.py` (plan semanal). |
| `backend/app/seed/` | Banco de preguntas: las escritas a mano (`bank_*.py`) y las familias que generan variantes nuevas (`families*.py`, `math_families.py`). |
| `backend/app/drafts.py` | Redacción de borradores con el modelo de lenguaje, para revisión docente. |
| `frontend/` | La web (React + TypeScript), instalable en el celular y usable sin conexión. |
| `firestore.rules` | Reglas de seguridad de la base de datos. |
| `e2e/` | Recorrido automático en un navegador real por todos los roles. |

## Probarla en el computador

Se necesita Python 3.11 o superior, Node 20 o superior y Java 21 o superior (lo usan los emuladores).

```bash
# 1. Emuladores de Firebase (dejar esta terminal abierta)
npm install
npm run emuladores

# 2. Servidor (otra terminal)
cd backend
python -m venv .venv && source .venv/bin/activate      # en Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
export FIRESTORE_EMULATOR_HOST=127.0.0.1:8080 FIREBASE_AUTH_EMULATOR_HOST=127.0.0.1:9099
python -m scripts.dev_seed          # crea cuentas de demostración y carga el banco
uvicorn app.main:app --port 8000

# 3. Web (otra terminal)
cd frontend
npm install
npm run dev                          # abre http://127.0.0.1:5173
```

En Windows (PowerShell) las variables se definen así: `$env:FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"; $env:FIREBASE_AUTH_EMULATOR_HOST="127.0.0.1:9099"`.

`dev_seed` imprime las cuentas de demostración (todas ficticias, contraseña `rumbo11-demo`): administrador, colegio, dos docentes, estudiantes en distintos estados y un particular.

### Pruebas

```bash
cd backend && pytest                 # 32 pruebas: motores, banco, tutor y flujo completo contra los emuladores
./e2e/correr.sh carpeta_capturas     # recorrido en Chrome (requiere `pip install playwright`); usa la web compilada contra los emuladores: npx vite build --mode e2e && npx vite preview --port 5173
```

## Cómo funciona

**Roles.** Administrador (crea colegios y licencias, activa planes individuales, exporta datos anónimos), institución (asigna el docente de cada área y registra estudiantes hasta el número de cupos), docente (ve el dominio de su grupo por competencia y aprueba preguntas), estudiante y particular.

**Autorización de datos.** Ningún estudiante puede empezar sin autorización. A los menores los autoriza su acudiente con un enlace que entrega el colegio; los mayores de edad autorizan al entrar. El servidor lo exige en cada petición, no solo la pantalla.

**Diagnóstico.** Entre 6 y 10 preguntas por área, elegidas según las respuestas anteriores. Entrega un puntaje estimado con su rango, no una cifra única: con tan pocas preguntas el margen es de unos 7 puntos hacia cada lado.

**Plan semanal.** Toma las tres competencias más débiles (máximo dos de la misma área), arma una práctica por cada una, un repaso de semanas anteriores y un cuestionario de salida sin ayudas. Con 60 % o más en la salida, la semana siguiente cambia de foco; con menos, refuerza los mismos temas con otras preguntas.

**Tutor.** Antes de responder solo orienta; después explica. Sin clave de Groq usa las pistas escritas para cada pregunta. Con clave, la respuesta del modelo pasa por tres filtros antes de mostrarse: que no nombre la opción correcta, que no la diga con otras palabras y que no confirme ni niegue lo que el estudiante propone. Si falla alguno, se muestra la pista escrita. Al modelo nunca se le envía nombre ni correo. En el cuestionario de salida y en el simulacro no hay tutor.

**Preguntas que no se repiten.** El plan nunca usa una pregunta ya vista mientras quede alguna nueva. Hay dos fuentes:

- *Familias* (51): plantillas de Matemáticas, Ciencias, Sociales (mecanismos de participación y organismos del Estado) e Inglés que producen una pregunta distinta cada vez, con la clave calculada. Cada variante lleva una firma de su contenido, así que dos variantes con el mismo texto cuentan como la misma pregunta y no se vuelven a entregar. En conjunto dan más de 8.000 preguntas distintas.
- *Preguntas escritas a mano* (311): textos y casos originales con sus preguntas. Aquí el banco es finito.

En una simulación de 12 estudiantes durante 40 semanas, con el plan rotando entre sus competencias más débiles, la primera pregunta repetida apareció entre la semana 6 y la 15. Lo que se agota primero es lo que depende de textos. Si la misma competencia fuera foco todas las semanas (el peor caso, 6 preguntas nuevas por semana), esto dura cada una:

| Competencia | Semanas sin repetir |
|---|---|
| Matemáticas: interpretación, formulación | más de 104 |
| Matemáticas: argumentación | 80 |
| Sociales: pensamiento social | más de 104 |
| Sociales: perspectivas, pensamiento sistémico | 3 a 4 |
| Naturales: uso del conocimiento | 81 |
| Naturales: indagación | más de 104 |
| Naturales: explicación de fenómenos | 10 |
| Inglés: vocabulario y gramática | más de 104 |
| Inglés: lectura | 6 |
| Lectura Crítica (cada competencia) | 3 a 5 |

Lectura Crítica, Sociales y la lectura en Inglés dependen de textos: no se pueden generar con plantillas sin perder calidad. Su banco crece de dos maneras: escribiendo más en `backend/app/seed/` o con el botón "Redactar borradores con IA" del administrador, que pide al modelo un texto nuevo con cuatro preguntas y lo deja en la bandeja del docente.

**Borradores con IA.** El modelo propone y una persona valida. Un borrador de origen IA nunca llega a un estudiante sin aprobación docente, ni siquiera con `ALLOW_UNREVIEWED_ITEMS=true`. En las pruebas el modelo cometió errores de hecho (por ejemplo, ubicó a un pueblo indígena en un municipio que no es el suyo): la revisión no es un trámite.

**Sin conexión.** El plan de la semana queda guardado en el dispositivo. Las prácticas se pueden responder sin señal y se envían solas al volver la conexión. El diagnóstico, el tutor con IA y el simulacro sí necesitan conexión.

**Simulacros.** Iguales para todos, con tiempo y sin ayudas. Hay tres: uno corto (15 preguntas, 30 minutos) y dos tipo examen (60 preguntas, 120 minutos) con la misma proporción por área que la prueba (Lectura 10, Matemáticas 12, Sociales 12, Naturales 13, Inglés 13). Ninguna de sus preguntas aparece en el diagnóstico, en la práctica ni en otro simulacro: las variantes de familias que usan quedan reservadas y la práctica nunca las genera.

## Publicar (todo en planes gratuitos)

**Ya está hecho en el proyecto de Firebase `aprendersaber11` (plan Spark):**

- Inicio de sesión con correo y contraseña, activado.
- Base de datos Firestore creada en `nam5` (Estados Unidos), en modo de producción.
- Reglas de seguridad de `firestore.rules`, publicadas.
- App web registrada; su configuración está en `frontend/.env.production`.

**Falta, y requiere tus cuentas:**

1. **Clave de la cuenta de servicio.** En Firebase: Configuración del proyecto > Cuentas de servicio > Generar nueva clave privada. Descarga un archivo `.json`. Es un secreto: no lo subas a GitHub ni lo pegues en un chat.
2. **Servidor en Render.** Crea una cuenta en render.com con tu GitHub, luego New > Blueprint > repositorio `aprenderSaber11` (usa `render.yaml`). Te pedirá tres valores:
   - `FIREBASE_SERVICE_ACCOUNT_JSON`: el contenido completo del archivo del paso 1.
   - `ADMIN_EMAILS`: tu correo.
   - `GROQ_API_KEY`: tu clave de Groq.
   En el plan gratuito el servidor se duerme tras un rato sin uso y la primera petición tarda cerca de un minuto en despertar. Si la dirección que te da Render no es `https://aprendersaber11-api.onrender.com`, cambia `VITE_API_URL` en `frontend/.env.production`.
3. **Web en Firebase Hosting.** Siempre desde la última versión de GitHub (no desde un .zip viejo: le falta `frontend/.env.production` y la web queda apuntando a los emuladores). La primera vez:
   ```
   git clone https://github.com/juanmelo20/aprenderSaber11.git
   cd aprenderSaber11
   npm install
   npm --prefix frontend install
   npx firebase login
   npm run desplegar:web
   ```
   Las siguientes veces basta `git pull` y `npm run desplegar:web`. Si falta la configuración, la compilación se detiene con un mensaje en vez de publicar una web rota. La web queda en https://aprendersaber11.web.app.
4. **Primer administrador.** En Firebase > Authentication > Usuarios, agrega tu correo con cualquier contraseña. En la app usa "Activar mi cuenta u olvidé la contraseña": al crear la contraseña desde el enlace, el correo queda verificado y entras como administrador.
5. **Banco.** Entra como administrador y pulsa "Cargar o actualizar banco semilla". Con `ALLOW_UNREVIEWED_ITEMS=false` (así queda en Render) los estudiantes solo ven preguntas y familias que un docente ya aprobó.
6. **Tutor.** Activa la retención cero de datos en la consola de Groq. El modelo es `openai/gpt-oss-120b`. Al probar la clave en noviembre de 2026, el plan gratuito permitía 1.000 consultas al día y 8.000 tokens por minuto (unas 10 por minuto); por eso cada estudiante tiene 10 consultas diarias al modelo y, pasado el límite, recibe las pistas escritas.
7. **Correos en español.** En Authentication > Plantillas, cambia el idioma de la plantilla de restablecimiento de contraseña.

## Lo que falta antes de usarla con estudiantes reales

- **Banco de lectura.** Es la tarea más grande que queda. Lectura Crítica tiene 79 preguntas de práctica y diagnóstico, y los casos de Sociales 66: alcanzan para pocas semanas sin repetir (ver la tabla). Para un año completo hacen falta varios cientos más, y todas deben pasar por un docente.
- **Revisión docente.** Todo el banco está en borrador: 311 preguntas escritas a mano, 102 ejemplos de las 51 familias y 70 variantes reservadas para los simulacros. Aprobar un ejemplo aprueba su familia. Los simulacros se muestran apenas se cargan, sin esperar la revisión.
- **Calibración.** La dificultad de cada pregunta es una estimación de quien la escribió. Los cortes de nivel usan los rangos de puntaje del ICFES, pero la escala de la app no está equiparada con la del examen: los niveles son orientativos hasta calibrar con respuestas reales (la colección `itemStats` ya las va acumulando).
- **Texto de autorización.** Debe revisarlo un abogado (Ley 1581 de 2012 y Decreto 1377 de 2013) antes de enviarlo a las familias.
- **Pagos.** No hay pasarela: el administrador activa cada licencia a mano después de recibir el pago.
- **Lo que no se ha probado.** La app publicada de punta a punta (falta el servidor en Render y subir la web), el envío de correos con Brevo y la imagen de Docker. El tutor y la redacción de borradores sí se probaron con el modelo real de Groq.
- **Privacidad del cuestionario de salida.** Para funcionar sin conexión, el plan guardado en el dispositivo incluye las claves de sus preguntas. Un estudiante con conocimientos técnicos podría verlas. El simulacro general no tiene ese problema: sus claves nunca salen del servidor antes de entregar.
- **Tablero docente.** Se calcula al abrirlo; con cientos de estudiantes conviene precalcular.

El sustento bibliográfico, el análisis de alternativas y los precios están en el documento de la propuesta, no aquí.
