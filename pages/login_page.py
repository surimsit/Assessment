from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = "input[type='email']"
    PASSWORD = "input[type='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def login(self, username, password):

        self.fill(self.EMAIL, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def continue_with_email(self):
        login_dialog = self.page.get_by_role(
            "heading",
            name="Login"
        )
        assert login_dialog.is_visible()
        self.page.get_by_role(
            "button",
            name="Continue with email"
        ).click()