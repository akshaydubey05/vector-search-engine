from typing import List, Tuple
from .indexer import Indexer
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SearchEngine:
    """Main search engine class to process queries and rank documents."""
    
    def __init__(self):
        self.indexer = Indexer()
        logging.info("Search engine initialized")

    def add_document(self, doc_id: int, document: str) -> None:
        """Add a document to the search engine.
        
        Args:
            doc_id: Unique document identifier.
            document: Text content of the document.
        """
        self.indexer.add_document(doc_id, document)

    def search(self, query: str) -> List[Tuple[float, str]]:
        """Search for documents matching the query.
        
        Args:
            query: Search query string.
            
        Returns:
            List of (relevance_score, document_snippet) tuples, sorted by relevance.
        """
        query_concordance = self.indexer.vector_compare.concordance(self.indexer.vector_compare.refine_query(query))
        matches = []
        
        for doc_id, doc_concordance in self.indexer.index.items():
            relevance = self.indexer.vector_compare.relation(query_concordance, doc_concordance)
            if relevance > 0:
                snippet = self.indexer.documents[doc_id][:100]
                matches.append((relevance, snippet))
        
        matches.sort(reverse=True)
        logging.info(f"Search completed for query '{query}': {len(matches)} matches found")
        return matches