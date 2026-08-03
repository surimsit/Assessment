from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.otp_page import OtpPage
from pages.payment_page import PaymentPage
from pages.scopely_login_page import ScopelyLoginPage
from pages.shop_page import ShopPage
from utils.config import TEST_EMAIL, EMAIL_APP_PASSWORD
from utils.email_helper import EmailHelper
from datetime import datetime, timezone


def test_login_flow(open_home):
    page = open_home
    HomePage(page).click_login()
    LoginPage(page).continue_with_email()

    scopely_page = ScopelyLoginPage(page)
    assert scopely_page.is_loaded()
    otp_request_time = datetime.now(timezone.utc)
    scopely_page.login_with_email(TEST_EMAIL)
    otp_page = OtpPage(page)
    otp_page.wait_for_otp_screen()
    otp = EmailHelper.get_latest_otp(
        email=TEST_EMAIL,
        password=EMAIL_APP_PASSWORD,
        received_after=otp_request_time
    )
    otp_page.submit_otp(otp)
    home = HomePage(page)
    assert home.is_loaded()
    assert home.is_logout_visible()


def test_purchase_flow(open_home):
    page = open_home
    HomePage(page).click_login()
    LoginPage(page).continue_with_email()

    scopely_page = ScopelyLoginPage(page)
    assert scopely_page.is_loaded()
    otp_request_time = datetime.now(timezone.utc)
    scopely_page.login_with_email(TEST_EMAIL)
    otp_page = OtpPage(page)
    otp_page.wait_for_otp_screen()
    otp = EmailHelper.get_latest_otp(
        email=TEST_EMAIL,
        password=EMAIL_APP_PASSWORD,
        received_after=otp_request_time
    )
    otp_page.submit_otp(otp)
    home = HomePage(page)
    assert home.is_loaded()
    assert home.is_logout_visible()

    shop = ShopPage(page)
    shop.open()
    assert shop.is_loaded(), \
        "Shop page not loaded"
    shop.click_first_purchase_item()
    payment = PaymentPage(page)
    assert payment.is_loaded(), \
        "Purchase popup was not displayed"
    assert payment.is_purchase_button_visible(), \
        "Purchase button not visible"

