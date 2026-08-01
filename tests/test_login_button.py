from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.scopely_login_page import ScopelyLoginPage


def test_login_menu(open_home):

    page = open_home

    HomePage(page).click_login()

    LoginPage(page).continue_with_email()

    assert "id.scopely.com" in page.url

    scopely = ScopelyLoginPage(page)

    email_input = page.locator("input[name='email']")
    email_input.wait_for(state="visible")

    assert email_input.is_visible()

    scopely.enter_email("surechirra@gmail.com")

    continue_btn = page.locator(
        "[data-test-id='site-email-input-submit-button']"
    )

    assert continue_btn.is_enabled()

    page.wait_for_timeout(5000)