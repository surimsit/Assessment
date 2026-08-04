from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.shop_page import ShopPage
from services.auth_service import AuthService


def test_user_can_login_with_email_otp(open_home):
    page = open_home
    AuthService(page).login_with_email_otp()


def test_user_can_reach_purchase_step(open_home):
    page = open_home
    AuthService(page).login_with_email_otp()
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


def test_user_can_launch_webgl_game(open_home):
    page = open_home
    home = HomePage(page)
    game = home.open_game()
    game.wait_for_webgl_game()
    game.click_start_playing()
    game.drag_age_slider_to_25()
    game.click_accept()
    game.click_update_ok_if_present()


def test_login_flow_mobile(mobile_page):
    page = mobile_page
    HomePage(page).click_login()
    LoginPage(page).continue_with_email()

