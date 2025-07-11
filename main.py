# This file will serve as the entry point for the quote scraper project.
# The project follows a clean architecture with the following modules:
# - models/quote.py: Quote data model
# - scraper/quote_scraper.py: Scraper logic
# - storage/json_storage.py: JSON storage logic
#
# The main function will orchestrate scraping and saving quotes.

from quotes_scraper.scraper.quote_scraper import QuoteScraper
from quotes_scraper.storage.json_storage import JsonStorage

INSPIRATIONAL_URL = "https://quotes.toscrape.com/tag/inspirational/"
OUTPUT_FILE = "quotes.json"

def main():
    scraper = QuoteScraper(INSPIRATIONAL_URL)
    quotes = scraper.fetch_quotes()
    storage = JsonStorage(OUTPUT_FILE)
    storage.save_quotes(quotes)
    print(f"Scraped {len(quotes)} quotes and saved to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
