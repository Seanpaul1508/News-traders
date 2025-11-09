import pandas as pd
import yfinance as yf
from typing import Dict, List
from datetime import datetime, timedelta

class TradingEngine:
    def __init__(self):
        self.portfolio = {}
        self.trading_history = []
    
    def get_stock_data(self, symbol: str, period: str = '1mo') -> pd.DataFrame:
        """Get historical stock data"""
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period=period)
            return hist
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return pd.DataFrame()
    
    def calculate_technical_indicators(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate technical indicators"""
        if data.empty:
            return data
        
        # Simple Moving Average
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        
        # RSI
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        
        return data
    
    def generate_signal(self, symbol: str, news_sentiment: float) -> Dict:
        """Generate trading signal based on news sentiment and technicals"""
        try:
            stock_data = self.get_stock_data(symbol, '3mo')
            if stock_data.empty:
                return {'symbol': symbol, 'signal': 'HOLD', 'confidence': 0}
            
            data_with_indicators = self.calculate_technical_indicators(stock_data)
            latest = data_with_indicators.iloc[-1]
            
            # Simple trading logic
            signal = 'HOLD'
            confidence = 0.5
            
            if news_sentiment > 0.1 and latest['RSI'] < 70:
                signal = 'BUY'
                confidence = min(0.8, (news_sentiment + 0.5) / 2)
            elif news_sentiment < -0.1 and latest['RSI'] > 30:
                signal = 'SELL' 
                confidence = min(0.8, (abs(news_sentiment) + 0.5) / 2)
            
            return {
                'symbol': symbol,
                'signal': signal,
                'confidence': round(confidence, 2),
                'current_price': latest['Close'],
                'sentiment': news_sentiment,
                'rsi': latest['RSI'] if pd.notna(latest['RSI']) else 50
            }
            
        except Exception as e:
            print(f"Error generating signal for {symbol}: {e}")
            return {'symbol': symbol, 'signal': 'HOLD', 'confidence': 0}
