from pages.base_page import BasePage


class StorePage(BasePage):

    def select_package(self, package_locator):

        self.click(package_locator)

    def buy(self):

        self.click("text=Buy")