"""Funciones auxiliares reutilizables para los tests."""


def login(page, usuario, contrasena):
    page.fill("#user-name", usuario)
    page.fill("#password", contrasena)
    page.click("#login-button")


def texto_error(page):
    return page.text_content('[data-test="error"]')
