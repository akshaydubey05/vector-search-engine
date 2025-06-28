import math
from typing import Dict
import logging
from sklearn.linear_model import LinearRegression
from transformers import pipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VectorCompare:
    """Class to compute vector space similarity between documents and queries with NLP refinement."""
    
    def __init__(self):
        self.model = LinearRegression()
        self._train_model()
        self.nlp = pipeline("fill-mask", model="distilbert-base-uncased", tokenizer="distilbert-base-uncased")
        logging.info("NLP model initialized for query refinement")

    def _train_model(self):
        """Train the linear regression model with dummy data."""
        X = [[0.1], [0.3], [0.5], [0.7]]
        y = [0.2, 0.4, 0.6, 0.8]
        self.model.fit(X, y)
        logging.info("ML model trained for relevance scoring")

    def refine_query(self, query: str) -> str:
        """Refine query with synonyms and corrections using NLP.
        
        Args:
            query: Input query string.
            
        Returns:
            Refined query string.
        """
        refined = query.lower()
        words = refined.split()
        for i, word in enumerate(words):
            if len(word) > 3:
                masked = refined.replace(word, "[MASK]")
                predictions = self.nlp(masked)
                if predictions:
                    synonym = next((p['token_str'] for p in predictions if p['score'] > 0.1), word)
                    words[i] = synonym
        return " ".join(words)

    def magnitude(self, concordance: Dict[str, int]) -> float:
        """Calculate the magnitude of a concordance vector.
        
        Args:
            concordance: Dictionary of word frequencies.
            
        Returns:
            Magnitude of the vector.
            
        Raises:
            ValueError: If input is not a dictionary.
        """
        if not isinstance(concordance, dict):
            logging.error("Concordance must be a dictionary")
            raise ValueError("Concordance must be a dictionary")
        
        total = sum(count ** 2 for count in concordance.values())
        return math.sqrt(total)

    def relation(self, concordance1: Dict[str, int], concordance2: Dict[str, int]) -> float:
        """Compute cosine similarity enhanced with ML prediction.
        
        Args:
            concordance1: First concordance (e.g., query).
            concordance2: Second concordance (e.g., document).
            
        Returns:
            Enhanced relevance score (0 to 1).
            
        Raises:
            ValueError: If inputs are not dictionaries.
        """
        if not isinstance(concordance1, dict) or not isinstance(concordance2, dict):
            logging.error("Both inputs must be dictionaries")
            raise ValueError("Both inputs must be dictionaries")
        
        topvalue = sum(count * concordance2.get(word, 0) for word, count in concordance1.items())
        magnitude_product = self.magnitude(concordance1) * self.magnitude(concordance2)
        cosine_score = 0.0 if magnitude_product == 0 else topvalue / magnitude_product
        ml_score = self.model.predict([[cosine_score]])[0]
        return min(max(ml_score, 0.0), 1.0)

    def concordance(self, document: str) -> Dict[str, int]:
        """Generate a concordance (word frequency dictionary) from a document.
        
        Args:
            document: Input string document.
            
        Returns:
            Dictionary mapping words to their frequency.
            
        Raises:
            ValueError: If input is not a string.
        """
        if not isinstance(document, str):
            logging.error("Input document must be a string")
            raise ValueError("Input document must be a string")
        
        con = {}
        for word in document.lower().split():
            con[word] = con.get(word, 0) + 1
        logging.debug(f"Concordance generated for document: {len(con)} unique words")
        return con