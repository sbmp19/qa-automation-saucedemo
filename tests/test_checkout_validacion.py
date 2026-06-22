"""Tests de validación del formulario de checkout."""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckoutValidacion:
    """Verifica los mensajes de error al dejar campos obligatorios vacíos."""

    @pytest.fixture(autouse=True)
    def setup(self, pagina):
        login_page = LoginPage(pagina)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(pagina)
        inventory_page.add_product_to_cart("sauce-labs-backpack")
        inventory_page.go_to_cart()

        cart_page = CartPage(pagina)
        cart_page.go_to_checkout()

    def test_nombre_vacio(self, pagina):
        checkout_page = CheckoutPage(pagina)
        checkout_page.fill_info("", "Meza", "1234")
        checkout_page.click_continue()
        error = checkout_page.texto_error()
        assert error is not None, "No apareció mensaje de error"
        assert "First Name is required" in error

    def test_apellido_vacio(self, pagina):
        checkout_page = CheckoutPage(pagina)
        checkout_page.fill_info("Silvia", "", "1234")
        checkout_page.click_continue()
        error = checkout_page.texto_error()
        assert error is not None, "No apareció mensaje de error"
        assert "Last Name is required" in error

    def test_codigo_postal_vacio(self, pagina):
        checkout_page = CheckoutPage(pagina)
        checkout_page.fill_info("Silvia", "Meza", "")
        checkout_page.click_continue()
        error = checkout_page.texto_error()
        assert error is not None, "No apareció mensaje de error"
        assert "Postal Code is required" in error
