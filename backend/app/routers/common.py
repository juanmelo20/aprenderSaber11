from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from .. import people
from ..catalog import public_catalog
from ..config import settings
from ..db import clean, db
from ..security import LEARNERS, access_state, current_user

router = APIRouter(prefix="/api", tags=["común"])


class ConsentBody(BaseModel):
    guardianName: str = Field(max_length=120)
    relationship: str = Field(max_length=60)
    accept: bool


class SelfConsent(BaseModel):
    declaresAdult: bool
    accept: bool


@router.get("/health")
def health():
    return {"ok": True, "app": settings.app_name}


@router.get("/catalog")
def catalog():
    return public_catalog()


@router.get("/me")
def me(user: dict = Depends(current_user)):
    out = {k: user.get(k) for k in ("uid", "email", "displayName", "role", "status", "institutionId", "grade", "group", "areas", "adult")}
    out["access"] = access_state(user)
    out["hasConsent"] = bool(user.get("consent"))
    out["license"] = user.get("license")
    if user.get("institutionId"):
        inst = db().collection("institutions").document(user["institutionId"]).get()
        out["institutionName"] = inst.to_dict().get("name") if inst.exists else None
    return clean(out)


@router.post("/me/consent")
def my_consent(body: SelfConsent, user: dict = Depends(current_user)):
    if user.get("role") not in LEARNERS or not (body.accept and body.declaresAdult):
        return {"status": "sin_cambios"}
    return people.self_consent(user)


@router.post("/me/consent-link")
def my_consent_link(user: dict = Depends(current_user)):
    """Usuario particular menor de edad: genera el enlace para que su acudiente autorice."""
    if user.get("role") != "particular":
        return {"link": None}
    return {"link": people.create_consent_link(user["uid"], user.get("displayName") or "Estudiante", None)}


@router.get("/public/consent/{token}")
def consent_info(token: str):
    return people.consent_info(token)


@router.post("/public/consent/{token}")
def consent_accept(token: str, body: ConsentBody):
    if not body.accept:
        return {"status": "pendiente"}
    return people.accept_consent(token, body.guardianName, body.relationship)
