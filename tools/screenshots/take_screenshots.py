"""Take the nine lecture screenshots of Coffee and Wifi with headless Chromium.

@file take_screenshots.py
@brief Runs the app in-process on a temp copy of the CSV and saves PNGs to /out.
"""

import logging
import os
import shutil
import sys
import tempfile
import threading
from pathlib import Path

from playwright.sync_api import Page, sync_playwright
from werkzeug.serving import make_server

from coffee_and_wifi.constants import (
    CSV_ENCODING,
    DEFAULT_DATA_FILE,
    HOST,
    MAPS_LINK_TEXT,
    ROUTE_ADD,
    ROUTE_CAFES,
    ROUTE_HOME,
)
from coffee_and_wifi.presentation.app import create_app

## @brief Folder inside the container that is bound to docs/screenshots.
OUT_DIR = Path(os.environ.get("SCREENSHOT_OUT_DIR", "/out"))
## @brief Browser viewport.
VIEWPORT = {"width": 1280, "height": 800}
## @brief Number of CSV lines shown in the file tail page.
TAIL_LINES = 6
## @brief Timeout for any browser step, in milliseconds.
STEP_TIMEOUT_MS = 15_000
## @brief Smallest PNG size that counts as a real screenshot, in bytes.
MIN_PNG_BYTES = 5_000
## @brief Values typed into the add form.
VALID_FORM = {
    "#cafe": "Screenshot Cafe, Soho",
    "#location": "https://goo.gl/maps/screenshot",
    "#open_time": "8AM",
    "#close_time": "5PM",
}
## @brief Rating choices selected in the add form.
VALID_SELECTS = {
    "#coffee_rating": "☕️☕️☕️",
    "#wifi_rating": "💪💪💪",
    "#power_rating": "🔌🔌",
}
## @brief An invalid location for the validation error shot.
INVALID_URL = "not-a-url"
## @brief CSS that outlines the Maps links.
HIGHLIGHT_CSS = (
    f"a:not([href='/']):not([href='{ROUTE_CAFES}']):not([href='{ROUTE_ADD}'])"
    "{outline:3px solid #ffc107;background:#ffc10733;padding:2px 4px}"
)
## @brief Style of the CSV tail page.
TAIL_PAGE = (
    "<html><body style='background:#212529;color:#f8f9fa;padding:24px;"
    "font-family:sans-serif'><h2>cafe-data.csv (last {n} lines)</h2>"
    "<pre style='font-size:15px;white-space:pre-wrap'>{text}</pre></body></html>"
)

logger = logging.getLogger("screenshots")


def _shot(page: Page, name: str, full_page: bool = False) -> None:
    path = OUT_DIR / name
    page.screenshot(path=str(path), full_page=full_page)
    size = path.stat().st_size
    if size < MIN_PNG_BYTES:
        raise RuntimeError(f"{name} is too small ({size} bytes)")
    logger.info("saved %s (%d bytes)", name, size)


def _expect_ok(page: Page, url: str) -> None:
    status = page.request.get(url).status
    if status != 200:
        raise RuntimeError(f"{url} answered {status}")


def _fill_form(page: Page, location: str) -> None:
    for selector, value in VALID_FORM.items():
        page.fill(selector, value)
    page.fill("#location", location)
    for selector, value in VALID_SELECTS.items():
        page.select_option(selector, value)


def _capture(page: Page, base: str, data_file: Path) -> None:
    page.goto(base + ROUTE_HOME)
    _shot(page, "01-home-page.png")

    page.goto(base + ROUTE_CAFES)
    _shot(page, "02-cafes-table.png", full_page=True)

    page.add_style_tag(content=HIGHLIGHT_CSS)
    page.locator(f"text={MAPS_LINK_TEXT}").first.scroll_into_view_if_needed()
    _shot(page, "03-maps-links.png")

    page.goto(base + ROUTE_HOME)
    button = page.get_by_role("button", name="Show Me!")
    button.hover()
    button.click()
    page.wait_for_url(base + ROUTE_CAFES)
    _shot(page, "04-show-me-button.png", full_page=True)

    page.goto(base + ROUTE_ADD)
    _shot(page, "05-secret-add-form.png", full_page=True)

    _fill_form(page, INVALID_URL)
    page.get_by_role("button", name="Submit").click()
    page.wait_for_selector("text=Enter a valid URL")
    _shot(page, "06-url-validation-error.png", full_page=True)

    _fill_form(page, VALID_FORM["#location"])
    page.get_by_role("button", name="Submit").click()
    page.wait_for_url(base + ROUTE_CAFES)
    page.wait_for_selector("text=Screenshot Cafe")
    _shot(page, "07-cafe-added.png", full_page=True)

    lines = data_file.read_text(encoding=CSV_ENCODING).splitlines()[-TAIL_LINES:]
    if "Screenshot Cafe" not in lines[-1]:
        raise RuntimeError("new cafe is not the last CSV line")
    html = TAIL_PAGE.format(n=TAIL_LINES, text="\n".join(lines))
    page.set_content(html)
    _shot(page, "08-csv-appended.png")

    page.goto(base + ROUTE_ADD)
    for href in ("/", ROUTE_CAFES):
        _expect_ok(page, base + href)
    _shot(page, "09-navigation-links.png", full_page=True)
    page.get_by_role("link", name="See all cafes").click()
    page.wait_for_url(base + ROUTE_CAFES)
    page.get_by_role("link", name="Return to index page").click()
    page.wait_for_url(base + "/")


def main() -> int:
    """Run the app, drive the browser and write the screenshots."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        data_file = Path(tmp) / "cafe-data.csv"
        shutil.copy(DEFAULT_DATA_FILE, data_file)
        app = create_app({"DATA_FILE": data_file})
        server = make_server(HOST, 0, app)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f"http://{HOST}:{server.server_port}"
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(viewport=VIEWPORT)
                page.set_default_timeout(STEP_TIMEOUT_MS)
                _capture(page, base, data_file)
                browser.close()
        finally:
            server.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
