# """
# extractor.py

# This file collects all business cards
# currently visible in Google Maps.
# """
# from scraper.selectors import BUSINESS_CARD

# def get_business_cards(page):

#     print("=" * 50)

#     print("Collecting Business Cards")

#     print("=" * 50)

#     # cards = page.locator('div[role="article"]')
#     cards = page.locator(BUSINESS_CARD)

#     total = cards.count()

#     print(f"Total Cards Found : {total}")

#     print("\nInspecting First Business Card\n")

#     print(cards.first.inner_text())

#     return cards

"""
extractor.py

Responsible for opening each business
and extracting details.
"""

from scraper.selectors import BUSINESS_CARD


def open_business(page, index):
    """
    Open a business using its index.
    """

    cards = page.locator(BUSINESS_CARD)

    total = cards.count()

    if index >= total:
        return False

    print(f"\nOpening Business {index + 1}/{total}")

    cards.nth(index).click()

    page.wait_for_timeout(3000)

    return True