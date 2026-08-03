class ShopPage:

    SHOP_LINK = "a[href='/shop']"
    PURCHASE_BUTTONS = "button[class*='price_button']"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.get_by_role(
            "navigation"
        ).get_by_role(
            "link",
            name="Shop"
        ).click()

    def is_loaded(self):
        self.page.wait_for_url("https://www.stumbleguys.com/shop")
        return "/shop" in self.page.url

    def click_first_purchase_item(self):
        self.page.locator(
            self.PURCHASE_BUTTONS
        ).first.click()