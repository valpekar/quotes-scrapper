import json
from typing import List
from models.quote import Quote

class JsonStorage:
    """Handles saving quotes to a JSON file."""
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_quotes(self, quotes: List[Quote]):
        """Save a list of Quote objects to a JSON file. If a quote exists (by text), replace it; otherwise, add it."""
        from dataclasses import asdict
        import os
        # Load existing quotes if file exists
        existing_quotes = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                try:
                    existing_quotes = json.load(f)
                except json.JSONDecodeError:
                    existing_quotes = []
        # Build a dict for fast lookup by text and track ids
        quote_dict = {q['text']: q for q in existing_quotes if 'text' in q}
        used_ids = {q.get('id') for q in existing_quotes if 'id' in q and isinstance(q['id'], int)}
        next_id = max(used_ids) + 1 if used_ids else 1
        # Update or add new quotes, assigning ids
        for q in quotes:
            q_dict = asdict(q)
            if q.text in quote_dict and 'id' in quote_dict[q.text]:
                q_dict['id'] = quote_dict[q.text]['id']
            else:
                q_dict['id'] = next_id
                next_id += 1
            quote_dict[q.text] = q_dict
        # Save back to file
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(list(quote_dict.values()), f, ensure_ascii=False, indent=2) 