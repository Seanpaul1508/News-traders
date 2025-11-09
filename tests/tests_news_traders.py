import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.news_analyzer import NewsAnalyzer
from src.trading_engine import TradingEngine
from src.sentiment_analysis import SentimentAnalyzer

class TestNewsTraders(unittest.TestCase):
    
    def test_sentiment_analyzer(self):
        """Test sentiment analysis functionality"""
        analyzer = SentimentAnalyzer()
        
        # Test positive sentiment
        positive_score = analyzer.get_combined_sentiment("Great earnings report and strong growth!")
        self.assertIsInstance(positive_score, float)
        
        # Test negative sentiment  
        negative_score = analyzer.get_combined_sentiment("Terrible losses and declining revenue")
        self.assertIsInstance(negative_score, float)
    
    def test_trading_engine(self):
        """Test trading engine functionality"""
        engine = TradingEngine()
        
        # Test data fetching
        data = engine.get_stock_data('AAPL', '1mo')
        self.assertIsInstance(data, pd.DataFrame)
    
    def test_news_analyzer(self):
        """Test news analyzer initialization"""
        analyzer = NewsAnalyzer()
        self.assertEqual(len(analyzer.sources), 2)

if __name__ == '__main__':
    unittest.main()
