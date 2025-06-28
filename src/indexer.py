from typing import Dict, List
from .vector_compare import VectorCompare
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Indexer:
    """Class to manage document indexing for the search engine."""
    
    def __init__(self):
        self.vector_compare = VectorCompare()
        self.index: Dict[int, Dict[str, int]] = {}
        self.documents: Dict[int, str] = {}
        logging.info("Indexer initialized")

    def add_document(self, doc_id: int, document: str) -> None:
        """Add a document to the index.
        
        Args:
            doc_id: Unique identifier for the document.
            document: Text content of the document.
        """
        self.documents[doc_id] = document
        self.index[doc_id] = self.vector_compare.concordance(document.lower())
        logging.info(f"Document {doc_id} added to index")