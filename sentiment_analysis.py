from textblob import TextBlob
from typing import Dict

class SentimentAnalyzer:
    def __init__(self):
        pass
    
    def analyze_sentiment(self, text: str) -> Dict:
        """Analyze sentiment of text using TextBlob"""
        try:
            analysis = TextBlob(text)
            sentiment_value = 'positive' if analysis.sentiment.polarity > 0 else ('negative' if analysis.sentiment.polarity < 0 else 'neutral')
            return {
                'polarity': analysis.sentiment.polarity,
                'subjectivity': analysis.sentiment.subjectivity,
                'sentiment': sentiment_value
            }
        except Exception as e:
            return {'polarity': 0, 'subjectivity': 0, 'sentiment': 'neutral', 'error': str(e)}