import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from typing import Dict

class SentimentAnalyzer:
    def __init__(self):
        try:
            nltk.download('vader_lexicon', quiet=True)
            self.sia = SentimentIntensityAnalyzer()
        except:
            self.sia = None
    
    def analyze_vader(self, text: str) -> Dict:
        """Analyze sentiment using VADER"""
        if self.sia:
            scores = self.sia.polarity_scores(text)
            return scores
        return {'compound': 0, 'pos': 0, 'neg': 0, 'neu': 1}
    
    def analyze_textblob(self, text: str) -> Dict:
        """Analyze sentiment using TextBlob"""
        analysis = TextBlob(text)
        return {
            'polarity': analysis.sentiment.polarity,
            'subjectivity': analysis.sentiment.subjectivity
        }
    
    def get_combined_sentiment(self, text: str) -> float:
        """Get combined sentiment score from multiple analyzers"""
        vader_scores = self.analyze_vader(text)
        textblob_scores = self.analyze_textblob(text)
        
        # Weighted combination
        vader_weight = 0.6
        textblob_weight = 0.4
        
        combined = (vader_scores['compound'] * vader_weight + 
                   textblob_scores['polarity'] * textblob_weight)
        
        return combined
