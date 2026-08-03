from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = "input[type='email']"
    PASSWORD = "input[type='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def continue_with_email(self):
        email_button = self.page.get_by_role(
            "button",
            name="Continue with email"
        )

        email_button.wait_for(
            state="visible"
        )
        email_button.click()