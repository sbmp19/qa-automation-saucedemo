from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkout")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def remove_product(self, product_id):
        self.page.click(f'[data-test="remove-{product_id}"]')

    def go_to_checkout(self):
        self.checkout_button.click()

    def get_item_count(self):
        if self.cart_badge.is_visible():
            return self.cart_badge.text_content()
        return None
