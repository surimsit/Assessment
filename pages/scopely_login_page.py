from pages.base_page import BasePage


class ScopelyLoginPage(BasePage):

    EMAIL_INPUT = "input[name='email']"
    CONTINUE_BUTTON = "[data-test-id='site-email-input-submit-button']"

    def enter_email(self, email):

        self.page.locator(
            self.EMAIL_INPUT
        ).fill(email)

    def click_continue(self):

        self.page.locator(
            self.CONTINUE_BUTTON
        ).click()