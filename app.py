from flask import Flask, jsonify, request
from src.news_analyzer import NewsAnalyzer
from src.trading_engine import TradingEngine
from src.sentiment_analysis import SentimentAnalyzer

app = Flask(__name__)
news_analyzer = NewsAnalyzer()
trading_engine = TradingEngine()
sentiment_analyzer = SentimentAnalyzer()

@app.route('/')
def home():
    return jsonify({
        "message": "News Traders API",
        "version": "1.0.0",
        "endpoints": {
            "news": "/api/news",
            "analyze": "/api/analyze/<symbol>",
            "health": "/health"
        }
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "news-traders"})

@app.route('/api/news')
def get_news():
    """Get latest market news with sentiment analysis"""
    try:
        news_df = news_analyzer.get_market_news()
        return jsonify({
            "news_count": len(news_df),
            "articles": news_df.to_dict('records')
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze/<symbol>')
def analyze_stock(symbol):
    """Analyze trading signal for a stock"""
    try:
        # Get recent news and calculate average sentiment
        news_df = news_analyzer.get_market_news()
        avg_sentiment = news_df['sentiment'].mean() if not news_df.empty else 0
        
        # Generate trading signal
        signal = trading_engine.generate_signal(symbol.upper(), avg_sentiment)
        
        return jsonify({
            "symbol": symbol.upper(),
            "analysis": signal,
            "news_analyzed": len(news_df),
            "average_sentiment": avg_sentiment
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
