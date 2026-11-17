"""Lógica de aprendizaje: diagnóstico adaptativo, plan semanal, sincronización de intentos y simulacro."""
from __future__ import annotations

import random

from fastapi import HTTPException
from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

from . import bank
from .catalog import AREAS, AREA_ORDER, comp_key, level_for
from .config import settings
from .db import db, now
from .engine import bkt, irt, planner
from .seed import families


# ---------- progreso ----------

def progress_ref(uid: str):
    return db().collection("progress").document(uid)


def get_progress(uid: str) -> dict:
    snap = progress_ref(uid).get()
    data = snap.to_dict() if snap.exists else {}
    data.setdefault("thetas", {})
    data.setdefault("mastery", {})
    data.setdefault("seen", [])
    data.setdefault("week", 0)
    data.setdefault("focusHistory", [])
    data.setdefault("counters", {})
    return data


def _area_result(theta: float, se: float, n: int, area: str) -> dict:
    score = irt.score_from_theta(theta)
    margin = round(10 * se)  # un error estándar en la escala de puntaje: con pocas preguntas el rango es amplio
    return {"theta": round(theta, 3), "se": round(se, 3), "n": n, "score": score, "low": max(0, score - margin), "high": min(100, score + margin),
            "level": level_for(area, score), "updatedAt": now()}


# ---------- diagnóstico adaptativo ----------

def _diag_ref(uid: str, area: str):
    return db().collection("users").document(uid).collection("diagnostics").document(area)


def _diag_pool(area: str) -> list[dict]:
    return [it for it in bank.usable_items() if it["area"] == area and it["pool"] == "diagnostico"]


def _weights(area: str) -> dict[str, float]:
    return {c: w for c, (_, w) in AREAS[area]["competencias"].items()}


def diagnostic_state(uid: str, area: str) -> dict:
    if area not in AREAS:
        raise HTTPException(404, "Área desconocida.")
    ref = _diag_ref(uid, area)
    snap = ref.get()
    state = snap.to_dict() if snap.exists else {"status": "en_curso", "administered": [], "theta": 0.0, "se": 1.0, "currentItemId": None}
    if state["status"] == "terminado":
        return {"done": True, "result": state.get("result")}
    pool = _diag_pool(area)
    by_id = {it["id"]: it for it in pool}
    if not state.get("currentItemId") or state["currentItemId"] not in by_id:
        used = {a["itemId"] for a in state["administered"]}
        nxt = irt.select_next(state["theta"], [it for it in pool if it["id"] not in used], state["administered"], _weights(area))
        if nxt is None:
            if not state["administered"]:
                raise HTTPException(409, "Aún no hay preguntas de diagnóstico publicadas para esta área.")
            return _finish_diagnostic(uid, area, state)
        state["currentItemId"] = nxt["id"]
        ref.set(state)
    total = min(settings.cat_max_items, len(pool))
    return {"done": False, "item": bank.public_item(by_id[state["currentItemId"]]), "n": len(state["administered"]) + 1, "max": total}


def diagnostic_answer(uid: str, area: str, item_id: str, selected: str) -> dict:
    ref = _diag_ref(uid, area)
    snap = ref.get()
    if not snap.exists:
        raise HTTPException(409, "Primero inicia el diagnóstico.")
    state = snap.to_dict()
    if state["status"] == "terminado":
        return {"done": True, "result": state.get("result")}
    if state.get("currentItemId") != item_id:
        raise HTTPException(409, "Esa no es la pregunta actual.")
    item = bank.by_id().get(item_id)
    if not item:
        raise HTTPException(404, "Pregunta no encontrada.")
    state["administered"].append({
        "itemId": item_id,
        "competencia": item["competencia"],
        "a": item.get("a", 1.0), "b": item.get("b", 0.0), "c": item.get("c", 0.25),
        "selected": selected,
        "correct": selected == item["correct"],
    })
    theta, se = irt.eap([(a["a"], a["b"], a["c"], a["correct"]) for a in state["administered"]])
    state.update(theta=theta, se=se, currentItemId=None)
    used = {a["itemId"] for a in state["administered"]}
    remaining = [it for it in _diag_pool(area) if it["id"] not in used]
    if irt.should_stop(len(state["administered"]), se, len(remaining), settings.cat_min_items, settings.cat_max_items, settings.cat_se_target):
        return _finish_diagnostic(uid, area, state)
    ref.set(state)
    return diagnostic_state(uid, area)


def _finish_diagnostic(uid: str, area: str, state: dict) -> dict:
    theta, se, n = state["theta"], state["se"], len(state["administered"])
    result = _area_result(theta, se, n, area)
    mastery_updates = {}
    for comp in AREAS[area]["competencias"]:
        answered = [a for a in state["administered"] if a["competencia"] == comp]
        mastery_updates[comp_key(area, comp)] = round(bkt.init_from_diagnostic(theta, sum(a["correct"] for a in answered), len(answered)), 3)
    state.update(status="terminado", currentItemId=None, result=result, finishedAt=now())
    _diag_ref(uid, area).set(state)
    progress = get_progress(uid)
    progress["thetas"][area] = result
    progress["mastery"].update(mastery_updates)
    progress["seen"] = sorted(set(progress["seen"]) | {a["itemId"] for a in state["administered"]})
    progress_ref(uid).set(progress, merge=True)
    return {"done": True, "result": result}


# ---------- plan semanal ----------

def _plans(uid: str):
    return db().collection("users").document(uid).collection("plans")


def active_plan(uid: str) -> tuple[str, dict] | None:
    for snap in _plans(uid).where(filter=FieldFilter("status", "==", "activo")).limit(1).stream():
        return snap.id, snap.to_dict()
    return None


def ensure_plan(uid: str, repeat_focus: list[str] | None = None, progress: dict | None = None) -> dict | None:
    current = active_plan(uid)
    if current:
        return {"id": current[0], **current[1]}
    progress = progress or get_progress(uid)
    if not progress["thetas"]:
        return None
    thetas = {a: v["theta"] for a, v in progress["thetas"].items()}
    plan = planner.build_plan(
        week=progress["week"] + 1,
        mastery=progress["mastery"],
        thetas=thetas,
        # Banco revisado más variantes recién generadas que este estudiante no ha visto.
        items=bank.usable_items() + bank.fresh_variants(uid, progress["week"] + 1, set(progress["seen"])),
        seen=set(progress["seen"]),
        previous_focus=progress["focusHistory"],
        practice_n=settings.practice_items,
        exit_n=settings.exit_items_per_focus,
        repeat_focus=repeat_focus,
    )
    if not plan:
        return None
    plan["createdAt"] = now()
    ref = _plans(uid).document(f"semana-{plan['week']:03d}")
    ref.set(plan)
    progress_ref(uid).set({"week": plan["week"]}, merge=True)
    return {"id": ref.id, **plan}


def sync(uid: str) -> dict:
    """Procesa los intentos que el estudiante guardó (incluso sin conexión): califica con el banco,
    actualiza el dominio por competencia y, si terminó el plan, genera el de la semana siguiente."""
    attempts_ref = db().collection("users").document(uid).collection("attempts")
    pending = sorted(
        ((s.id, s.to_dict()) for s in attempts_ref.where(filter=FieldFilter("processed", "==", False)).stream()),
        key=lambda x: str(x[1].get("finishedAt") or ""),
    )
    summary = {"processed": 0, "planCompleted": False, "exitPassed": None, "newPlan": False}
    if not pending:
        return summary
    items = bank.by_id()
    progress = get_progress(uid)
    mastery, seen, counters = progress["mastery"], set(progress["seen"]), progress["counters"]
    plans_cache: dict[str, dict] = {}
    batch = db().batch()

    for attempt_id, attempt in pending:
        plan_id = attempt.get("planId", "")
        if plan_id not in plans_cache:
            snap = _plans(uid).document(plan_id).get() if plan_id else None
            plans_cache[plan_id] = snap.to_dict() if snap and snap.exists else None
        plan = plans_cache[plan_id]
        session = next((s for s in (plan or {}).get("sessions", []) if s["id"] == attempt.get("sessionId")), None)
        if not session or session.get("status") == "hecha":
            batch.update(attempts_ref.document(attempt_id), {"processed": True, "ignored": True})
            continue
        allowed = {it["id"] for it in session["items"]}
        embedded = {it["id"]: it for it in session["items"] if families.is_generated(it["id"])}
        correct = total = hints = 0
        exit_responses: dict[str, list] = {}
        for ans in attempt.get("answers", []):
            # Las variantes generadas no están en el banco: se califican con la copia guardada en el plan,
            # que solo el servidor puede escribir.
            item = items.get(ans.get("itemId")) or embedded.get(ans.get("itemId"))
            if not item or item["id"] not in allowed:
                continue
            ok = ans.get("selected") == item["correct"]
            hinted = int(ans.get("hintsUsed") or 0) > 0
            total += 1
            correct += ok
            hints += hinted
            key = comp_key(item["area"], item["competencia"])
            mastery[key] = round(bkt.update(mastery.get(key, 0.3), ok, hinted), 3)
            seen.add(item["id"])
            generated = families.is_generated(item["id"])
            stats_id = f"G.{families.family_of(item['id'])}" if generated else item["id"]
            batch.set(db().collection("itemStats").document(stats_id), {
                "area": item["area"], "competencia": item["competencia"], **({"example": item["stem"]} if generated else {}),
                "n": firestore.Increment(1), "correct": firestore.Increment(1 if ok else 0),
            }, merge=True)
            if session["type"] == "salida":
                exit_responses.setdefault(item["area"], []).append((item.get("a", 1.0), item.get("b", 0.0), item.get("c", 0.25), ok))
        session.update(status="hecha", correct=correct, total=total, score=round(correct / total, 3) if total else 0.0)
        if session["type"] == "salida":
            plan["exitPassed"] = session["score"] >= settings.exit_pass
            summary["exitPassed"] = plan["exitPassed"]
            for area, responses in exit_responses.items():  # nueva medición del nivel
                prev = progress["thetas"].get(area)
                if prev:
                    theta, se = irt.eap(responses, prior_mean=prev["theta"], prior_sd=0.7)
                    progress["thetas"][area] = _area_result(theta, se, prev.get("n", 0) + len(responses), area)
        counters["attempts"] = counters.get("attempts", 0) + 1
        counters["answers"] = counters.get("answers", 0) + total
        counters["hinted"] = counters.get("hinted", 0) + hints
        batch.update(attempts_ref.document(attempt_id), {"processed": True, "score": session["score"], "processedAt": now()})
        summary["processed"] += 1

    repeat_focus = None
    for plan_id, plan in plans_cache.items():
        if not plan:
            continue
        others = [s for s in plan["sessions"] if s["type"] != "salida"]
        exit_s = next((s for s in plan["sessions"] if s["type"] == "salida"), None)
        if exit_s and exit_s["status"] == "bloqueada" and all(s["status"] == "hecha" for s in others):
            exit_s["status"] = "pendiente"
        if plan["status"] == "activo" and all(s["status"] == "hecha" for s in plan["sessions"]):
            plan["status"] = "completado"
            plan["completedAt"] = now()
            summary["planCompleted"] = True
            if plan.get("exitPassed") is False:
                repeat_focus = plan["focus"]
            history = [k for k in progress["focusHistory"] if k not in plan["focus"]] + plan["focus"]
            progress["focusHistory"] = history[-8:]
        batch.set(_plans(uid).document(plan_id), plan)

    progress.update(mastery=mastery, seen=sorted(seen), counters=counters)
    batch.set(progress_ref(uid), progress, merge=True)
    batch.commit()
    if summary["planCompleted"]:
        summary["newPlan"] = ensure_plan(uid, repeat_focus=repeat_focus, progress=progress) is not None
    return summary


# ---------- simulacro general ----------

def _sim_results(uid: str):
    return db().collection("users").document(uid).collection("simulacroResults")


def list_simulacros(uid: str) -> list[dict]:
    done = {s.id: s.to_dict() for s in _sim_results(uid).stream()}
    out = []
    for snap in db().collection("simulacros").where(filter=FieldFilter("status", "==", "publicado")).stream():
        d = snap.to_dict()
        r = done.get(snap.id, {})
        out.append({"id": snap.id, "title": d["title"], "minutes": d["minutes"], "questions": len(d["itemIds"]), "order": d.get("order", 99),
                    "submitted": bool(r.get("submittedAt")), "startedAt": r.get("startedAt"), "summary": r.get("byArea")})
    return sorted(out, key=lambda s: (s["order"], s["id"]))


def _sim_def(sim_id: str) -> dict:
    snap = db().collection("simulacros").document(sim_id).get()
    if not snap.exists or snap.to_dict().get("status") != "publicado":
        raise HTTPException(404, "Simulacro no disponible.")
    return snap.to_dict()


def get_simulacro(uid: str, sim_id: str) -> dict:
    sim = _sim_def(sim_id)
    items = bank.by_id()
    ordered = [items[i] for i in sim["itemIds"] if i in items]
    ref = _sim_results(uid).document(sim_id)
    snap = ref.get()
    result = snap.to_dict() if snap.exists else None
    if result and result.get("submittedAt"):
        review = [{**bank.public_item(it), "correct": it["correct"], "explanation": it.get("explanation", ""),
                   "selected": result["answers"].get(it["id"])} for it in ordered]
        return {"id": sim_id, "title": sim["title"], "submitted": True, "items": review, "byArea": result["byArea"], "total": result["total"]}
    if not result:
        result = {"startedAt": now()}
        ref.set(result)
    return {"id": sim_id, "title": sim["title"], "minutes": sim["minutes"], "submitted": False,
            "startedAt": result["startedAt"], "items": [bank.public_item(it) for it in ordered]}


def submit_simulacro(uid: str, sim_id: str, answers: dict[str, str]) -> dict:
    sim = _sim_def(sim_id)
    ref = _sim_results(uid).document(sim_id)
    snap = ref.get()
    if snap.exists and snap.to_dict().get("submittedAt"):
        raise HTTPException(409, "Este simulacro ya fue enviado.")
    items = bank.by_id()
    by_area: dict[str, dict] = {}
    responses: dict[str, list] = {}
    clean_answers = {}
    for item_id in sim["itemIds"]:
        item = items.get(item_id)
        if not item:
            continue
        selected = answers.get(item_id)
        clean_answers[item_id] = selected
        ok = selected == item["correct"]
        slot = by_area.setdefault(item["area"], {"correct": 0, "total": 0})
        slot["total"] += 1
        slot["correct"] += ok
        responses.setdefault(item["area"], []).append((item.get("a", 1.0), item.get("b", 0.0), item.get("c", 0.25), ok))
    for area, slot in by_area.items():
        theta, se = irt.eap(responses[area])
        slot.update(score=irt.score_from_theta(theta), se=round(se, 2), pct=round(100 * slot["correct"] / slot["total"]))
    total = {"correct": sum(s["correct"] for s in by_area.values()), "total": sum(s["total"] for s in by_area.values())}
    started = snap.to_dict().get("startedAt") if snap.exists else now()
    ref.set({"startedAt": started, "submittedAt": now(), "answers": clean_answers, "byArea": by_area, "total": total})
    return get_simulacro(uid, sim_id)


def overview(uid: str) -> dict:
    progress = get_progress(uid)
    return {
        "areas": {a: progress["thetas"].get(a) for a in AREA_ORDER},
        "mastery": progress["mastery"],
        "week": progress["week"],
        "diagnosed": [a for a in AREA_ORDER if a in progress["thetas"]],
    }


def new_rng() -> random.Random:
    return random.Random()
