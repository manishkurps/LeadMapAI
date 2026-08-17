"""
Application Configuration
"""

# -----------------------------
# Browser Settings
# -----------------------------

HEADLESS = False

GOOGLE_MAPS_URL = "https://www.google.com/maps"

WAIT_TIME = 2500

SEARCH_WAIT = 5000


# -----------------------------
# Scraper Settings
# -----------------------------

# Set to True to scrape every business
SCRAPE_ALL = False

# Used only when SCRAPE_ALL = False
MAX_BUSINESSES = 40

# Number of times to retry scrolling
MAX_SCROLL_RETRY = 5


# -----------------------------
# Export Settings
# -----------------------------

OUTPUT_FOLDER = "output"