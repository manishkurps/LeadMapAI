"""
scroll.py

This file is responsible for scrolling the Google Maps
results panel until all available businesses are loaded.
"""

from config import MAX_SCROLL_RETRY
from config import SCRAPE_ALL
from config import MAX_BUSINESSES
from config import WAIT_TIME


def scroll_results(page):
    """
    Scroll the Google Maps left side results panel
    until no new businesses are loaded.

    Parameters
    ----------
    page : Playwright Page

    Returns
    -------
    int
        Total number of business cards loaded.
    """

    print("=" * 50)
    print("Scrolling Started...")
    print("=" * 50)

    previous_count = 0

    retry = 0

    # MAX_RETRY = 5
    from config import MAX_SCROLL_RETRY

    while True:

        cards = page.locator('div[role="article"]')

        current_count = cards.count()

        # Stop after required number of businesses
        if not SCRAPE_ALL and current_count >= MAX_BUSINESSES:
            print(f"\nReached limit ({MAX_BUSINESSES})")
            return MAX_BUSINESSES

        print(f"Businesses Loaded : {current_count}")

        if current_count == previous_count:

            retry += 1

        else:

            retry = 0

        if retry >= MAX_SCROLL_RETRY:

            print("No more businesses found.")

            break

        previous_count = current_count

        cards.last.scroll_into_view_if_needed()

        page.wait_for_timeout(WAIT_TIME)

    print("=" * 50)

    return current_count