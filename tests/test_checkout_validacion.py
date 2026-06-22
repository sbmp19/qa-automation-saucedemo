"""Tests de validación del formulario de checkout."""

import pytest
from helpers import login, texto_error


class TestCheckoutValidacion:
    """Verifica los mensajes de error al dejar campos obligatorios vacíos."""

    @pytest.fixture(autouse=True)
    def setup(self, pagina):
        login(pagina, "standard_user", "secret_sauce")
        pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
        pagina.click(".shopping_cart_link")
        pagina.click("#checkout")

    def test_nombre_vacio(self, pagina):
        pagina.fill("#first-name", "")
        pagina.fill("#last-name", "Meza")
        pagina.fill("#postal-code", "1234")
        pagina.click("#continue")
        error = texto_error(pagina)
        assert error is not None, "No apareció mensaje de error"
        assert "First Name is required" in error

    def test_apellido_vacio(self, pagina):
        pagina.fill("#first-name", "Silvia")
        pagina.fill("#last-name", "")
        pagina.fill("#postal-code", "1234")
        pagina.click("#continue")
        error = texto_error(pagina)
        assert error is not None, "No apareció mensaje de error"
        assert "Last Name is required" in error

    def test_codigo_postal_vacio(self, pagina):
        pagina.fill("#first-name", "Silvia")
        pagina.fill("#last-name", "Meza")
        pagina.fill("#postal-code", "")
        pagina.click("#continue")
        error = texto_error(pagina)
        assert error is not None, "No apareció mensaje de error"
        assert "Postal Code is required" in error
