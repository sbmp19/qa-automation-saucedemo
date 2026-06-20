"""Tests automatizados para saucedemo.com con Playwright + pytest."""

import pytest
from playwright.sync_api import sync_playwright


# ─── Fixture: crea una página nueva por cada test ──────────────────────────────

@pytest.fixture
def pagina():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        page = navegador.new_page()
        page.goto("https://www.saucedemo.com")
        yield page
        navegador.close()


# ─── Helpers ────────────────────────────────────────────────────────────────────

def login(page, usuario, contrasena):
    page.fill("#user-name", usuario)
    page.fill("#password", contrasena)
    page.click("#login-button")


def texto_error(page):
    return page.text_content('[data-test="error"]')


# ─── Test 1: Producto al carrito (test original) ───────────────────────────────

def test_agregar_producto_al_carrito(pagina):
    login(pagina, "standard_user", "secret_sauce")
    pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    contador = pagina.text_content(".shopping_cart_badge")
    assert contador == "1", f"Se esperaba '1' pero se obtuvo '{contador}'"
    print("✅ TEST 1 PASÓ — Producto agregado al carrito, badge muestra 1")


# ─── Test 2: Login con contraseña incorrecta ────────────────────────────────────

def test_login_contrasena_incorrecta(pagina):
    login(pagina, "standard_user", "wrong_pass")
    error = texto_error(pagina)
    assert error is not None, "No apareció el mensaje de error"
    assert "Username and password do not match" in error
    print("✅ TEST 2 PASÓ — Se muestra error de credenciales inválidas")


# ─── Test 3: Login con usuario bloqueado ────────────────────────────────────────

def test_login_usuario_bloqueado(pagina):
    login(pagina, "locked_out_user", "secret_sauce")
    error = texto_error(pagina)
    assert error is not None, "No apareció el mensaje de error"
    assert "locked out" in error.lower()
    print("✅ TEST 3 PASÓ — Se muestra error de usuario bloqueado")


# ─── Test 4: Compra completa hasta el "Thank you" ──────────────────────────────

def test_compra_completa(pagina):
    # Login
    login(pagina, "standard_user", "secret_sauce")

    # Agregar producto al carrito
    pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')

    # Ir al carrito y hacer clic en Checkout
    pagina.click(".shopping_cart_link")
    pagina.click("#checkout")

    # Completar información de envío
    pagina.fill("#first-name", "Silvia")
    pagina.fill("#last-name", "Meza")
    pagina.fill("#postal-code", "1234")
    pagina.click("#continue")

    # Confirmar compra
    pagina.click("#finish")

    # Verificar mensaje de éxito
    mensaje = pagina.text_content(".complete-header")
    assert mensaje is not None, "No apareció el mensaje de confirmación"
    assert "Thank you for your order" in mensaje
    print("✅ TEST 4 PASÓ — Compra completada, aparece 'Thank you for your order'")
