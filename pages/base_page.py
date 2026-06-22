class BasePage:
    def __init__(self, page):
        self.page = page

    def texto_error(self):
        return self.page.text_content('[data-test="error"]')
