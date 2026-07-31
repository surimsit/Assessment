from utils.config import BASE_URL


def test_launch_browser(page):
    page.goto(BASE_URL)
    assert "Stumble Guys" in page.title()
