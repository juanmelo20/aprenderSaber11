"""Configuración leída del entorno. Todos los valores tienen un default seguro para desarrollo."""
import os


def _bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in ("1", "true", "yes", "si", "sí")


def _list(name: str, default: str = "") -> list[str]:
    return [x.strip().lower() for x in os.getenv(name, default).split(",") if x.strip()]


class Settings:
    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "Rumbo 11")
        self.project_id = os.getenv("FIREBASE_PROJECT_ID", "demo-rumbo11")
        # JSON de la cuenta de servicio (contenido, no ruta). Vacío cuando se usan emuladores.
        self.service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON", "")
        self.emulators = bool(os.getenv("FIRESTORE_EMULATOR_HOST"))
        # Correos que entran como administrador. En producción se define en el entorno; nunca en el código.
        self.admin_emails = _list("ADMIN_EMAILS", "admin@rumbo11.test" if self.emulators else "")
        self.cors_origins = _list("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
        self.frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173").rstrip("/")

        # Tutor (GroqCloud, API compatible con OpenAI). Sin clave, el tutor usa solo pistas validadas.
        self.groq_api_key = os.getenv("GROQ_API_KEY", "")
        self.groq_model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
        # Solo para modelos con razonamiento (familia gpt-oss): "low" responde más rápido y gasta menos.
        self.groq_reasoning = os.getenv("GROQ_REASONING_EFFORT", "low")
        self.groq_url = os.getenv("GROQ_URL", "https://api.groq.com/openai/v1/chat/completions")
        self.tutor_daily_limit = int(os.getenv("TUTOR_DAILY_LIMIT", "10"))
        # El plan gratuito de Groq limita los tokens por minuto (8.000 al revisar en nov. 2026): unas 10 consultas.
        self.tutor_rpm = int(os.getenv("TUTOR_RPM", "10"))
        # Cada cuánto se vuelve a leer el banco desde Firestore (segundos). Leerlo cuesta una lectura por pregunta.
        self.bank_ttl = int(os.getenv("BANK_TTL", "21600"))

        # Correo opcional (Brevo). Sin clave, los enlaces se muestran para compartir.
        self.brevo_api_key = os.getenv("BREVO_API_KEY", "")
        self.mail_from = os.getenv("MAIL_FROM", "")

        # Diagnóstico adaptativo
        self.cat_min_items = int(os.getenv("CAT_MIN_ITEMS", "6"))
        self.cat_max_items = int(os.getenv("CAT_MAX_ITEMS", "10"))
        self.cat_se_target = float(os.getenv("CAT_SE_TARGET", "0.45"))

        # Plan semanal
        self.practice_items = int(os.getenv("PLAN_PRACTICE_ITEMS", "4"))
        self.exit_items_per_focus = int(os.getenv("PLAN_EXIT_ITEMS_PER_FOCUS", "2"))
        self.exit_pass = float(os.getenv("PLAN_EXIT_PASS", "0.6"))

        self.consent_version = os.getenv("CONSENT_VERSION", "2026-11")
        self.research_salt = os.getenv("RESEARCH_SALT", "cambia-esta-sal")
        # Permite usar el banco semilla sin revisión docente (solo desarrollo y pruebas internas).
        self.allow_unreviewed = _bool("ALLOW_UNREVIEWED_ITEMS", True)


settings = Settings()
