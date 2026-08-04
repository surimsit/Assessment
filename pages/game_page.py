from playwright.sync_api import Page, expect
import re


class GamePage:
    START_PLAYING_BUTTON = "text=Start Playing"

    def __init__(self, page: Page):
        self.page = page

        self.loading_percentage = page.get_by_text(
            re.compile(r"\d+\s*%")
        )

        self.webgl_canvas = page.locator(
            "#react-unity-webgl-canvas-1"
        )

    def wait_for_loading_complete(self):
        self.page.wait_for_timeout(100000)
        print(
            self.loading_percentage.first.text_content()
        )

    def wait_for_webgl_game2(self):
        expect(
            self.webgl_canvas
        ).to_be_visible(
            timeout=120000
        )

    def get_canvas_box(self):
        canvas_box = self.webgl_canvas.bounding_box()

        assert canvas_box is not None, \
            "Unable to determine canvas position"

        return canvas_box

    def click_canvas_position(
            self,
            x_ratio: float,
            y_ratio: float):

        canvas = self.get_canvas_box()

        x = canvas["x"] + canvas["width"] * x_ratio
        y = canvas["y"] + canvas["height"] * y_ratio

        self.page.mouse.click(x, y)

    def click_start_playing(self):
        """
        Adjust ratios after validating with screenshots.
        """
        self.click_canvas_position(
            x_ratio=0.50,
            y_ratio=0.75
        )

    def drag_age_slider_to_25(self):
        """
        Adjust coordinates after observing
        the actual age-selection screen.
        """

        canvas = self.get_canvas_box()

        slider_y = canvas["y"] + canvas["height"] * 0.56

        start_x = canvas["x"] + canvas["width"] * 0.30
        end_x = canvas["x"] + canvas["width"] * 0.43

        self.page.mouse.move(
            start_x,
            slider_y
        )

        self.page.mouse.down()

        self.page.mouse.move(
            end_x,
            slider_y,
            steps=20
        )

        self.page.mouse.up()

    def click_accept(self):
        self.click_canvas_position(
            x_ratio=0.50,
            y_ratio=0.82
        )

    def click_update_ok_if_present(self):
        """
        Optional popup.
        If popup is not displayed,
        this click should be skipped or
        coordinates adjusted.
        """

        self.page.wait_for_timeout(3000)

        self.click_canvas_position(
            x_ratio=0.50,
            y_ratio=0.66
        )

    def take_screenshot(
            self,
            name="webgl_state.png"):
        self.page.screenshot(
            path=name,
            full_page=True
        )

    def wait_for_webgl_game(self):
        self.page.locator(
            self.START_PLAYING_BUTTON
        ).wait_for(
            state="visible",
            timeout=180000
        )