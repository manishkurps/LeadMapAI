"""
cards.py

Responsible for collecting all business cards.
"""

from scraper.selectors import BUSINESS_CARD


def get_business_cards(page):
    """
    Returns all currently loaded business cards.
    """

    cards = page.locator(BUSINESS_CARD)

    total = cards.count()

    print("=" * 50)
    print(f"Business Cards Found : {total}")
    print("=" * 50)

    return cards

def open_business(page, index):

    from scraper.selectors import BUSINESS_CARD

    cards = page.locator(BUSINESS_CARD)

    total = cards.count()

    if index >= total:
        return False

    card = cards.nth(index)

    # Make sure the card is visible
    card.scroll_into_view_if_needed()

    page.wait_for_timeout(1000)

    # Click the center of the card
    card.click(force=True)

    page.wait_for_timeout(2500)

    return True