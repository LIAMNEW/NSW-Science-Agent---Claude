"""
Textbook Manager - Dynamic fetching and recommendation system for OpenStax textbooks
"""

import requests
from typing import Dict, List, Any
from datetime import datetime
from src.data.openstax_catalog import (
    get_textbooks_for_topic,
    format_textbook_recommendation,
    OPENSTAX_TEXTBOOKS
)


class TextbookManager:
    def __init__(self):
        self.catalog = OPENSTAX_TEXTBOOKS
        self.last_update = datetime.now()
    
    def search_textbooks(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for relevant textbooks based on query
        Returns formatted textbook recommendations
        """
        recommendations = get_textbooks_for_topic(query)
        return [format_textbook_recommendation(rec) for rec in recommendations]
    
    def get_textbook_for_nesa_outcome(self, outcome_code: str) -> List[Dict[str, Any]]:
        """
        Get textbook recommendations for specific NESA outcome code
        e.g., SC4-FRC-01 returns Physics textbooks about forces
        """
        from src.data.openstax_catalog import NSW_TOPIC_MAPPINGS
        
        if outcome_code in NSW_TOPIC_MAPPINGS:
            mapping = NSW_TOPIC_MAPPINGS[outcome_code]
            topic_name = mapping['nesa_name']
            return self.search_textbooks(topic_name)
        return []
    
    def get_all_science_textbooks(self) -> List[Dict[str, Any]]:
        """Get complete list of available science textbooks"""
        textbooks = []
        for book_key, book_data in self.catalog.items():
            textbooks.append({
                'id': book_key,
                'title': book_data['title'],
                'description': book_data['description'],
                'url': book_data['url'],
                'pdf_url': book_data['pdf_url'],
                'subjects': book_data['subjects'],
                'license': book_data['license']
            })
        return textbooks
    
    def update_catalog(self):
        """
        Fetch latest textbook information from OpenStax
        This function can be enhanced to scrape OpenStax website for new books
        """
        try:
            # For now, we use the static catalog
            # In future, this could scrape openstax.org/subjects for new books
            self.last_update = datetime.now()
            print(f"Textbook catalog updated at {self.last_update}")
            return True
        except Exception as e:
            print(f"Error updating textbook catalog: {e}")
            return False
    
    def get_catalog_info(self) -> Dict[str, Any]:
        """Get information about the textbook catalog"""
        return {
            'total_textbooks': len(self.catalog),
            'last_updated': self.last_update.isoformat(),
            'textbook_titles': [book['title'] for book in self.catalog.values()],
            'subjects_covered': list(set(
                subject 
                for book in self.catalog.values() 
                for subject in book['subjects']
            ))
        }


# Global instance
_textbook_manager = None

def get_textbook_manager() -> TextbookManager:
    """Get singleton instance of TextbookManager"""
    global _textbook_manager
    if _textbook_manager is None:
        _textbook_manager = TextbookManager()
    return _textbook_manager
