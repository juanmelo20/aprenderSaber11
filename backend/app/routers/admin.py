"""Administrador de la plataforma: instituciones, licencias, banco de ítems y datos anonimizados de investigación."""
from __future__ import annotations

from fastapi import APIRouter, Depends
from google.cloud.firestore_v1.base_query import FieldFilter
from pydantic import BaseModel, Field

from .. import bank, drafts, people
from ..catalog import AREA_ORDER
from ..db import clean, db
from ..seed import loader
from ..security import require
from ..seed import families

router = APIRouter(prefix="/api/admin", tags=["administrador"])
admin = require("admin")


class InstitutionBody(BaseModel):
    name: str = Field(min_length=3, max_length=160)
    municipality: str = Field(max_length=120)
    seats: int = Field(ge=1, le=5000)
    expires: str
    adminEmail: str
    adminName: str = Field(max_length=120)
    plan: str = "institucional"


class LicenseBody(BaseModel):
    email: str
    plan: str = "mensual"
    expires: str


@router.get("/institutions")
def institutions(user: dict = Depends(admin)):
    out = []
    for snap in db().collection("institutions").stream():
        out.append({"id": snap.id, **snap.to_dict()})
    return clean(sorted(out, key=lambda i: i["name"]))


@router.post("/institutions")
def create_institution(body: InstitutionBody, user: dict = Depends(admin)):
    return people.create_institution(body.name, body.municipality, body.seats, body.expires, body.adminEmail, body.adminName, body.plan)


@router.get("/particulares")
def particulares(user: dict = Depends(admin)):
    out = []
    for snap in db().collection("users").where(filter=FieldFilter("role", "==", "particular")).stream():
        d = snap.to_dict()
        out.append({"uid": snap.id, "email": d.get("email"), "name": d.get("displayName"),
                    "consent": bool(d.get("consent")), "license": d.get("license")})
    return clean(out)


@router.post("/licenses")
def grant_license(body: LicenseBody, user: dict = Depends(admin)):
    return people.grant_license(body.email, body.plan, body.expires)


@router.get("/items/stats")
def items_stats(user: dict = Depends(admin)):
    stats: dict = {}
    for it in bank.all_items(force=True):
        slot = stats.setdefault(it["area"], {})
        key = f"{it['pool']}/{it.get('status')}"
        slot[key] = slot.get(key, 0) + 1
    fams: dict = {}
    for name, (area, _) in families.REGISTRY.items():
        fams[area] = fams.get(area, 0) + 1
    approved = bank.approved_families()
    return {"total": len(bank.all_items()), "byArea": stats, "familiesByArea": fams,
            "familiesApproved": {a: sum(1 for n in approved if families.REGISTRY[n][0] == a) for a in fams}}


@router.post("/items/seed")
def seed_items(user: dict = Depends(admin)):
    """Carga (o actualiza) el banco semilla y el simulacro general. No pisa ítems ya revisados."""
    return loader.load_seed()


@router.get("/research/export")
def research_export(user: dict = Depends(admin)):
    """Datos para el trabajo de grado, sin nombres ni correos: identificador con hash y sal."""
    inst_names = {s.id: s.to_dict().get("name") for s in db().collection("institutions").stream()}
    rows = []
    for snap in db().collection("progress").stream():
        p = snap.to_dict()
        thetas = p.get("thetas") or {}
        row = {"id": people.research_id(snap.id), "institucion": inst_names.get(p.get("institutionId"), "particular"),
               "grado": p.get("grade"), "grupo": p.get("group"), "semana": p.get("week", 0)}
        for area in AREA_ORDER:
            res = thetas.get(area) or {}
            row[f"{area}_theta"] = res.get("theta")
            row[f"{area}_puntaje"] = res.get("score")
            row[f"{area}_nivel"] = res.get("level")
        row.update({f"dominio_{k}": v for k, v in sorted((p.get("mastery") or {}).items())})
        row.update({f"conteo_{k}": v for k, v in (p.get("counters") or {}).items()})
        rows.append(row)
    return clean({"rows": rows})


@router.post("/items/draft/{area}")
def draft_items(area: str, user: dict = Depends(admin)):
    """Redacta borradores con el modelo de lenguaje para la competencia con menos preguntas del área."""
    return drafts.create(area.upper())
