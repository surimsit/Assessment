from pages.base_page import BasePage


class HomePage(BasePage):

    PROFILE_MENU = "img[alt='avatar']"

    def click_login(self):
        self.page.locator(
            self.PROFILE_MENU
        ).first.hover()

        login_button = self.page.get_by_role(
            "button",
            name="Login"
        )
        assert login_button.is_visible()
        login_button.click()