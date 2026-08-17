from playwright.sync_api import sync_playwright
from config import HEADLESS


def launch_browser():

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=300
    )

    context = browser.new_context(
        viewport={"width": 1400, "height": 900}
    )

    page = context.new_page()

    page.set_default_timeout(60000)

    return playwright, browser, page