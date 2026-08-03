class PaymentPage:

    def __init__(self, page):
        self.page = page

    def is_loaded(self):

        try:
            self.page.wait_for_load_state(
                "networkidle",
                timeout=10000
            )
        except:
            pass

        return (
                "shop" in self.page.url
                or self.page.locator("button").count() > 0
        )

    def is_purchase_button_visible(self):

        buttons = self.page.locator("button")

        return buttons.count() > 0
