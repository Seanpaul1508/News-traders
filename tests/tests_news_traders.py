import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestBasicImports(unittest.TestCase):
    
    def test_imports(self):
        """Test that core modules can be imported"""
        try:
            from src.news_analyzer import NewsAnalyzer
            from src.sentiment_analysis import SentimentAnalyzer
            from src.trading_engine import TradingEngine
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Import failed: {e}")

if __name__ == '__main__':
    unittest.main()
