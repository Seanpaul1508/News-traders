import yfinance as yf
import pandas as pd
from typing import Dict

class TradingEngine:
    def __init__(self):
        pass
    
    def get_stock_data(self, symbol: str) -> pd.DataFrame:
        """Get stock data using yfinance"""
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="1mo")
            return hist
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return pd.DataFrame()
    
    def generate_signal(self, symbol: str, sentiment_score: float) -> Dict:
        """Generate trading signal based on sentiment"""
        try:
            data = self.get_stock_data(symbol)
            if data.empty:
                return {'symbol': symbol, 'signal': 'HOLD', 'confidence': 0, 'error': 'No data'}
            
            current_price = data['Close'].iloc[-1]
            
            # Simple signal logic based on sentiment
            if sentiment_score > 0.1:
                signal = 'BUY'
                confidence = min(0.9, sentiment_score + 0.3)
            elif sentiment_score < -0.1:
                signal = 'SELL'
                confidence = min(0.9, abs(sentiment_score) + 0.3)
            else:
                signal = 'HOLD'
                confidence = 0.5
            
            return {
                'symbol': symbol,
                'signal': signal,
                'confidence': round(confidence, 2),
                'current_price': round(current_price, 2),
                'sentiment_score': round(sentiment_score, 2)
            }
        except Exception as e:
            return {'symbol': symbol, 'signal': 'HOLD', 'confidence': 0, 'error': str(e)}
