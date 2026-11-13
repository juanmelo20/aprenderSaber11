"""Datos de demostración para probar la app en el computador (solo contra los emuladores).

Uso, con los emuladores encendidos:
    FIRESTORE_EMULATOR_HOST=127.0.0.1:8080 FIREBASE_AUTH_EMULATOR_HOST=127.0.0.1:9099 python -m scripts.dev_seed

Crea un administrador, un colegio con docentes y estudiantes, y un particular.
Todas las personas son ficticias. La contraseña de todas las cuentas es la de PASSWORD.
"""
import datetime as dt
import os
import random
import sys

import httpx

if not os.getenv("FIRESTORE_EMULATOR_HOST") or not os.getenv("FIREBASE_AUTH_EMULATOR_HOST"):
    sys.exit("Este script solo corre contra los emuladores. Define FIRESTORE_EMULATOR_HOST y FIREBASE_AUTH_EMULATOR_HOST.")

from fastapi.testclient import TestClient  # noqa: E402

from app import bank  # noqa: E402
from app.config import settings  # noqa: E402
from app.db import auth  # noqa: E402
from app.main import app  # noqa: E402
from app.seed.loader import seed_items  # noqa: E402

PASSWORD = "rumbo11-demo"
AUTH = f"http://{os.environ['FIREBASE_AUTH_EMULATOR_HOST']}"
FS = f"http://{os.environ['FIRESTORE_EMULATOR_HOST']}"
api = TestClient(app)
KEYS = {it["id"]: it for it in seed_items()}


def token(email: str, signup: bool = False) -> str:
    kind = "signUp" if signup else "signInWithPassword"
    r = httpx.post(f"{AUTH}/identitytoolkit.googleapis.com/v1/accounts:{kind}?key=demo",
                   json={"email": email, "password": PASSWORD, "returnSecureToken": True})
    r.raise_for_status()
    return r.json()["idToken"]


def login(email: str) -> dict:
    auth().update_user(auth().get_user_by_email(email).uid, password=PASSWORD)
    return {"Authorization": f"Bearer {token(email)}"}


def ok(r):
    assert r.status_code == 200, f"{r.request.method} {r.request.url}: {r.status_code} {r.text}"
    return r.json()


def diagnose(headers: dict, area: str, ability: float, rng: random.Random) -> None:
    state = ok(api.post(f"/api/diagnostic/{area}/start", headers=headers))
    while not state["done"]:
        real = KEYS[state["item"]["id"]]
        selected = real["correct"] if rng.random() < ability else next(k for k in "ABCD" if k != real["correct"])
        state = ok(api.post(f"/api/diagnostic/{area}/answer", headers=headers, json={"itemId": real["id"], "selected": selected}))


def main() -> None:
    httpx.delete(f"{FS}/emulator/v1/projects/{settings.project_id}/databases/(default)/documents")
    httpx.delete(f"{AUTH}/emulator/v1/projects/{settings.project_id}/accounts")
    bank.invalidate()
    rng = random.Random(11)
    expires = (dt.date.today() + dt.timedelta(days=300)).isoformat()

    admin_email = settings.admin_emails[0]
    admin = {"Authorization": f"Bearer {token(admin_email, signup=True)}"}
    ok(api.get("/api/me", headers=admin))
    seed = ok(api.post("/api/admin/items/seed", headers=admin))

    ok(api.post("/api/admin/institutions", headers=admin, json={
        "name": "Colegio de demostración", "municipality": "Hacarí", "seats": 10, "expires": expires,
        "adminEmail": "rectoria@colegio.test", "adminName": "Rectoría (demo)"}))
    inst = login("rectoria@colegio.test")
    ok(api.post("/api/institution/teachers", headers=inst, json={"name": "Docente de Matemáticas (demo)", "email": "mate@colegio.test", "areas": ["MAT", "NAT"]}))
    ok(api.post("/api/institution/teachers", headers=inst, json={"name": "Docente de Lenguaje (demo)", "email": "lenguaje@colegio.test", "areas": ["LEC", "SOC", "ING"]}))
    login("mate@colegio.test"), login("lenguaje@colegio.test")

    # (nombre, correo, grupo, mayor de edad, habilidad simulada o None si no ha empezado)
    students = [
        ("Estudiante Uno", "uno@colegio.test", "A", False, 0.80),
        ("Estudiante Dos", "dos@colegio.test", "A", False, 0.55),
        ("Estudiante Tres", "tres@colegio.test", "A", False, 0.35),
        ("Estudiante Cuatro", "cuatro@colegio.test", "B", False, 0.65),
        ("Estudiante Cinco", "cinco@colegio.test", "B", False, 0.25),
        ("Estudiante Nuevo", "nuevo@colegio.test", "B", False, None),      # autorizado, sin diagnóstico
        ("Estudiante Mayor", "mayor@colegio.test", "B", True, None),        # mayor de edad: autoriza al entrar
        ("Estudiante Pendiente", "pendiente@colegio.test", "A", False, None),  # falta la autorización del acudiente
    ]
    rows = [{"name": n, "email": e, "grade": "11", "group": g, "adult": adult} for n, e, g, adult, _ in students]
    results = ok(api.post("/api/institution/students", headers=inst, json={"students": rows}))["results"]
    pending_link = ""
    for (name, email, _, adult, ability), res in zip(students, results):
        assert res["ok"], res
        if email == "pendiente@colegio.test":
            pending_link = res["consentLink"]
            login(email)
            continue
        if not adult:
            ok(api.post(f"/api/public/consent/{res['consentLink'].rsplit('/', 1)[1]}",
                        json={"guardianName": "Acudiente de demostración", "relationship": "Madre", "accept": True}))
        headers = login(email)
        if ability is None:
            continue
        for area in ("LEC", "MAT", "SOC", "NAT", "ING"):
            diagnose(headers, area, ability, rng)
        ok(api.post("/api/plan/ensure", headers=headers))

    part = "particular@correo.test"
    ok(api.get("/api/me", headers={"Authorization": f"Bearer {token(part, signup=True)}"}))  # el perfil se crea al entrar por primera vez
    ok(api.post("/api/admin/licenses", headers=admin, json={"email": part, "plan": "individual", "expires": expires}))

    print(f"Banco: {seed['written']} ítems, simulacro con {seed['simulacroItems']}.")
    print(f"Contraseña de todas las cuentas: {PASSWORD}\n")
    for label, email in [("Administrador", admin_email), ("Colegio", "rectoria@colegio.test"), ("Docente MAT/NAT", "mate@colegio.test"),
                         ("Docente LEC/SOC/ING", "lenguaje@colegio.test"), ("Estudiante con ruta", "uno@colegio.test"),
                         ("Estudiante sin diagnóstico", "nuevo@colegio.test"), ("Estudiante mayor de edad", "mayor@colegio.test"),
                         ("Estudiante sin autorización", "pendiente@colegio.test"), ("Particular", part)]:
        print(f"  {label:30} {email}")
    print(f"\nEnlace de autorización pendiente:\n  {pending_link}")


if __name__ == "__main__":
    main()
