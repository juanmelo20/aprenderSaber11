from __future__ import annotations

import datetime as dt

from fastapi import APIRouter, Depends, HTTPException
from google.cloud import firestore
from pydantic import BaseModel, Field

from .. import bank, learning, tutor
from ..config import settings
from ..db import clean, db
from ..security import learner

router = APIRouter(prefix="/api", tags=["estudiante"])


class Answer(BaseModel):
    itemId: str
    selected: str = Field(max_length=2)


class TutorAsk(BaseModel):
    planId: str
    sessionId: str
    itemId: str
    answered: bool = False
    selected: str | None = None
    question: str = Field(default="", max_length=400)


class SimSubmit(BaseModel):
    answers: dict[str, str | None]


@router.get("/overview")
def overview(user: dict = Depends(learner)):
    return clean(learning.overview(user["uid"]))


@router.post("/diagnostic/{area}/start")
def diagnostic_start(area: str, user: dict = Depends(learner)):
    return clean(learning.diagnostic_state(user["uid"], area.upper()))


@router.post("/diagnostic/{area}/answer")
def diagnostic_answer(area: str, body: Answer, user: dict = Depends(learner)):
    return clean(learning.diagnostic_answer(user["uid"], area.upper(), body.itemId, body.selected))


@router.post("/plan/ensure")
def plan_ensure(user: dict = Depends(learner)):
    plan = learning.ensure_plan(user["uid"])
    if not plan:
        raise HTTPException(409, "Completa al menos un diagnóstico para generar tu plan.")
    return {"id": plan["id"], "week": plan["week"]}


@router.post("/sync")
def sync(user: dict = Depends(learner)):
    return learning.sync(user["uid"])


@router.post("/tutor/ask")
def tutor_ask(body: TutorAsk, user: dict = Depends(learner)):
    uid = user["uid"]
    snap = db().collection("users").document(uid).collection("plans").document(body.planId).get()
    plan = snap.to_dict() if snap.exists else None
    session = next((s for s in (plan or {}).get("sessions", []) if s["id"] == body.sessionId), None)
    if not session or not any(it["id"] == body.itemId for it in session["items"]):
        raise HTTPException(404, "Esa pregunta no pertenece a tu plan.")
    if not session.get("tutor"):
        raise HTTPException(403, "El cuestionario de salida se responde sin ayudas.")
    item = bank.by_id().get(body.itemId) or next((it for it in session["items"] if it["id"] == body.itemId and it["id"].startswith("G.")), None)
    if not item:
        raise HTTPException(404, "Pregunta no encontrada.")
    usage_ref = db().collection("users").document(uid).collection("tutorUsage").document(dt.date.today().isoformat())
    usage = usage_ref.get()
    used = (usage.to_dict() or {}).get("count", 0) if usage.exists else 0
    if used >= settings.tutor_daily_limit:
        return {"reply": tutor.stored_reply(item, body.answered, body.selected), "source": "validado", "limit": True}
    result = tutor.ask(item, body.answered, body.selected, body.question)
    if result["source"] == "modelo":
        usage_ref.set({"count": firestore.Increment(1)}, merge=True)
        db().collection("progress").document(uid).set({"counters": {"tutorModel": firestore.Increment(1)}}, merge=True)
    return {**result, "limit": False}


@router.get("/simulacros")
def simulacros(user: dict = Depends(learner)):
    return clean(learning.list_simulacros(user["uid"]))


@router.get("/simulacros/{sim_id}")
def simulacro(sim_id: str, user: dict = Depends(learner)):
    return clean(learning.get_simulacro(user["uid"], sim_id))


@router.post("/simulacros/{sim_id}/submit")
def simulacro_submit(sim_id: str, body: SimSubmit, user: dict = Depends(learner)):
    return clean(learning.submit_simulacro(user["uid"], sim_id, {k: v for k, v in body.answers.items() if v}))
