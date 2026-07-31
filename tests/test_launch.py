


def test_launch_browser(page):
    page.goto("https://www.stumbleguys.com")
    assert "Stumble Guys" in page.title()