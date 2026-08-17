import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
import streamlit as st
from scraper.cards import get_business_cards
from scraper.cards import open_business
from scraper.details import extract_business_details

from scraper.scroll import scroll_results
from scraper.browser import launch_browser
from scraper.google_maps import search_location

from exporter.json_export import export_json

from exporter.excel_export import export_excel

from utils.filename import generate_filename

from config import OUTPUT_FOLDER

st.set_page_config(
    page_title="LeadMap AI",
    page_icon="📍",
    layout="wide"
)

st.title("📍 LeadMap AI")

location = st.text_input(
    "Location",
    placeholder="Pune"
)

category = st.text_input(
    "Business Category",
    placeholder="Banquet Hall"
)

if st.button("Start Scraping"):

    playwright, browser, page = launch_browser()

    search_query = search_location(
        page,
        location,
        category
    )

    total = scroll_results(page)

    cards = get_business_cards(page)

    total = cards.count()

    print("=" * 60)
    print(f"Processing {total} Businesses")
    print("=" * 60)

    businesses = []

    for index in range(total):

        success = open_business(page, index)

        if not success:
            break

        print("Current URL:", page.url)

        business = extract_business_details(page)

        print("=" * 50)

        print("Name     :", business.name)
        print("Phone    :", business.phone)
        print("Website  :", business.website)
        print("Address  :", business.address)
        print("Rating   :", business.rating)
        print("Reviews  :", business.reviews)
        print("Maps URL :", business.maps_link)

        businesses.append(business)
    
    


    print("\n" + "="*60)
    print("Scraping Completed Successfully")
    print(f"Total Businesses Scraped : {len(businesses)}")
    print("="*60)

    filename = generate_filename(
        search_query,
        len(businesses)
    )

    export_json(
        businesses,
        OUTPUT_FOLDER,
        filename
    )

    export_excel(
        businesses,
        OUTPUT_FOLDER,
        filename
    )

    browser.close()
    playwright.stop()