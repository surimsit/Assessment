from playwright.sync_api import sync_playwright
import pytest
from utils.config import BASE_URL


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )
        context = browser.new_context()
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
def mobile_page(playwright):
    device = playwright.devices["Pixel 7"]
    browser = playwright.chromium.launch(
        headless=False
    )
    context = browser.new_context(
        **device
    )
    page = context.new_page()
    yield page
    browser.close()
