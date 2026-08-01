from playwright.sync_api import TimeoutError


class CookieBanner:

    def __init__(self, page):
        self.page = page

    def accept_all(self):

        try:
            self.page.get_by_role(
                "button",
                name="Accept All"
            ).click(timeout=5000)

        except TimeoutError:
            pass