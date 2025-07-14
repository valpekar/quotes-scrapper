# Quotes Scraper

A clean-architecture Python package to scrape inspirational quotes from [quotes.toscrape.com](https://quotes.toscrape.com/tag/inspirational/), save them to a JSON file, and keep them up-to-date with unique IDs. Designed for easy reuse and automation.

## Features
- Scrapes quotes, authors, and tags from the 'inspirational' tag page
- Saves quotes to a JSON file, updating or adding as needed
- Assigns a unique, stable integer ID to each quote
- Clean, modular codebase (models, scraper, storage)
- Ready to use as a Python package in other projects
- Supports scheduled runs via cron job

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/quotes-scrapper.git
   cd quotes-scrapper
   ```
2. **Install dependencies:**
   ```bash
   pip install -e .
   ```
   Or, for system-wide install:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the scraper and save quotes to `quotes.json`:
```bash
python main.py
```
Or use the helper script:
```bash
./run_scraper.sh
```

## Using as a Package in Other Projects

After installing with `pip install -e .`, you can import and use the scraper in any Python project:
```python
from quotes_scraper.scraper.quote_scraper import QuoteScraper
from quotes_scraper.storage.json_storage import JsonStorage
```

## Scheduling with Cron

To run the scraper automatically twice a day:
1. Make sure `run_scraper.sh` is executable:
   ```bash
   chmod +x run_scraper.sh
   ```
2. Add this line to your crontab (`crontab -e`):
   ```
   0 6,18 * * * /Users/valeriyapekar/Work/py/quotes-scrapper/run_scraper.sh >> /Users/valeriyapekar/Work/py/quotes-scrapper/cron.log 2>&1
   ```

## Project Structure
```
quotes_scraper/
  models/
    quote.py
  scraper/
    quote_scraper.py
  storage/
    json_storage.py
main.py
run_scraper.sh
setup.py
requirements.txt
README.md
```

## License
MIT 