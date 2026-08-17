from config import GOOGLE_MAPS_URL
from config import SEARCH_WAIT
from scraper.selectors import SEARCH_BOX

from utils.filename import generate_filename

def search_location(page, location, category):

    search_query = f"{category} {location}"

    print(f"Searching: {search_query}")


    page.goto(GOOGLE_MAPS_URL)
    print(page.url)
    print(page.title())

    page.wait_for_timeout(2000)

    search_box = page.locator(SEARCH_BOX).first

    search_box.wait_for(state="visible")

    search_box.fill(search_query)

    search_box.press("Enter")

    page.wait_for_timeout(SEARCH_WAIT)

    return search_query