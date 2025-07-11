from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Quote:
    """Data model for a quote scraped from the website, with a unique id."""
    text: str
    author: str
    tags: List[str]
    id: Optional[int] = field(default=None) 