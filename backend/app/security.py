"""Autenticación (token de Firebase) y autorización por rol."""
from __future__ import annotations

import datetime as dt

from fastapi import Depends, Header, HTTPException

from .config import settings
from .db import auth, db, now

ROLES = ("admin", "institucion", "docente", "estudiante", "particular")
LEARNERS = ("estudiante", "particular")


def _bootstrap(decoded: dict) -> dict:
    """Primera vez que alguien entra sin perfil: administrador (si su correo está en ADMIN_EMAILS
    y está verificado) o usuario particular pendiente de autorización y licencia."""
    email = (decoded.get("email") or "").lower()
    verified = bool(decoded.get("email_verified")) or settings.emulators
    base = {"email": email, "displayName": decoded.get("name") or email.split("@")[0], "createdAt": now()}
    if email and email in settings.admin_emails and verified:
        profile = {**base, "role": "admin", "status": "activo"}
    else:
        profile = {**base, "role": "particular", "status": "pendiente_consentimiento"}
    db().collection("users").document(decoded["uid"]).set(profile)
    return profile


def current_user(authorization: str | None = Header(default=None)) -> dict:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(401, "Falta el token de sesión.")
    try:
        decoded = auth().verify_id_token(authorization.split(" ", 1)[1])
    except Exception as exc:  # token inválido o vencido
        raise HTTPException(401, "Sesión inválida o vencida.") from exc
    snap = db().collection("users").document(decoded["uid"]).get()
    profile = snap.to_dict() if snap.exists else _bootstrap(decoded)
    # Un administrador que creó su cuenta antes de verificar el correo queda como particular;
    # se asciende en cuanto entra con el correo verificado.
    if profile.get("role") == "particular" and (profile.get("email") or "") in settings.admin_emails \
            and (decoded.get("email_verified") or settings.emulators):
        profile.update(role="admin", status="activo")
        snap.reference.update({"role": "admin", "status": "activo"})
    profile["uid"] = decoded["uid"]
    return profile


def require(*roles: str):
    def dep(user: dict = Depends(current_user)) -> dict:
        if user.get("role") not in roles:
            raise HTTPException(403, "Tu rol no tiene permiso para esta acción.")
        if user.get("status") == "suspendido":
            raise HTTPException(403, "Cuenta suspendida.")
        return user

    return dep


def _expired(value) -> bool:
    if not value:
        return True
    if isinstance(value, str):
        try:
            value = dt.datetime.fromisoformat(value)
        except ValueError:
            return True
    if value.tzinfo is None:
        value = value.replace(tzinfo=dt.timezone.utc)
    return value < now()


def access_state(user: dict) -> dict:
    """Por qué un estudiante puede o no usar la plataforma. Lo consume el frontend para guiarlo."""
    role = user.get("role")
    if role not in LEARNERS:
        return {"ok": user.get("status") == "activo", "reason": None if user.get("status") == "activo" else "inactivo"}
    if not user.get("consent"):
        return {"ok": False, "reason": "consentimiento"}
    if role == "estudiante":
        inst = db().collection("institutions").document(user.get("institutionId", "-")).get()
        data = inst.to_dict() if inst.exists else None
        if not data or data.get("status") != "activa" or _expired(data.get("licenseExpires")):
            return {"ok": False, "reason": "licencia_institucion"}
        return {"ok": True, "reason": None}
    lic = user.get("license") or {}
    if _expired(lic.get("expires")):
        return {"ok": False, "reason": "licencia"}
    return {"ok": True, "reason": None}


def learner(user: dict = Depends(require(*LEARNERS))) -> dict:
    state = access_state(user)
    if not state["ok"]:
        raise HTTPException(403, {"code": state["reason"], "message": "Tu acceso aún no está activo."})
    return user
