"""Tests de funcionalidad del carrito de compras."""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCarrito:
    """Verifica el comportamiento del carrito al agregar y quitar productos."""

    def test_agregar_tres_y_quitar_uno(self, pagina):
        login_page = LoginPage(pagina)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(pagina)
        inventory_page.add_product_to_cart("sauce-labs-backpack")
        inventory_page.add_product_to_cart("sauce-labs-bike-light")
        inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")

        contador = inventory_page.get_cart_badge_count()
        assert contador == "3", f"Se esperaba '3' pero se obtuvo '{contador}'"

        inventory_page.go_to_cart()

        cart_page = CartPage(pagina)
        cart_page.remove_product("sauce-labs-backpack")

        contador = cart_page.get_item_count()
        assert contador == "2", f"Se esperaba '2' pero se obtuvo '{contador}'"
