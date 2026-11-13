"""Institución (administra cupos, docentes y estudiantes) y docente (ve en qué va flojo su grupo)."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from google.cloud.firestore_v1.base_query import FieldFilter
from pydantic import BaseModel, Field

from .. import bank, people
from ..catalog import AREAS, TEACHING_TIPS, comp_key
from ..db import clean, db, now
from ..security import require

router = APIRouter(prefix="/api", tags=["institución y docente"])


class StudentRow(BaseModel):
    name: str = Field(max_length=120)
    email: str = Field(max_length=160)
    grade: str = "11"
    group: str = "A"
    adult: bool = False
    guardianEmail: str | None = None


class StudentsBody(BaseModel):
    students: list[StudentRow] = Field(max_length=200)


class TeacherBody(BaseModel):
    name: str = Field(max_length=120)
    email: str = Field(max_length=160)
    areas: list[str]


class ItemPatch(BaseModel):
    context: str | None = None
    stem: str | None = None
    options: dict[str, str] | None = None
    correct: str | None = None
    explanation: str | None = None
    hints: list[str] | None = None
    status: str | None = None


@router.get("/institution")
def institution(institutionId: str | None = None, user: dict = Depends(require("institucion", "admin"))):
    inst_id, inst = people.institution_of(user, institutionId)
    return clean({"id": inst_id, **inst, **people.list_members(inst_id)})


@router.post("/institution/students")
def add_students(body: StudentsBody, institutionId: str | None = None, user: dict = Depends(require("institucion", "admin"))):
    inst_id, inst = people.institution_of(user, institutionId)
    return {"results": people.add_students(inst_id, inst, [r.model_dump() for r in body.students])}


@router.post("/institution/teachers")
def add_teacher(body: TeacherBody, institutionId: str | None = None, user: dict = Depends(require("institucion", "admin"))):
    inst_id, _ = people.institution_of(user, institutionId)
    return people.add_teacher(inst_id, body.email, body.name, [a.upper() for a in body.areas])


@router.post("/institution/students/{uid}/consent-link")
def renew_consent_link(uid: str, institutionId: str | None = None, user: dict = Depends(require("institucion", "admin"))):
    inst_id, inst = people.institution_of(user, institutionId)
    snap = db().collection("users").document(uid).get()
    if not snap.exists or snap.to_dict().get("institutionId") != inst_id:
        raise HTTPException(404, "Estudiante no encontrado.")
    d = snap.to_dict()
    return {"consentLink": people.create_consent_link(uid, d.get("displayName", "Estudiante"), inst["name"]),
            "activationLink": people.activation_link(d["email"])}


@router.get("/teacher/overview")
def teacher_overview(area: str, group: str | None = None, user: dict = Depends(require("docente", "institucion", "admin"))):
    area = area.upper()
    if area not in AREAS:
        raise HTTPException(404, "Área desconocida.")
    if user["role"] == "docente" and area not in user.get("areas", []):
        raise HTTPException(403, "No tienes asignada esa área.")
    inst_id, inst = people.institution_of(user)
    names = {s["uid"]: s for s in people.list_members(inst_id)["students"]}
    comps = list(AREAS[area]["competencias"].keys())
    rows, sums, counts, levels, groups = [], {c: 0.0 for c in comps}, {c: 0 for c in comps}, {}, set()
    for snap in db().collection("progress").where(filter=FieldFilter("institutionId", "==", inst_id)).stream():
        p = snap.to_dict()
        info = names.get(snap.id)
        if not info:
            continue
        groups.add(f"{info['grade']}{info['group']}")
        if group and f"{info['grade']}{info['group']}" != group:
            continue
        res = (p.get("thetas") or {}).get(area)
        mastery = {c: (p.get("mastery") or {}).get(comp_key(area, c)) for c in comps}
        for c, v in mastery.items():
            if v is not None:
                sums[c] += v
                counts[c] += 1
        if res:
            levels[res["level"]] = levels.get(res["level"], 0) + 1
        rows.append({"uid": snap.id, "name": info["name"], "group": f"{info['grade']}{info['group']}",
                     "score": res["score"] if res else None, "level": res["level"] if res else None,
                     "mastery": mastery, "week": p.get("week", 0), "attempts": (p.get("counters") or {}).get("attempts", 0)})
    comp_avg = [{"key": c, "label": AREAS[area]["competencias"][c][0],
                 "avg": round(sums[c] / counts[c], 3) if counts[c] else None, "n": counts[c]} for c in comps]
    weakest = sorted((c for c in comp_avg if c["avg"] is not None), key=lambda c: c["avg"])[:2]
    items = bank.by_id()
    hard = []
    for snap in db().collection("itemStats").where(filter=FieldFilter("area", "==", area)).stream():
        s = snap.to_dict()
        if s.get("n", 0) >= 3 and snap.id in items:
            it = items[snap.id]
            hard.append({"id": snap.id, "stem": it["stem"], "competencia": AREAS[area]["competencias"][it["competencia"]][0],
                         "n": s["n"], "pct": round(100 * s.get("correct", 0) / s["n"])})
    hard = sorted(hard, key=lambda h: h["pct"])[:5]
    rows.sort(key=lambda r: (r["score"] is None, r["score"] if r["score"] is not None else 0))
    return clean({
        "area": area, "areaName": AREAS[area]["name"], "institution": inst["name"], "groups": sorted(groups),
        "students": rows, "diagnosed": sum(1 for r in rows if r["score"] is not None),
        "competencias": comp_avg, "levels": levels, "levelOrder": AREAS[area]["levels"],
        "classPlan": [{"competencia": w["label"], "avg": w["avg"], "tips": TEACHING_TIPS.get(comp_key(area, w["key"]), [])} for w in weakest],
        "hardItems": hard,
    })


@router.get("/items")
def list_items(area: str, status: str | None = None, user: dict = Depends(require("docente", "admin"))):
    area = area.upper()
    if user["role"] == "docente" and area not in user.get("areas", []):
        raise HTTPException(403, "No tienes asignada esa área.")
    out = [it for it in bank.all_items(force=True) if it["area"] == area and (not status or it.get("status") == status)]
    return sorted(out, key=lambda it: (it.get("status", ""), it["competencia"], it["id"]))


@router.patch("/items/{item_id}")
def patch_item(item_id: str, body: ItemPatch, user: dict = Depends(require("docente", "admin"))):
    ref = db().collection("items").document(item_id)
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(404, "Pregunta no encontrada.")
    item = snap.to_dict()
    if user["role"] == "docente" and item["area"] not in user.get("areas", []):
        raise HTTPException(403, "No tienes asignada esa área.")
    changes = {k: v for k, v in body.model_dump().items() if v is not None}
    if "status" in changes and changes["status"] not in ("borrador", "publicado", "descartado"):
        raise HTTPException(422, "Estado inválido.")
    merged = {**item, **changes}
    if merged["correct"] not in merged["options"]:
        raise HTTPException(422, "La clave debe ser una de las opciones.")
    if changes.get("status") == "publicado":
        changes.update(reviewedBy=user["uid"], reviewedAt=now())
    ref.update(changes)
    bank.invalidate()
    return {"ok": True}
