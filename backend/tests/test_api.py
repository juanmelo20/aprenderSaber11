"""Prueba de integración de extremo a extremo contra los emuladores de Firebase.

Requiere:  FIRESTORE_EMULATOR_HOST=127.0.0.1:8080  FIREBASE_AUTH_EMULATOR_HOST=127.0.0.1:9099
Recorre el flujo completo: administrador -> institución -> docente -> estudiante -> acudiente.
"""
import datetime as dt
import os
import random
import zlib

import httpx
import pytest

pytestmark = pytest.mark.skipif(not os.getenv("FIRESTORE_EMULATOR_HOST"), reason="requiere emuladores de Firebase")

PROJECT = "demo-rumbo11"
AUTH = f"http://{os.getenv('FIREBASE_AUTH_EMULATOR_HOST', '127.0.0.1:9099')}"
FS = f"http://{os.getenv('FIRESTORE_EMULATOR_HOST', '127.0.0.1:8080')}"
DOCS = f"{FS}/v1/projects/{PROJECT}/databases/(default)/documents"
S: dict = {}


def token(email, password="clave-segura-1", signup=False):
    kind = "signUp" if signup else "signInWithPassword"
    r = httpx.post(f"{AUTH}/identitytoolkit.googleapis.com/v1/accounts:{kind}?key=demo",
                   json={"email": email, "password": password, "returnSecureToken": True})
    r.raise_for_status()
    return r.json()["idToken"]


def H(tok):
    return {"Authorization": f"Bearer {tok}"}


@pytest.fixture(scope="module")
def api():
    httpx.delete(f"{FS}/emulator/v1/projects/{PROJECT}/databases/(default)/documents")
    httpx.delete(f"{AUTH}/emulator/v1/projects/{PROJECT}/accounts")
    from fastapi.testclient import TestClient

    from app import bank
    from app.main import app
    bank.invalidate()
    return TestClient(app)


def set_password(email, password="clave-segura-1"):
    from app.db import auth
    auth().update_user(auth().get_user_by_email(email).uid, password=password)
    return token(email, password)


def future(days=200):
    return (dt.date.today() + dt.timedelta(days=days)).isoformat()


def test_01_admin_bootstrap_and_seed(api):
    assert api.get("/api/me").status_code == 401
    S["admin"] = token("admin@rumbo11.test", signup=True)
    me = api.get("/api/me", headers=H(S["admin"])).json()
    assert me["role"] == "admin" and me["access"]["ok"]
    seed = api.post("/api/admin/items/seed", headers=H(S["admin"])).json()
    assert seed["written"] >= 100 and seed["simulacroItems"] == 15
    stats = api.get("/api/admin/items/stats", headers=H(S["admin"])).json()
    assert set(stats["byArea"]) == {"LEC", "MAT", "SOC", "NAT", "ING"}


def test_02_institution_license_and_members(api):
    r = api.post("/api/admin/institutions", headers=H(S["admin"]), json={
        "name": "IER El Tarra", "municipality": "Hacarí", "seats": 3, "expires": future(),
        "adminEmail": "rectoria@eltarra.test", "adminName": "Rectoría El Tarra"})
    assert r.status_code == 200, r.text
    S["inst_id"] = r.json()["id"]
    S["inst"] = set_password("rectoria@eltarra.test")
    assert api.get("/api/me", headers=H(S["inst"])).json()["role"] == "institucion"

    t = api.post("/api/institution/teachers", headers=H(S["inst"]), json={"name": "Profe Mate", "email": "mate@eltarra.test", "areas": ["MAT", "NAT"]})
    assert t.status_code == 200, t.text
    S["teacher"] = set_password("mate@eltarra.test")

    rows = [
        {"name": "Ana Pérez", "email": "ana@eltarra.test", "grade": "11", "group": "A", "guardianEmail": "mama.ana@correo.test"},
        {"name": "Luis Rojas", "email": "luis@eltarra.test", "grade": "11", "group": "A", "adult": True},
        {"name": "Sara Díaz", "email": "sara@eltarra.test", "grade": "10", "group": "A"},
        {"name": "Sin Cupo", "email": "sincupo@eltarra.test"},
        {"name": "", "email": "malo"},
    ]
    res = api.post("/api/institution/students", headers=H(S["inst"]), json={"students": rows}).json()["results"]
    assert [r["ok"] for r in res] == [True, True, True, False, False]
    assert "cupos" in res[3]["error"]
    assert "/autorizacion/" in res[0]["consentLink"] and "consentLink" not in res[1]  # el mayor de edad autoriza él mismo
    S["consent_token"] = res[0]["consentLink"].rsplit("/", 1)[1]
    S["sara_token"] = res[2]["consentLink"].rsplit("/", 1)[1]
    inst = api.get("/api/institution", headers=H(S["inst"])).json()
    assert inst["seatsUsed"] == 3 and len(inst["students"]) == 3 and inst["teacherByArea"]["MAT"]


def test_03_consent_gate(api):
    S["ana"] = set_password("ana@eltarra.test")
    me = api.get("/api/me", headers=H(S["ana"])).json()
    assert me["role"] == "estudiante" and me["access"] == {"ok": False, "reason": "consentimiento"}
    assert api.get("/api/overview", headers=H(S["ana"])).status_code == 403
    assert api.post("/api/me/consent", headers=H(S["ana"]), json={"declaresAdult": True, "accept": True}).status_code == 403  # menor: no puede autorizarse sola

    info = api.get(f"/api/public/consent/{S['consent_token']}").json()
    assert info["studentFirstName"] == "Ana" and info["status"] == "pendiente" and "email" not in info
    assert api.post(f"/api/public/consent/{S['consent_token']}", json={"guardianName": "x", "relationship": "", "accept": True}).status_code == 422
    ok = api.post(f"/api/public/consent/{S['consent_token']}", json={"guardianName": "María Pérez Gómez", "relationship": "Madre", "accept": True})
    assert ok.json()["status"] == "aceptado"
    assert api.get("/api/me", headers=H(S["ana"])).json()["access"]["ok"]

    S["luis"] = set_password("luis@eltarra.test")
    assert api.post("/api/me/consent", headers=H(S["luis"]), json={"declaresAdult": True, "accept": True}).json()["status"] == "aceptado"


def run_diagnostic(api, tok, area, ability):
    from app.seed.loader import seed_items
    keys = {it["id"]: it for it in seed_items()}
    rng = random.Random(zlib.crc32(f"{area}-{ability}".encode()))  # semilla estable entre ejecuciones
    state = api.post(f"/api/diagnostic/{area}/start", headers=H(tok)).json()
    seen, n = [], 0
    while not state["done"]:
        item = state["item"]
        assert "correct" not in item and "explanation" not in item  # el diagnóstico no envía la clave
        assert item["id"] not in seen
        seen.append(item["id"])
        real = keys[item["id"]]
        selected = real["correct"] if rng.random() < ability else next(k for k in "ABCD" if k != real["correct"])
        state = api.post(f"/api/diagnostic/{area}/answer", headers=H(tok), json={"itemId": item["id"], "selected": selected}).json()
        n += 1
    assert 6 <= n <= 8  # el banco semilla tiene 8 por área; el tope general es 10
    return state["result"]


def test_04_adaptive_diagnostic(api):
    strong = {a: run_diagnostic(api, S["ana"], a, 0.95) for a in ("MAT", "LEC", "SOC", "NAT", "ING")}
    weak = run_diagnostic(api, S["luis"], "MAT", 0.1)
    assert strong["MAT"]["score"] > weak["score"] + 10 and weak["level"] in ("1", "2")
    # Con 8 preguntas el diagnóstico es prudente: informa un rango y no puede ubicar a nadie en el nivel más alto.
    for r in list(strong.values()) + [weak]:
        assert r["low"] < r["score"] < r["high"] and r["high"] - r["low"] >= 10
    assert all(r["score"] >= 50 for r in strong.values())
    again = api.post("/api/diagnostic/MAT/start", headers=H(S["ana"])).json()
    assert again["done"] and again["result"]["score"] == strong["MAT"]["score"]  # no se puede repetir para inflar el resultado
    ov = api.get("/api/overview", headers=H(S["ana"])).json()
    assert len(ov["diagnosed"]) == 5 and len(ov["mastery"]) == 15


def fs_get(path, tok):
    return httpx.get(f"{DOCS}/{path}", headers=H(tok))


def test_05_plan_offline_attempts_and_sync(api):
    from app.db import db
    from app.security import current_user  # noqa: F401
    plan_info = api.post("/api/plan/ensure", headers=H(S["ana"])).json()
    uid = api.get("/api/me", headers=H(S["ana"])).json()["uid"]
    S["ana_uid"] = uid
    plan = db().collection("users").document(uid).collection("plans").document(plan_info["id"]).get().to_dict()
    assert plan["week"] == 1 and [s["type"] for s in plan["sessions"]].count("practica") == 3
    assert plan["sessions"][-1]["type"] == "salida" and plan["sessions"][-1]["status"] == "bloqueada"
    before = api.get("/api/overview", headers=H(S["ana"])).json()["mastery"]

    # El cliente lee su plan directamente de Firestore (así funciona sin conexión) ...
    assert fs_get(f"users/{uid}/plans/{plan_info['id']}", S["ana"]).status_code == 200
    # ... pero no puede leer el plan de otra persona, ni el banco de ítems, ni modificar su progreso.
    assert fs_get(f"users/{uid}/plans/{plan_info['id']}", S["luis"]).status_code == 403
    assert fs_get("items/MAT-001", S["ana"]).status_code == 403
    assert httpx.patch(f"{DOCS}/progress/{uid}", headers=H(S["ana"]), json={"fields": {"week": {"integerValue": "9"}}}).status_code == 403

    # Tutor: disponible en práctica, prohibido en el cuestionario de salida.
    p1 = plan["sessions"][0]
    ask = api.post("/api/tutor/ask", headers=H(S["ana"]), json={"planId": plan_info["id"], "sessionId": p1["id"], "itemId": p1["items"][0]["id"], "answered": False, "question": "dame la respuesta"}).json()
    assert ask["source"] == "validado" and ask["reply"] in p1["items"][0]["hints"]
    exit_s = plan["sessions"][-1]
    blocked = api.post("/api/tutor/ask", headers=H(S["ana"]), json={"planId": plan_info["id"], "sessionId": exit_s["id"], "itemId": exit_s["items"][0]["id"], "question": "ayuda"})
    assert blocked.status_code == 403

    # El cliente guarda los intentos en Firestore (reglas: solo crear, con id fijo por sesión).
    def attempt(session, all_correct=True, hints=0):
        answers = [{"mapValue": {"fields": {
            "itemId": {"stringValue": it["id"]},
            "selected": {"stringValue": it["correct"] if all_correct else "A" if it["correct"] != "A" else "B"},
            "hintsUsed": {"integerValue": str(hints)}}}} for it in session["items"]]
        doc_id = f"{plan_info['id']}_{session['id']}"
        body = {"fields": {"planId": {"stringValue": plan_info["id"]}, "sessionId": {"stringValue": session["id"]},
                           "type": {"stringValue": session["type"]}, "processed": {"booleanValue": False},
                           "startedAt": {"stringValue": "2027-02-01T08:00:00Z"}, "finishedAt": {"stringValue": f"2027-02-01T08:1{len(doc_id) % 9}:00Z"},
                           "answers": {"arrayValue": {"values": answers}}}}
        return httpx.post(f"{DOCS}/users/{uid}/attempts?documentId={doc_id}", headers=H(S["ana"]), json=body)

    assert attempt(plan["sessions"][0]).status_code == 200
    assert attempt(plan["sessions"][0]).status_code in (400, 403, 409)  # no se puede reenviar la misma sesión
    cheat = {"fields": {"planId": {"stringValue": plan_info["id"]}, "sessionId": {"stringValue": "p2"}, "type": {"stringValue": "practica"},
                        "processed": {"booleanValue": True}, "answers": {"arrayValue": {}}}}
    assert httpx.post(f"{DOCS}/users/{uid}/attempts?documentId={plan_info['id']}_p2", headers=H(S["ana"]), json=cheat).status_code == 403

    first = api.post("/api/sync", headers=H(S["ana"])).json()
    assert first["processed"] == 1 and not first["planCompleted"]
    after = api.get("/api/overview", headers=H(S["ana"])).json()["mastery"]
    key = plan["sessions"][0]["competencia"]
    assert after[key] > before[key]

    for s in plan["sessions"][1:]:  # termina el resto estando "sin conexión" y sincroniza una sola vez
        assert attempt(s, all_correct=True).status_code == 200
    done = api.post("/api/sync", headers=H(S["ana"])).json()
    assert done["planCompleted"] and done["exitPassed"] is True and done["newPlan"]
    assert api.post("/api/sync", headers=H(S["ana"])).json()["processed"] == 0  # idempotente
    plans = {p.id: p.to_dict() for p in db().collection("users").document(uid).collection("plans").stream()}
    assert plans["semana-001"]["status"] == "completado" and plans["semana-002"]["status"] == "activo"
    week1_ids = {it["id"] for s in plan["sessions"] for it in s["items"]}
    week2_ids = {it["id"] for s in plans["semana-002"]["sessions"] for it in s["items"]}
    assert len(week2_ids - week1_ids) >= len(week2_ids) // 2  # la semana 2 prioriza preguntas nuevas


def test_06_failed_exit_quiz_repeats_focus(api):
    from app.db import db
    for a in ("LEC", "SOC"):
        run_diagnostic(api, S["luis"], a, 0.2)
    info = api.post("/api/plan/ensure", headers=H(S["luis"])).json()
    uid = api.get("/api/me", headers=H(S["luis"])).json()["uid"]
    ref = db().collection("users").document(uid)
    plan = ref.collection("plans").document(info["id"]).get().to_dict()
    for s in plan["sessions"]:
        ref.collection("attempts").document(f"{info['id']}_{s['id']}").set({
            "planId": info["id"], "sessionId": s["id"], "type": s["type"], "processed": False, "finishedAt": "2027-02-02T10:00:00Z",
            "answers": [{"itemId": it["id"], "selected": "A" if it["correct"] != "A" else "B", "hintsUsed": 1} for it in s["items"]]})
    out = api.post("/api/sync", headers=H(S["luis"])).json()
    assert out["planCompleted"] and out["exitPassed"] is False and out["newPlan"]
    nxt = ref.collection("plans").document("semana-002").get().to_dict()
    assert nxt["refuerzo"] is True and nxt["focus"] == plan["focus"]


def test_07_simulacro(api):
    sims = api.get("/api/simulacros", headers=H(S["ana"])).json()
    assert len(sims) == 1 and sims[0]["questions"] == 15 and not sims[0]["submitted"]
    sim = api.get("/api/simulacros/general-1", headers=H(S["ana"])).json()
    assert all("correct" not in it for it in sim["items"])
    from app.seed.loader import seed_items
    keys = {it["id"]: it["correct"] for it in seed_items()}
    plan_ids = set()  # el simulacro no comparte preguntas con la práctica
    from app.db import db
    for p in db().collection("users").document(S["ana_uid"]).collection("plans").stream():
        plan_ids |= {it["id"] for s in p.to_dict()["sessions"] for it in s["items"]}
    assert not plan_ids & {it["id"] for it in sim["items"]}
    answers = {it["id"]: keys[it["id"]] for it in sim["items"][:10]}
    res = api.post("/api/simulacros/general-1/submit", headers=H(S["ana"]), json={"answers": answers}).json()
    assert res["submitted"] and res["total"] == {"correct": 10, "total": 15} and res["byArea"]["LEC"]["pct"] == 100
    assert res["items"][0]["correct"] and res["items"][0]["explanation"]
    assert api.post("/api/simulacros/general-1/submit", headers=H(S["ana"]), json={"answers": answers}).status_code == 409


def test_08_teacher_dashboard_and_item_review(api):
    ov = api.get("/api/teacher/overview?area=MAT", headers=H(S["teacher"])).json()
    names = [s["name"] for s in ov["students"]]
    assert set(names) == {"Ana Pérez", "Luis Rojas", "Sara Díaz"} and names[0] == "Luis Rojas"  # primero quien va más flojo
    assert ov["diagnosed"] == 2 and len(ov["competencias"]) == 3 and ov["classPlan"][0]["tips"]
    assert ov["groups"] == ["10A", "11A"]
    only10 = api.get("/api/teacher/overview?area=MAT&group=10A", headers=H(S["teacher"])).json()
    assert [s["name"] for s in only10["students"]] == ["Sara Díaz"]
    assert api.get("/api/teacher/overview?area=SOC", headers=H(S["teacher"])).status_code == 403  # no es su área
    assert api.get("/api/teacher/overview?area=MAT", headers=H(S["ana"])).status_code == 403

    items = api.get("/api/items?area=MAT&status=borrador", headers=H(S["teacher"])).json()
    target = items[0]["id"]
    assert api.patch(f"/api/items/{target}", headers=H(S["teacher"]), json={"correct": "Z"}).status_code == 422
    assert api.patch(f"/api/items/{target}", headers=H(S["teacher"]), json={"status": "publicado", "explanation": "Explicación revisada por el docente."}).status_code == 200
    assert api.patch("/api/items/SOC-001", headers=H(S["teacher"]), json={"status": "publicado"}).status_code == 403
    reseed = api.post("/api/admin/items/seed", headers=H(S["admin"])).json()
    assert reseed["skipped"] == 1  # volver a cargar la semilla no pisa lo revisado
    again = [i for i in api.get("/api/items?area=MAT", headers=H(S["teacher"])).json() if i["id"] == target][0]
    assert again["status"] == "publicado" and again["explanation"].startswith("Explicación revisada")


def test_09_individual_user_and_license(api):
    S["indep"] = token("particular@correo.test", signup=True)
    me = api.get("/api/me", headers=H(S["indep"])).json()
    assert me["role"] == "particular" and me["access"]["reason"] == "consentimiento"
    link = api.post("/api/me/consent-link", headers=H(S["indep"])).json()["link"]
    assert "/autorizacion/" in link
    api.post("/api/me/consent", headers=H(S["indep"]), json={"declaresAdult": True, "accept": True})
    assert api.get("/api/me", headers=H(S["indep"])).json()["access"]["reason"] == "licencia"
    assert api.post("/api/diagnostic/MAT/start", headers=H(S["indep"])).status_code == 403
    assert api.post("/api/admin/licenses", headers=H(S["indep"]), json={"email": "particular@correo.test", "expires": future()}).status_code == 403
    assert api.post("/api/admin/licenses", headers=H(S["admin"]), json={"email": "particular@correo.test", "plan": "pase", "expires": future()}).status_code == 200
    assert api.get("/api/me", headers=H(S["indep"])).json()["access"]["ok"]
    assert api.post("/api/diagnostic/MAT/start", headers=H(S["indep"])).status_code == 200


def test_10_research_export_is_anonymous(api):
    data = api.get("/api/admin/research/export", headers=H(S["admin"]))
    text = data.text.lower()
    for private in ("ana p", "pérez", "@", "luis", "rojas", "eltarra.test", S["ana_uid"].lower()):
        assert private not in text, private
    rows = data.json()["rows"]
    row = next(r for r in rows if r.get("MAT_puntaje") and r.get("conteo_attempts", 0) >= 4)
    assert row["institucion"] == "IER El Tarra" and row["grado"] == "11" and len(row["id"]) == 16
    assert api.get("/api/admin/research/export", headers=H(S["inst"])).status_code == 403


def test_11_expired_institution_license_blocks_students(api):
    from app.db import db
    db().collection("institutions").document(S["inst_id"]).update({"licenseExpires": dt.datetime(2020, 1, 1, tzinfo=dt.timezone.utc)})
    assert api.get("/api/me", headers=H(S["ana"])).json()["access"] == {"ok": False, "reason": "licencia_institucion"}
    assert api.post("/api/sync", headers=H(S["ana"])).status_code == 403
