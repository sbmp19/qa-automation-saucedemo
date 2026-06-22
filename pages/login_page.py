from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, usuario, contrasena):
        self.username_input.fill(usuario)
        self.password_input.fill(contrasena)
        self.login_button.click()
