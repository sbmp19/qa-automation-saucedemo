"""Tests de ordenamiento de productos en el inventario."""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestOrdenamiento:
    """Verifica que el ordenamiento por precio funcione correctamente."""

    def test_ordenar_precio_menor_a_mayor(self, pagina):
        login_page = LoginPage(pagina)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(pagina)
        inventory_page.sort_by_price_low_to_high()
        prices = inventory_page.get_prices()
        assert prices == sorted(prices), (
            "Los precios no están ordenados de menor a mayor"
        )

    def test_ordenar_precio_mayor_a_menor(self, pagina):
        login_page = LoginPage(pagina)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(pagina)
        inventory_page.sort_by_price_high_to_low()
        prices = inventory_page.get_prices()
        assert prices == sorted(prices, reverse=True), (
            "Los precios no están ordenados de mayor a menor"
        )
