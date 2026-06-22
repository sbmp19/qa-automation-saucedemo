from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sort_dropdown = page.locator(".product_sort_container")
        self.inventory_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def sort_by_price_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def sort_by_price_high_to_low(self):
        self.sort_dropdown.select_option("hilo")

    def get_prices(self):
        prices = self.inventory_prices.all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def add_product_to_cart(self, product_id):
        self.page.click(f'[data-test="add-to-cart-{product_id}"]')

    def go_to_cart(self):
        self.cart_link.click()

    def get_cart_badge_count(self):
        return self.cart_badge.text_content()
