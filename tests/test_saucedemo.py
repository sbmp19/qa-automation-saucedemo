"""Tests automatizados para saucedemo.com con Playwright + pytest."""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize("usuario, resultado_esperado", [
    ("standard_user",           "exito"),
    ("locked_out_user",         "bloqueado"),
    ("performance_glitch_user", "exito"),
])
def test_login(pagina, usuario, resultado_esperado):
    login_page = LoginPage(pagina)
    login_page.login(usuario, "secret_sauce")

    if resultado_esperado == "exito":
        assert "/inventory.html" in pagina.url, (
            f"'{usuario}' no redirigió a inventory"
        )
    else:
        error = login_page.texto_error()
        assert error is not None, f"'{usuario}' debía mostrar error pero no lo hizo"
        assert "locked out" in error.lower()


def test_login_contrasena_incorrecta(pagina):
    login_page = LoginPage(pagina)
    login_page.login("standard_user", "wrong_pass")
    error = login_page.texto_error()
    assert error is not None, "No apareció el mensaje de error"
    assert "Username and password do not match" in error


def test_agregar_producto_al_carrito(pagina):
    login_page = LoginPage(pagina)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(pagina)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    contador = inventory_page.get_cart_badge_count()
    assert contador == "1", f"Se esperaba '1' pero se obtuvo '{contador}'"


def test_compra_completa(pagina):
    login_page = LoginPage(pagina)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(pagina)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(pagina)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(pagina)
    checkout_page.fill_info("Silvia", "Meza", "1234")
    checkout_page.click_continue()
    checkout_page.click_finish()

    mensaje = checkout_page.get_complete_header()
    assert mensaje is not None, "No apareció el mensaje de confirmación"
    assert "Thank you for your order" in mensaje
