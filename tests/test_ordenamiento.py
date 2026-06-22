"""Tests de ordenamiento de productos en el inventario."""

import pytest
from helpers import login


class TestOrdenamiento:
    """Verifica que el ordenamiento por precio funcione correctamente."""

    def test_ordenar_precio_menor_a_mayor(self, pagina):
        login(pagina, "standard_user", "secret_sauce")
        pagina.select_option(".product_sort_container", "lohi")
        prices = pagina.locator(".inventory_item_price").all_text_contents()
        prices_float = [float(p.replace("$", "")) for p in prices]
        assert prices_float == sorted(prices_float), (
            "Los precios no están ordenados de menor a mayor"
        )

    def test_ordenar_precio_mayor_a_menor(self, pagina):
        login(pagina, "standard_user", "secret_sauce")
        pagina.select_option(".product_sort_container", "hilo")
        prices = pagina.locator(".inventory_item_price").all_text_contents()
        prices_float = [float(p.replace("$", "")) for p in prices]
        assert prices_float == sorted(prices_float, reverse=True), (
            "Los precios no están ordenados de mayor a menor"
        )
