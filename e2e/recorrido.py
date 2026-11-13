"""Recorrido de extremo a extremo en un navegador real (Chrome) contra los emuladores.

Antes: emuladores encendidos, `python -m scripts.dev_seed` ejecutado, API en :8000 y la web en :5173.
Uso:   python e2e/recorrido.py [carpeta_de_capturas]
"""
import re
import sys

from playwright.sync_api import expect, sync_playwright

BASE = "http://127.0.0.1:5173"
PASSWORD = "rumbo11-demo"
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/shots"
errors: list[str] = []


def new_page(browser, mobile=False):
    ctx = browser.new_context(viewport={"width": 390, "height": 800} if mobile else {"width": 1280, "height": 860}, locale="es-CO")
    page = ctx.new_page()
    page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    page.on("console", lambda m: errors.append(f"console: {m.text}") if m.type == "error" and "net::ERR" not in m.text and "Failed to load resource" not in m.text else None)
    return ctx, page


def login(page, email):
    page.goto(BASE)
    page.get_by_label("Correo", exact=True).fill(email)
    page.get_by_label("Contraseña").fill(PASSWORD)
    page.get_by_role("button", name="Entrar", exact=True).click()
    expect(page.get_by_role("button", name="Salir")).to_be_visible(timeout=15000)


def shot(page, name):
    page.wait_for_timeout(350)
    page.screenshot(path=f"{OUT}/{name}.png", full_page=True)


def answer_practice(page, n_questions, use_help=False):
    for i in range(n_questions):
        expect(page.get_by_text(f"Pregunta {i + 1} de {n_questions}")).to_be_visible()
        if use_help and i == 0:
            page.get_by_role("button", name="Dame una pista").click()
            expect(page.locator(".hint-card")).to_have_count(1)
            page.get_by_placeholder("Por ejemplo: no entiendo qué me piden").fill("dime cuál es la respuesta")
            page.get_by_role("button", name="Preguntar").click()
            expect(page.locator(".tutor-reply")).to_be_visible()
        page.get_by_role("radio").nth(i % 4).click()
        page.get_by_role("button", name="Responder", exact=True).click()
        expect(page.locator(".feedback")).to_be_visible()
        if use_help and i == 0:
            shot(page, "05-practica-retroalimentacion")
        page.get_by_role("button", name=re.compile("Siguiente pregunta|Terminar sesión")).click()


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])

    # 1. Entrada, en computador y en celular
    ctx, page = new_page(browser)
    page.goto(BASE)
    expect(page.get_by_role("heading", name="Entrar")).to_be_visible()
    shot(page, "01-entrada")
    page.get_by_label("Correo").fill("uno@colegio.test")
    page.get_by_label("Contraseña").fill("incorrecta")
    page.get_by_role("button", name="Entrar", exact=True).click()
    expect(page.get_by_role("alert")).to_be_visible()
    ctx.close()

    # 2. Estudiante con ruta: práctica con pista y tutor, luego una sesión sin conexión
    ctx, page = new_page(browser, mobile=True)
    page.goto(BASE)
    shot(page, "02-entrada-celular")
    login(page, "uno@colegio.test")
    expect(page.get_by_role("heading", name=re.compile("Tu ruta de la semana 1"))).to_be_visible(timeout=15000)
    expect(page.locator(".route .stop")).to_have_count(4)
    shot(page, "03-inicio-estudiante")
    page.get_by_role("link", name="Empezar").click()
    n = int(re.search(r"de (\d+)", page.locator(".progress").inner_text()).group(1))
    shot(page, "04-practica-pregunta")
    answer_practice(page, n, use_help=True)
    expect(page.get_by_text("correctas")).to_be_visible()
    page.get_by_role("link", name="Volver a mi ruta").click()
    expect(page.locator(".route .stop.done")).to_have_count(1, timeout=15000)
    expect(page.get_by_text("Resultado:")).to_be_visible(timeout=15000)  # el servidor ya la calificó

    ctx.set_offline(True)
    expect(page.get_by_text("Sin conexión: tu avance se guarda aquí")).to_be_visible()
    page.reload()  # la app abre sin red gracias al service worker
    expect(page.get_by_role("heading", name=re.compile("Tu ruta de la semana 1"))).to_be_visible(timeout=15000)
    page.get_by_role("link", name="Empezar").click()
    n = int(re.search(r"de (\d+)", page.locator(".progress").inner_text()).group(1))
    answer_practice(page, n)
    expect(page.get_by_text("Quedó guardada en este dispositivo")).to_be_visible()
    page.get_by_role("link", name="Volver a mi ruta").click()
    expect(page.get_by_text("pendiente de calificar")).to_be_visible()
    shot(page, "06-sin-conexion")
    ctx.set_offline(False)
    expect(page.get_by_text("Resultado:")).to_have_count(2, timeout=20000)  # se sincronizó sola

    # Termina la tercera práctica y presenta el cuestionario de salida (sin ayudas)
    page.get_by_role("link", name="Empezar").click()
    n = int(re.search(r"de (\d+)", page.locator(".progress").inner_text()).group(1))
    answer_practice(page, n)
    page.get_by_role("link", name="Volver a mi ruta").click()
    expect(page.get_by_text("Resultado:")).to_have_count(3, timeout=20000)
    page.get_by_role("link", name="Empezar").click()
    expect(page.get_by_text("Sin pistas ni tutor")).to_be_visible()
    expect(page.get_by_role("button", name="Dame una pista")).to_have_count(0)
    n = int(re.search(r"de (\d+)", page.locator(".progress").inner_text()).group(1))
    for i in range(n):
        page.get_by_role("radio").nth(0).click()
        page.get_by_role("button", name=re.compile("Siguiente pregunta|Entregar cuestionario")).click()
    expect(page.locator(".review details")).to_have_count(n)
    shot(page, "07-salida-resultado")
    page.get_by_role("link", name="Volver a mi ruta").click()
    expect(page.get_by_role("heading", name=re.compile("Tu ruta de la semana 2"))).to_be_visible(timeout=20000)
    shot(page, "08-semana-2")

    # Simulacro general
    page.get_by_role("link", name="Presentar").click()
    expect(page.locator(".timer")).to_be_visible(timeout=15000)
    total = page.locator(".grid-nav button").count()
    for i in range(total - 2):  # deja dos sin responder
        page.get_by_role("radio").nth(1).click()
        page.get_by_role("button", name="Siguiente", exact=True).click()
    shot(page, "09-simulacro")
    page.locator(".grid-nav button").nth(total - 1).click()
    page.get_by_role("button", name="Entregar simulacro").click()
    expect(page.get_by_role("heading", name="Revisión")).to_be_visible(timeout=15000)
    expect(page.get_by_text("sin responder")).to_have_count(2)
    shot(page, "10-simulacro-resultado")
    ctx.close()

    # 3. Estudiante nuevo: diagnóstico adaptativo completo en una área
    ctx, page = new_page(browser, mobile=True)
    login(page, "nuevo@colegio.test")
    page.get_by_role("link", name="Hacer diagnóstico").first.click()
    seen = 0
    expect(page.get_by_role("button", name="Responder y seguir")).to_be_visible(timeout=15000)
    while page.get_by_role("button", name="Responder y seguir").count():
        page.get_by_role("radio").nth(seen % 4).click()
        if seen == 0:
            shot(page, "11-diagnostico")
        page.get_by_role("button", name="Responder y seguir").click()
        seen += 1
        page.wait_for_function("document.querySelector('.result') || !document.querySelector('.option.chosen')", timeout=15000)
        assert seen <= 10
    expect(page.locator(".result")).to_contain_text("Nivel")
    assert 6 <= seen <= 10, seen
    shot(page, "12-diagnostico-resultado")
    ctx.close()

    # 4. Menor sin autorización: no entra hasta que el acudiente autoriza
    ctx, page = new_page(browser, mobile=True)
    login(page, "pendiente@colegio.test")
    expect(page.get_by_role("heading", name="Falta la autorización de datos")).to_be_visible()
    page.goto(BASE + "/diagnostico/MAT")
    expect(page.get_by_role("heading", name="Falta la autorización de datos")).to_be_visible()  # tampoco por enlace directo
    link = sys.argv[2] if len(sys.argv) > 2 else None
    if link:
        ctx2, guardian = new_page(browser, mobile=True)
        guardian.goto(link.replace("http://localhost:5173", BASE))
        expect(guardian.get_by_role("heading", name=re.compile("Autorización para"))).to_be_visible()
        shot(guardian, "13-autorizacion-acudiente")
        guardian.get_by_label("Nombre completo de quien autoriza").fill("Acudiente de Prueba")
        guardian.get_by_label("Parentesco").select_option("Madre")
        guardian.get_by_role("checkbox").check()
        guardian.get_by_role("button", name="Autorizar").click()
        expect(guardian.get_by_role("heading", name="Autorización registrada")).to_be_visible()
        ctx2.close()
        page.goto(BASE)
        expect(page.get_by_role("heading", name="Tu nivel por área")).to_be_visible(timeout=15000)
    ctx.close()

    # 5. Mayor de edad: autoriza al entrar
    ctx, page = new_page(browser)
    login(page, "mayor@colegio.test")
    page.get_by_role("checkbox").nth(0).check()
    page.get_by_role("checkbox").nth(1).check()
    page.get_by_role("button", name="Autorizar y continuar").click()
    expect(page.get_by_role("heading", name="Tu nivel por área")).to_be_visible(timeout=15000)
    shot(page, "14-inicio-sin-diagnostico")
    ctx.close()

    # 6. Docente, colegio y administrador
    ctx, page = new_page(browser)
    login(page, "mate@colegio.test")
    expect(page.get_by_role("heading", name="Dominio del grupo por competencia")).to_be_visible(timeout=15000)
    shot(page, "15-docente")
    page.get_by_role("button", name="Revisar preguntas").click()
    expect(page.get_by_role("button", name="Aprobar y publicar").first).to_be_visible(timeout=15000)
    shot(page, "16-docente-revision")
    page.get_by_role("button", name="Aprobar y publicar").first.click()
    page.get_by_role("button", name="Salir").click()
    expect(page.get_by_role("heading", name="Entrar")).to_be_visible()
    login(page, "rectoria@colegio.test")
    expect(page.get_by_role("heading", name="Estudiantes registrados")).to_be_visible(timeout=15000)
    shot(page, "17-colegio")
    page.get_by_role("button", name="Resultados por área").click()
    page.wait_for_timeout(1500)
    shot(page, "18-colegio-resultados")
    page.get_by_role("button", name="Salir").click()
    expect(page.get_by_role("heading", name="Entrar")).to_be_visible()
    login(page, "admin@rumbo11.test")
    expect(page.get_by_role("heading", name="Administración")).to_be_visible(timeout=15000)
    page.wait_for_timeout(1500)
    shot(page, "19-admin")
    with page.expect_download() as dl:
        page.get_by_role("button", name="Descargar datos anónimos (CSV)").click()
    csv = open(dl.value.path(), encoding="utf-8").read()
    assert "@" not in csv and "Estudiante" not in csv, "el CSV de investigación no debe traer nombres ni correos"
    print("CSV de investigación:", len(csv.splitlines()) - 1, "filas;", csv.splitlines()[0])
    ctx.close()
    browser.close()

print("ERRORES DE CONSOLA:", errors or "ninguno")
print("RECORRIDO COMPLETO")
