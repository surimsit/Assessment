from pages.base_page import BasePage


class HomePage(BasePage):
    PROFILE_MENU = "img[alt='avatar']"

    def open_profile_menu(self):
        self.page.locator(
            self.PROFILE_MENU
        ).first.hover()

    def click_login(self):
        self.open_profile_menu()
        login_button = self.page.get_by_role(
            "button",
            name="Login"
        )
        assert login_button.is_visible()
        login_button.click()

    def is_logout_visible(self):
        self.open_profile_menu()
        logout_button = self.page.get_by_role(
            "button",
            name="Logout"
        )
        return (
                logout_button.is_visible()
                and logout_button.is_enabled()
        )

    def is_loaded(self):
        self.page.wait_for_url(
            "https://www.stumbleguys.com/",
            timeout=30000
        )
        return self.page.locator(
            self.PROFILE_MENU
        ).first.is_visible()
