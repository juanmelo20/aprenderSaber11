# Rumbo 11 (nombre provisional)

Plataforma de preparación para la prueba Saber 11: diagnóstico adaptativo corto por área, plan de mejora semanal por estudiante, tutor que da pistas y no respuestas, simulacro general, y tableros para el docente de cada área y para el colegio.

Versión 0.1. Funciona completa en el computador con los emuladores de Firebase. Todavía no está publicada en internet: para eso faltan las cuentas reales (ver "Publicar").

El nombre se cambia sin tocar código: variable `APP_NAME` en el servidor y `VITE_APP_NAME` en la web.

## Qué hay en cada carpeta

| Carpeta | Qué es |
|---|---|
| `backend/` | Servidor en Python (FastAPI). Aquí vive toda la lógica: diagnóstico, plan, calificación, tutor, licencias, autorizaciones. |
| `backend/app/engine/` | Los tres motores: `irt.py` (diagnóstico adaptativo, modelo 3PL), `bkt.py` (dominio por competencia), `planner.py` (plan semanal). |
| `backend/app/seed/` | Banco de preguntas semilla (`bank_seed.py`) y familias de Matemáticas con números variables (`math_families.py`). |
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
cd backend && pytest                 # 26 pruebas: motores y flujo completo contra los emuladores
./e2e/correr.sh carpeta_capturas     # recorrido en Chrome (requiere `pip install playwright`); usa la web compilada: npm run build && npx vite preview --port 5173
```

## Cómo funciona

**Roles.** Administrador (crea colegios y licencias, activa planes individuales, exporta datos anónimos), institución (asigna el docente de cada área y registra estudiantes hasta el número de cupos), docente (ve el dominio de su grupo por competencia y aprueba preguntas), estudiante y particular.

**Autorización de datos.** Ningún estudiante puede empezar sin autorización. A los menores los autoriza su acudiente con un enlace que entrega el colegio; los mayores de edad autorizan al entrar. El servidor lo exige en cada petición, no solo la pantalla.

**Diagnóstico.** Entre 6 y 10 preguntas por área, elegidas según las respuestas anteriores. Entrega un puntaje estimado con su rango, no una cifra única: con tan pocas preguntas el margen es de unos 7 puntos hacia cada lado.

**Plan semanal.** Toma las tres competencias más débiles (máximo dos de la misma área), arma una práctica por cada una, un repaso de semanas anteriores y un cuestionario de salida sin ayudas. Con 60 % o más en la salida, la semana siguiente cambia de foco; con menos, refuerza los mismos temas con otras preguntas.

**Tutor.** Antes de responder solo orienta; después explica. Sin clave de Groq usa las pistas escritas para cada pregunta. Con clave, la respuesta del modelo pasa por un filtro que descarta cualquier texto que revele la opción correcta, y al modelo nunca se le envía nombre ni correo. En el cuestionario de salida y en el simulacro no hay tutor.

**Sin conexión.** El plan de la semana queda guardado en el dispositivo. Las prácticas se pueden responder sin señal y se envían solas al volver la conexión. El diagnóstico, el tutor con IA y el simulacro sí necesitan conexión.

**Simulacro general.** El mismo para todos, con tiempo, y con preguntas que no aparecen en las prácticas.

## Publicar (todo en planes gratuitos)

1. **Firebase.** Crear un proyecto en plan Spark. Activar Authentication (correo y contraseña) y Firestore. En Authentication > Plantillas, poner el correo de restablecimiento en español.
2. **Cuenta de servicio.** Configuración del proyecto > Cuentas de servicio > Generar clave privada. Ese archivo no se sube a GitHub: su contenido va en la variable `FIREBASE_SERVICE_ACCOUNT_JSON` del servidor.
3. **Servidor en Render.** New > Blueprint > este repositorio (usa `render.yaml`). Llenar las variables que describe `backend/.env.example`. En el plan gratuito el servidor se duerme tras un rato sin uso y la primera petición tarda cerca de un minuto en despertar.
4. **Web en Firebase Hosting.** Copiar `frontend/.env.example` como `frontend/.env.production`, llenarlo, y luego `npx firebase login`, `npx firebase use --add` y `npm run desplegar:web` (publica la web y las reglas de Firestore).
5. **Primer administrador.** Poner el correo en `ADMIN_EMAILS`, crear ese usuario en Firebase > Authentication, y en la app usar "Activar mi cuenta u olvidé la contraseña". Al crear la contraseña desde el enlace, el correo queda verificado y la cuenta entra como administrador.
6. **Banco.** Entrar como administrador y pulsar "Cargar o actualizar banco semilla". Con `ALLOW_UNREVIEWED_ITEMS=false` los estudiantes solo ven preguntas que un docente ya aprobó.
7. **Tutor.** Crear una clave gratuita en GroqCloud, activar la retención cero de datos en su consola y ponerla en `GROQ_API_KEY`.

## Lo que falta antes de usarla con estudiantes reales

- **Banco de preguntas.** Es la tarea más grande. Hay 103 preguntas (80 escritas a mano y 23 generadas por familias de Matemáticas), todas en estado borrador. Alcanza para probar, no para un grado completo: en Lectura, Sociales y Naturales hay apenas 14 preguntas de diagnóstico y práctica por área, así que desde la segunda semana se repiten. Para el piloto se necesitan del orden de 40 o más por competencia, revisadas por docentes. Se agregan en `backend/app/seed/bank_seed.py` y se cargan con el botón del administrador; las ya aprobadas no se sobrescriben.
- **Calibración.** La dificultad de cada pregunta es una estimación de quien la escribió. Los cortes de nivel usan los rangos de puntaje del ICFES, pero la escala de la app no está equiparada con la del examen: los niveles son orientativos hasta calibrar con respuestas reales (la colección `itemStats` ya las va acumulando).
- **Texto de autorización.** Debe revisarlo un abogado (Ley 1581 de 2012 y Decreto 1377 de 2013) antes de enviarlo a las familias.
- **Pagos.** No hay pasarela: el administrador activa cada licencia a mano después de recibir el pago.
- **Lo que no se ha probado.** El despliegue real en Firebase, Render y Groq (falta crear las cuentas), el tutor con el modelo real (está probado con un modelo simulado), el envío de correos con Brevo y la imagen de Docker.
- **Privacidad del cuestionario de salida.** Para funcionar sin conexión, el plan guardado en el dispositivo incluye las claves de sus preguntas. Un estudiante con conocimientos técnicos podría verlas. El simulacro general no tiene ese problema: sus claves nunca salen del servidor antes de entregar.
- **Tablero docente.** Se calcula al abrirlo; con cientos de estudiantes conviene precalcular.

El sustento bibliográfico, el análisis de alternativas y los precios están en el documento de la propuesta, no aquí.
