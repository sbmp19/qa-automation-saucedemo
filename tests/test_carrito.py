"""Tests de funcionalidad del carrito de compras."""

import pytest
from helpers import login


class TestCarrito:
    """Verifica el comportamiento del carrito al agregar y quitar productos."""

    def test_agregar_tres_y_quitar_uno(self, pagina):
        login(pagina, "standard_user", "secret_sauce")
        pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
        pagina.click('[data-test="add-to-cart-sauce-labs-bike-light"]')
        pagina.click('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')

        contador = pagina.text_content(".shopping_cart_badge")
        assert contador == "3", f"Se esperaba '3' pero se obtuvo '{contador}'"

        pagina.click(".shopping_cart_link")
        pagina.click('[data-test="remove-sauce-labs-backpack"]')

        contador = pagina.text_content(".shopping_cart_badge")
        assert contador == "2", f"Se esperaba '2' pero se obtuvo '{contador}'"
