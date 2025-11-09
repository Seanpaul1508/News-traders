from flask import Flask, jsonify
from src.news_analyzer import NewsAnalyzer
from src.sentiment_analysis import SentimentAnalyzer
from src.trading_engine import TradingEngine

app = Flask(__name__)
news_analyzer = NewsAnalyzer()
sentiment_analyzer = SentimentAnalyzer()
trading_engine = TradingEngine()

@app.route('/')
def home():
    return jsonify({
        "message": "News Traders API - Live",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "/health": "System health check",
            "/api/news": "Get market news",
            "/api/analyze/<symbol>": "Analyze stock with sentiment"
        }
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "news-traders",
        "timestamp": "2024-01-01T00:00:00Z"
    })

@app.route('/api/news')
def get_news():
    """Get latest market news"""
    try:
        news_df = news_analyzer.analyze_news()
        
        # Add sentiment analysis to news
        articles_with_sentiment = []
        for _, article in news_df.iterrows():
            text = f"{article['title']} {article['description']}"
            sentiment = sentiment_analyzer.analyze_sentiment(text)
            
            article_data = article.to_dict()
            article_data.update(sentiment)
            articles_with_sentiment.append(article_data)
        
        return jsonify({
            "status": "success",
            "articles_count": len(articles_with_sentiment),
            "articles": articles_with_sentiment
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/analyze/<symbol>')
def analyze_stock(symbol):
    """Analyze stock with news sentiment"""
    try:
        # Get news and calculate average sentiment
        news_df = news_analyzer.analyze_news()
        
        if news_df.empty:
            avg_sentiment = 0
        else:
            sentiments = []
            for _, article in news_df.iterrows():
                text = f"{article['title']} {article['description']}"
                sentiment = sentiment_analyzer.analyze_sentiment(text)
                sentiments.append(sentiment['polarity'])
            avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        
        # Generate trading signal
        signal = trading_engine.generate_signal(symbol.upper(), avg_sentiment)
        
        return jsonify({
            "status": "success",
            "symbol": symbol.upper(),
            "analysis": signal,
            "news_analyzed": len(news_df),
            "average_sentiment": round(avg_sentiment, 3)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
