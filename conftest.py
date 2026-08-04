from playwright.sync_api import sync_playwright
import pytest
from utils.config import BASE_URL
from pages.cookie_banner import CookieBanner


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-fullscreen"]
        )
        context = browser.new_context(
            viewport={
                "width": 1920,
                "height": 1080
            }
        )
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="session")
def app_url():
    return BASE_URL


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(
                path=f"screenshots/{item.name}.png"
            )


@pytest.fixture
def mobile_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )
        pixel = p.devices["Pixel 7"]
        context = browser.new_context(**pixel)
        page = context.new_page()
        page.goto("https://www.stumbleguys.com")
        yield page
        browser.close()


@pytest.fixture
def open_home(page):
    page.goto(BASE_URL)

    CookieBanner(page).accept_all()

    return page
