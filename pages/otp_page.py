from pages.base_page import BasePage


class OtpPage(BasePage):

    OTP_INPUTS = "input[data-index]"
    SIGN_IN_BUTTON = "button:has-text('Sign in')"

    def enter_otp(self, otp):
        otp = str(otp)
        inputs = self.page.locator(self.OTP_INPUTS)
        for i in range(6):
            inputs.nth(i).fill(otp[i])

    def click_sign_in(self):
        self.page.locator(
            self.SIGN_IN_BUTTON
        ).click()

    def submit_otp(self, otp):
        self.enter_otp(otp)
        self.page.locator(
            self.SIGN_IN_BUTTON
        ).wait_for(state="visible")
        self.click_sign_in()

    def wait_for_otp_screen(self):
        self.page.locator(
            self.OTP_INPUTS
        ).nth(0).wait_for(state="visible")