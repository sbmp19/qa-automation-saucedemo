"""Configuración global de pytest: fixture del navegador y captura de screenshots."""

import base64

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def pagina():
    """Abre una página nueva en Chromium para cada test y la cierra al final."""
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        page = navegador.new_page()
        page.goto("https://www.saucedemo.com")
        yield page
        navegador.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Toma una captura de pantalla si el test falla y la incrusta en el reporte HTML."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        pagina = item.funcargs.get("pagina")
        if pagina:
            screenshot = pagina.screenshot()
            encoded = base64.b64encode(screenshot).decode("utf-8")
            from pytest_html import extras
            report.extras = getattr(report, "extras", [])
            report.extras.append(extras.png(encoded, "Screenshot al fallar"))
