import requests
from bs4 import BeautifulSoup
from typing import List
from models.quote import Quote

class QuoteScraper:
    """Scrapes quotes from a given URL."""
    def __init__(self, url: str):
        self.url = url

    def fetch_quotes(self) -> List[Quote]:
        """Fetch and parse quotes from the URL."""
        response = requests.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_elements = soup.select('div.quote')
        quotes = []
        for element in quotes_elements:
            text_elem = element.select_one('span.text')
            text = text_elem.get_text(strip=True) if text_elem else ''
            author_elem = element.select_one('small.author')
            author = author_elem.get_text(strip=True) if author_elem else ''
            tags = [tag.get_text(strip=True) for tag in element.select('div.tags a.tag')]
            quotes.append(Quote(text=text, author=author, tags=tags))
        return quotes 