"""
Google Maps Selectors

If Google changes their HTML,
we only modify this file.
"""


# Search
SEARCH_BOX = 'input[name="q"], #searchboxinput'

# Business Cards
BUSINESS_CARD = 'div[role="article"]'

# Details Panel
BUSINESS_TITLE = "h1.DUwDvf.lfPIob"

PHONE = 'button[data-item-id^="phone"]'

WEBSITE = 'a[data-item-id="authority"]'

ADDRESS = 'button[data-item-id="address"]'

RATING = "div.fontDisplayLarge"

REVIEWS = 'button[aria-label*="reviews"], span'