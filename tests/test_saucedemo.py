"""Tests automatizados para saucedemo.com con Playwright + pytest."""

import pytest
from helpers import login, texto_error


# ─── Test 1: Login data-driven ──────────────────────────────────────────────────

@pytest.mark.parametrize("usuario, resultado_esperado", [
    ("standard_user",           "exito"),
    ("locked_out_user",         "bloqueado"),
    ("performance_glitch_user", "exito"),
])
def test_login(pagina, usuario, resultado_esperado):
    login(pagina, usuario, "secret_sauce")

    if resultado_esperado == "exito":
        assert "/inventory.html" in pagina.url, (
            f"'{usuario}' no redirigió a inventory"
        )
        print(f"✅ Login exitoso con '{usuario}'")
    else:
        error = texto_error(pagina)
        assert error is not None, f"'{usuario}' debía mostrar error pero no lo hizo"
        assert "locked out" in error.lower()
        print(f"✅ Login bloqueado correctamente para '{usuario}'")


# ─── Test 2: Login con contraseña incorrecta ────────────────────────────────────

def test_login_contrasena_incorrecta(pagina):
    login(pagina, "standard_user", "wrong_pass")
    error = texto_error(pagina)
    assert error is not None, "No apareció el mensaje de error"
    assert "Username and password do not match" in error
    print("✅ TEST 2 PASÓ — Se muestra error de credenciales inválidas")


# ─── Test 3: Producto al carrito ────────────────────────────────────────────────

def test_agregar_producto_al_carrito(pagina):
    login(pagina, "standard_user", "secret_sauce")
    pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    contador = pagina.text_content(".shopping_cart_badge")
    assert contador == "1", f"Se esperaba '1' pero se obtuvo '{contador}'"
    print("✅ TEST 3 PASÓ — Producto agregado al carrito, badge muestra 1")


# ─── Test 4: Compra completa hasta el "Thank you" ──────────────────────────────

def test_compra_completa(pagina):
    login(pagina, "standard_user", "secret_sauce")
    pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    pagina.click(".shopping_cart_link")
    pagina.click("#checkout")
    pagina.fill("#first-name", "Silvia")
    pagina.fill("#last-name", "Meza")
    pagina.fill("#postal-code", "1234")
    pagina.click("#continue")
    pagina.click("#finish")
    mensaje = pagina.text_content(".complete-header")
    assert mensaje is not None, "No apareció el mensaje de confirmación"
    assert "Thank you for your order" in mensaje
    print("✅ TEST 4 PASÓ — Compra completada, aparece 'Thank you for your order'")
