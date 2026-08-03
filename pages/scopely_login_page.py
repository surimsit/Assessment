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

    def wait_for_input(self, INPUT):
        self.page.locator(
            INPUT
        ).wait_for(state="visible")

    def login_with_email(self, email):
        self.page.locator(self.EMAIL_INPUT).wait_for()
        self.page.locator(self.EMAIL_INPUT).fill(email)
        self.page.locator(
            self.CONTINUE_BUTTON
        ).wait_for()
        self.page.locator(
            self.CONTINUE_BUTTON
        ).click()

    def is_loaded(self):
        return "id.scopely.com" in self.page.url