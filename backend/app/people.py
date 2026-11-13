"""Instituciones, licencias, cuentas y autorización de tratamiento de datos (Ley 1581 de 2012)."""
from __future__ import annotations

import datetime as dt
import hashlib
import re
import secrets

import httpx
from fastapi import HTTPException
from google.cloud.firestore_v1.base_query import FieldFilter

from .catalog import AREAS
from .config import settings
from .db import auth, db, now

EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")


def _users():
    return db().collection("users")


def _parse_date(value: str) -> dt.datetime:
    try:
        d = dt.datetime.fromisoformat(value)
    except ValueError as exc:
        raise HTTPException(422, "Fecha inválida; usa el formato AAAA-MM-DD.") from exc
    return d.replace(tzinfo=dt.timezone.utc) if d.tzinfo is None else d


def get_or_create_auth_user(email: str, name: str) -> tuple[str, bool]:
    email = email.strip().lower()
    if not EMAIL_RE.match(email):
        raise HTTPException(422, f"Correo inválido: {email}")
    try:
        return auth().get_user_by_email(email).uid, False
    except auth().UserNotFoundError:
        return auth().create_user(email=email, display_name=name.strip() or None).uid, True


def activation_link(email: str) -> str | None:
    """Enlace para que la persona cree su contraseña. También puede pedirlo desde la app
    ('Activar mi cuenta'), y en ese caso el correo lo envía Firebase sin costo."""
    try:
        return auth().generate_password_reset_link(email)
    except Exception:
        return None


def send_mail(to: str, subject: str, html: str) -> bool:
    if not (settings.brevo_api_key and settings.mail_from):
        return False
    try:
        r = httpx.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={"api-key": settings.brevo_api_key},
            json={"sender": {"email": settings.mail_from, "name": settings.app_name}, "to": [{"email": to}],
                  "subject": subject, "htmlContent": html},
            timeout=15,
        )
        return r.status_code < 300
    except Exception:
        return False


# ---------- instituciones ----------

def create_institution(name: str, municipality: str, seats: int, expires: str, admin_email: str, admin_name: str, plan: str) -> dict:
    if seats < 1:
        raise HTTPException(422, "La licencia debe tener al menos un cupo.")
    uid, _ = get_or_create_auth_user(admin_email, admin_name)
    existing = _users().document(uid).get()
    if existing.exists and existing.to_dict().get("role") not in (None, "particular", "institucion"):
        raise HTTPException(409, "Ese correo ya tiene otro rol en la plataforma.")
    ref = db().collection("institutions").document()
    ref.set({
        "name": name.strip(), "municipality": municipality.strip(), "plan": plan, "licenseSeats": seats,
        "seatsUsed": 0, "licenseExpires": _parse_date(expires), "status": "activa", "teacherByArea": {},
        "createdAt": now(),
    })
    _users().document(uid).set({
        "email": admin_email.strip().lower(), "displayName": admin_name.strip(), "role": "institucion",
        "status": "activo", "institutionId": ref.id, "createdAt": now(),
    })
    link = activation_link(admin_email.strip().lower())
    send_mail(admin_email, f"Acceso de tu institución a {settings.app_name}",
              f"<p>Hola {admin_name}:</p><p>Crea tu contraseña aquí: <a href='{link}'>{link}</a></p>")
    return {"id": ref.id, "adminUid": uid, "activationLink": link}


def institution_of(user: dict, institution_id: str | None = None) -> tuple[str, dict]:
    inst_id = institution_id if user["role"] == "admin" and institution_id else user.get("institutionId")
    if not inst_id:
        raise HTTPException(400, "No hay institución asociada.")
    snap = db().collection("institutions").document(inst_id).get()
    if not snap.exists:
        raise HTTPException(404, "Institución no encontrada.")
    return inst_id, snap.to_dict()


def add_teacher(inst_id: str, email: str, name: str, areas: list[str]) -> dict:
    bad = [a for a in areas if a not in AREAS]
    if bad or not areas:
        raise HTTPException(422, "Indica al menos un área válida para el docente.")
    uid, _ = get_or_create_auth_user(email, name)
    snap = _users().document(uid).get()
    if snap.exists and snap.to_dict().get("role") not in ("docente", "particular") :
        raise HTTPException(409, "Ese correo ya tiene otro rol en la plataforma.")
    if snap.exists and snap.to_dict().get("role") == "docente" and snap.to_dict().get("institutionId") != inst_id:
        raise HTTPException(409, "Ese docente pertenece a otra institución.")
    _users().document(uid).set({
        "email": email.strip().lower(), "displayName": name.strip(), "role": "docente", "status": "activo",
        "institutionId": inst_id, "areas": areas, "createdAt": now(),
    })
    inst_ref = db().collection("institutions").document(inst_id)
    teacher_by_area = inst_ref.get().to_dict().get("teacherByArea", {})
    for area, t_uid in list(teacher_by_area.items()):  # un docente responsable por área
        if t_uid == uid and area not in areas:
            teacher_by_area.pop(area)
    for area in areas:
        teacher_by_area[area] = uid
    inst_ref.update({"teacherByArea": teacher_by_area})
    return {"uid": uid, "activationLink": activation_link(email.strip().lower())}


def add_students(inst_id: str, inst: dict, rows: list[dict]) -> list[dict]:
    free = inst["licenseSeats"] - inst.get("seatsUsed", 0)
    results, created = [], 0
    for row in rows:
        email = (row.get("email") or "").strip().lower()
        name = (row.get("name") or "").strip()
        out = {"email": email, "name": name, "ok": False}
        try:
            if not name:
                raise HTTPException(422, "Falta el nombre.")
            if created >= free:
                raise HTTPException(409, "No quedan cupos en la licencia.")
            uid, _ = get_or_create_auth_user(email, name)
            snap = _users().document(uid).get()
            if snap.exists and snap.to_dict().get("role") != "particular":
                raise HTTPException(409, "Ese correo ya está registrado.")
            adult = bool(row.get("adult"))
            _users().document(uid).set({
                "email": email, "displayName": name, "role": "estudiante", "status": "pendiente_consentimiento",
                "institutionId": inst_id, "grade": str(row.get("grade") or "11"), "group": str(row.get("group") or "A"),
                "adult": adult, "createdAt": now(),
            })
            db().collection("progress").document(uid).set({
                "institutionId": inst_id, "grade": str(row.get("grade") or "11"), "group": str(row.get("group") or "A"),
            }, merge=True)
            out.update(ok=True, uid=uid, activationLink=activation_link(email))
            if not adult:
                out["consentLink"] = create_consent_link(uid, name, inst["name"])
                guardian = (row.get("guardianEmail") or "").strip().lower()
                if guardian and EMAIL_RE.match(guardian):
                    send_mail(guardian, f"Autorización para {name} en {settings.app_name}",
                              f"<p>La institución {inst['name']} registró a {name}. Para activar su cuenta, "
                              f"revise y autorice el tratamiento de datos: <a href='{out['consentLink']}'>{out['consentLink']}</a></p>")
            created += 1
        except HTTPException as exc:
            out["error"] = exc.detail if isinstance(exc.detail, str) else "No se pudo registrar."
        results.append(out)
    if created:
        db().collection("institutions").document(inst_id).update({"seatsUsed": inst.get("seatsUsed", 0) + created})
    return results


def list_members(inst_id: str) -> dict:
    students, teachers = [], []
    for snap in _users().where(filter=FieldFilter("institutionId", "==", inst_id)).stream():
        d = snap.to_dict()
        row = {"uid": snap.id, "name": d.get("displayName"), "email": d.get("email"), "status": d.get("status")}
        if d.get("role") == "estudiante":
            students.append({**row, "grade": d.get("grade"), "group": d.get("group"), "consent": bool(d.get("consent"))})
        elif d.get("role") == "docente":
            teachers.append({**row, "areas": d.get("areas", [])})
    students.sort(key=lambda r: (r["grade"] or "", r["group"] or "", r["name"] or ""))
    return {"students": students, "teachers": teachers}


# ---------- autorización de tratamiento de datos ----------

def create_consent_link(uid: str, student_name: str, institution_name: str | None) -> str:
    token = secrets.token_urlsafe(24)
    db().collection("consents").document(token).set({
        "uid": uid, "studentFirstName": student_name.split(" ")[0], "institutionName": institution_name,
        "status": "pendiente", "version": settings.consent_version, "createdAt": now(),
    })
    return f"{settings.frontend_url}/autorizacion/{token}"


def consent_info(token: str) -> dict:
    snap = db().collection("consents").document(token).get()
    if not snap.exists:
        raise HTTPException(404, "Este enlace de autorización no existe.")
    d = snap.to_dict()
    return {"studentFirstName": d["studentFirstName"], "institutionName": d.get("institutionName"),
            "status": d["status"], "version": d["version"], "appName": settings.app_name}


def accept_consent(token: str, guardian_name: str, relationship: str) -> dict:
    ref = db().collection("consents").document(token)
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(404, "Este enlace de autorización no existe.")
    d = snap.to_dict()
    if d["status"] == "aceptado":
        return {"status": "aceptado"}
    if len(guardian_name.strip()) < 5 or not relationship.strip():
        raise HTTPException(422, "Escribe el nombre completo de quien autoriza y su parentesco.")
    consent = {"by": "acudiente", "guardianName": guardian_name.strip(), "relationship": relationship.strip(),
               "version": d["version"], "acceptedAt": now()}
    _users().document(d["uid"]).update({"consent": consent, "status": "activo"})
    ref.update({"status": "aceptado", "acceptedAt": now()})
    return {"status": "aceptado"}


def self_consent(user: dict) -> dict:
    """Autorización propia: solo para quien declara ser mayor de edad."""
    if user["role"] == "estudiante" and not user.get("adult"):
        raise HTTPException(403, "Tu institución te registró como menor de edad: debe autorizar tu acudiente.")
    consent = {"by": "titular", "declaresAdult": True, "version": settings.consent_version, "acceptedAt": now()}
    _users().document(user["uid"]).update({"consent": consent, "status": "activo"})
    return {"status": "aceptado"}


def grant_license(email: str, plan: str, expires: str) -> dict:
    try:
        uid = auth().get_user_by_email(email.strip().lower()).uid
    except auth().UserNotFoundError as exc:
        raise HTTPException(404, "Esa persona aún no se ha registrado en la app.") from exc
    snap = _users().document(uid).get()
    if not snap.exists or snap.to_dict().get("role") != "particular":
        raise HTTPException(409, "La licencia individual solo aplica a usuarios particulares.")
    _users().document(uid).update({"license": {"plan": plan, "expires": _parse_date(expires), "grantedAt": now()}})
    return {"uid": uid}


def research_id(uid: str) -> str:
    return hashlib.sha256(f"{settings.research_salt}:{uid}".encode()).hexdigest()[:16]
