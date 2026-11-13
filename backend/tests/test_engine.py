import random

from app import tutor
from app.catalog import AREAS, level_for
from app.engine import bkt, irt, planner
from app.seed import bank_seed, math_families
from app.seed.loader import seed_items


def simulate_cat(true_theta, pool, rng, min_items=6, max_items=10):
    administered, theta, se = [], 0.0, 1.0
    weights = {c: w for c, (_, w) in AREAS["MAT"]["competencias"].items()}
    while True:
        used = {a["id"] for a in administered}
        cands = [it for it in pool if it["id"] not in used]
        if irt.should_stop(len(administered), se, len(cands), min_items, max_items, 0.45):
            return theta, se, administered
        item = irt.select_next(theta, cands, administered, weights, rng)
        ok = rng.random() < irt.p3pl(true_theta, item["a"], item["b"], item["c"])
        administered.append({**item, "correct": ok})
        theta, se = irt.eap([(a["a"], a["b"], a["c"], a["correct"]) for a in administered])


def synthetic_pool(n=60, seed=1):
    rng = random.Random(seed)
    comps = list(AREAS["MAT"]["competencias"])
    return [{"id": f"i{i}", "competencia": comps[i % 3], "a": rng.uniform(0.8, 1.6), "b": rng.uniform(-2.2, 2.2), "c": 0.25} for i in range(n)]


def test_eap_moves_with_evidence():
    easy_right = [(1.2, -1.0, 0.25, True)] * 4
    hard_right = [(1.2, 1.0, 0.25, True)] * 4
    all_wrong = [(1.2, -1.0, 0.25, False)] * 4
    assert irt.eap(hard_right)[0] > irt.eap(easy_right)[0] > 0 > irt.eap(all_wrong)[0]
    assert irt.eap(easy_right + hard_right)[1] < irt.eap(easy_right)[1]  # más ítems, menos error


def test_cat_recovers_ability_ordering():
    pool = synthetic_pool()
    means = {}
    for true_theta in (-1.5, 0.0, 1.5):
        rng = random.Random(42)
        estimates = [simulate_cat(true_theta, pool, rng)[0] for _ in range(300)]
        means[true_theta] = sum(estimates) / len(estimates)
    assert means[-1.5] < means[0.0] < means[1.5]
    assert abs(means[0.0]) < 0.35
    assert means[1.5] - means[-1.5] > 1.4


def test_cat_is_short_and_balanced():
    pool = synthetic_pool()
    rng = random.Random(7)
    _, _, administered = simulate_cat(0.3, pool, rng)
    assert 6 <= len(administered) <= 10
    assert len({a["competencia"] for a in administered}) == 3  # cubre las tres competencias


def test_levels_follow_cuts():
    assert level_for("MAT", 30) == "1" and level_for("MAT", 36) == "2" and level_for("MAT", 71) == "4"
    assert level_for("ING", 47) == "Pre A1" and level_for("ING", 80) == "B+"


def test_bkt_direction_and_hint_discount():
    p = 0.4
    assert bkt.update(p, True) > p > bkt.update(p, False) - 0.12
    assert bkt.update(p, True, hinted=True) < bkt.update(p, True)
    for _ in range(12):
        p = bkt.update(p, True)
    assert p > 0.9


def test_seed_bank_is_well_formed():
    items = seed_items()
    ids = [it["id"] for it in items]
    assert len(ids) == len(set(ids))
    for it in items:
        assert it["area"] in AREAS and it["competencia"] in AREAS[it["area"]]["competencias"], it["id"]
        assert set(it["options"]) == set("ABCD") and it["correct"] in it["options"], it["id"]
        assert len(set(it["options"].values())) == 4, it["id"]
        assert it["explanation"] and it["hints"], it["id"]
        assert it["pool"] in ("diagnostico", "practica", "simulacro")
    for area, spec in AREAS.items():
        diag = [it for it in items if it["area"] == area and it["pool"] == "diagnostico"]
        assert len(diag) >= 8 and {it["competencia"] for it in diag} == set(spec["competencias"]), area
        assert any(it["pool"] == "simulacro" and it["area"] == area for it in items)


def test_math_families_are_correct_and_reproducible():
    a, b = math_families.generate(), math_families.generate()
    assert a == b and len(a) >= 20
    d = next(it for it in a if it["origin"] == "familia:descuento")
    assert d["options"][d["correct"]].startswith("$")


def test_practice_and_simulacro_pools_do_not_overlap():
    items = seed_items()
    sim = {it["id"] for it in items if it["pool"] == "simulacro"}
    mastery = {f"{a}.{c}": 0.3 for a, s in AREAS.items() for c in s["competencias"]}
    plan = planner.build_plan(1, mastery, {a: 0.0 for a in AREAS}, items, set(), [], 4, 2, rng=random.Random(1))
    used = {it["id"] for s in plan["sessions"] for it in s["items"]}
    assert used and not used & sim


def test_plan_targets_weakest_and_has_exit_quiz():
    items = seed_items()
    mastery = {f"{a}.{c}": 0.7 for a, s in AREAS.items() for c in s["competencias"]}
    mastery["MAT.argumentacion"] = 0.1
    mastery["LEC.critica"] = 0.15
    plan = planner.build_plan(1, mastery, {a: 0.0 for a in AREAS}, items, set(), [], 4, 2, rng=random.Random(3))
    assert plan["focus"][:2] == ["MAT.argumentacion", "LEC.critica"]
    types = [s["type"] for s in plan["sessions"]]
    assert types.count("practica") == 3 and types[-1] == "salida"
    exit_s = plan["sessions"][-1]
    assert exit_s["tutor"] is False and exit_s["status"] == "bloqueada"
    ids = [it["id"] for s in plan["sessions"] for it in s["items"]]
    assert len(ids) == len(set(ids))  # el cuestionario de salida no repite preguntas de la práctica


def test_plan_week2_adds_spaced_review():
    items = seed_items()
    mastery = {f"{a}.{c}": 0.5 for a, s in AREAS.items() for c in s["competencias"]}
    mastery.update({"NAT.indagacion": 0.1, "SOC.perspectivas": 0.2, "ING.gramatica": 0.2})
    plan = planner.build_plan(2, mastery, {a: 0.0 for a in AREAS}, items, set(), ["MAT.formulacion", "LEC.global"], 4, 2, rng=random.Random(5))
    assert any(s["type"] == "repaso" for s in plan["sessions"])


ITEM = next(it for it in bank_seed.ITEMS if it["id"] == "MAT-005")  # clave B: $68.000


def test_tutor_blocks_answer_before_attempt():
    for leak in ("La respuesta correcta es la B.", "Es la B, porque 80.000 menos 12.000...", "Debes marcar $68.000", "la opción (b) es la indicada: la respuesta es esa"):
        out = tutor.ask(ITEM, answered=False, selected=None, question="dime la respuesta", call=lambda s, u, r=leak: r)
        assert out["source"] == "validado" and "68.000" not in out["reply"], leak


def test_tutor_allows_socratic_hint_and_full_explanation_after():
    hint = "¿Cuánto es el 15 % de 80.000? Empieza por ahí y luego piensa qué haces con ese valor."
    out = tutor.ask(ITEM, False, None, "no entiendo", call=lambda s, u: hint)
    assert out == {"reply": hint, "source": "modelo"}
    seen = {}
    after = tutor.ask(ITEM, True, "A", "por qué fallé", call=lambda s, u: seen.update(system=s, user=u) or "La correcta es la B: el descuento es 12.000.")
    assert after["source"] == "modelo" and "YA respondió" in seen["system"] and "Explicación validada" in seen["user"]


def test_tutor_sends_no_personal_data_and_survives_failures():
    captured = {}
    tutor.ask(ITEM, False, None, "soy juan@correo.com, cel 3001234567, ayuda", call=lambda s, u: captured.update(u=u) or "Piensa en el porcentaje.")
    assert "juan@correo.com" not in captured["u"] and "3001234567" not in captured["u"]

    def boom(s, u):
        raise RuntimeError("sin red")

    assert tutor.ask(ITEM, False, None, "ayuda", call=boom)["source"] == "validado"
    assert tutor.stored_reply(ITEM, True, "B").startswith("¡Bien!")


def test_plan_always_has_exit_quiz_even_with_a_small_bank():
    """Con pocas preguntas por competencia, el plan aparta primero las del cuestionario de salida."""
    import random

    from app.engine.planner import build_plan
    for n in (2, 3, 4, 5, 8):
        items = [{"id": f"X{i}", "area": "LEC", "competencia": "global", "pool": "practica" if i % 2 else "diagnostico", "b": 0.0,
                  "stem": "s", "options": {}, "correct": "A"} for i in range(n)]
        for seed in range(20):
            plan = build_plan(1, {"LEC.global": 0.2}, {"LEC": 0.0}, items, {"X0", "X1"}, [], 4, 2, rng=random.Random(seed))
            types = [s["type"] for s in plan["sessions"]]
            assert types[-1] == "salida" and "practica" in types, (n, seed, types)
            ids = [it["id"] for s in plan["sessions"] for it in s["items"]]
            assert len(ids) == len(set(ids))  # la salida no repite preguntas de la práctica


def test_admin_requires_verified_email_and_is_promoted_later(monkeypatch):
    """Sin correo verificado nadie entra como administrador aunque su correo esté en la lista."""
    from app import security

    class Ref:
        def __init__(self): self.data = None
        def get(self): return type("Snap", (), {"exists": self.data is not None, "to_dict": lambda s: dict(self.data), "reference": self})()
        def set(self, d): self.data = dict(d)
        def update(self, d): self.data.update(d)

    ref = Ref()
    fake_db = type("DB", (), {"collection": lambda s, n: type("C", (), {"document": lambda s2, uid: ref})()})()
    monkeypatch.setattr(security, "db", lambda: fake_db)
    monkeypatch.setattr(security.settings, "admin_emails", ["jefe@ejemplo.test"])
    monkeypatch.setattr(security.settings, "emulators", False)
    token = {"uid": "u1", "email": "jefe@ejemplo.test", "email_verified": False}
    monkeypatch.setattr(security, "auth", lambda: type("A", (), {"verify_id_token": lambda s, t: token})())

    assert security.current_user("Bearer x")["role"] == "particular"
    token["email_verified"] = True
    assert security.current_user("Bearer x")["role"] == "admin" and ref.data["role"] == "admin"
    monkeypatch.setattr(security.settings, "admin_emails", [])
    ref.data = None
    assert security.current_user("Bearer x")["role"] == "particular"  # sin lista, nadie es administrador
