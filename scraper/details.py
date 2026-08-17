"""
Extract Business Details
"""


from scraper.selectors import *

from models.business import Business


def safe_text(locator):

    try:
        return locator.inner_text().strip()
    except:
        return ""


def safe_attribute(locator, attribute):

    try:
        value = locator.get_attribute(attribute)
        return value if value else ""
    except:
        return ""


def extract_business_details(page):

    business = Business()

    # Name
    business.name = safe_text(
        page.locator(BUSINESS_TITLE).first
    )

    # Phone
    business.phone = safe_text(
        page.locator(PHONE).locator("div.Io6YTe").first
    )

    # Website (display text)
    business.website = safe_text(
        page.locator(WEBSITE).locator("div.Io6YTe").first
    )

    # Address
    business.address = safe_text(
        page.locator(ADDRESS).locator("div.Io6YTe").first
    )

    # Rating
    business.rating = safe_text(
        page.locator(RATING).first
    )

    # Reviews
    try:
        business.reviews = page.locator(
            'button[aria-label*="reviews"] span'
        ).last.inner_text().strip()
    except:
        business.reviews = ""

    # Maps URL
    business.maps_link = page.url

    return business