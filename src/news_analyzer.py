import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import nltk
from textblob import TextBlob

class NewsAnalyzer:
    def __init__(self):
        self.sources = [
            'https://feeds.reuters.com/reuters/businessNews',
            'https://feeds.bloomberg.com/markets/news.rss'
        ]
    
    def fetch_news(self, source: str) -> List[Dict]:
        """Fetch news from RSS feeds"""
        try:
            response = requests.get(source, timeout=10)
            soup = BeautifulSoup(response.content, 'xml')
            
            articles = []
            for item in soup.find_all('item')[:10]:  # Limit to 10 articles
                article = {
                    'title': item.title.text if item.title else '',
                    'description': item.description.text if item.description else '',
                    'pub_date': item.pubDate.text if item.pubDate else '',
                    'link': item.link.text if item.link else ''
                }
                articles.append(article)
            
            return articles
        except Exception as e:
            print(f"Error fetching news from {source}: {e}")
            return []
    
    def analyze_sentiment(self, text: str) -> float:
        """Analyze sentiment of news text"""
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    
    def get_market_news(self) -> pd.DataFrame:
        """Get and analyze all market news"""
        all_articles = []
        
        for source in self.sources:
            articles = self.fetch_news(source)
            for article in articles:
                # Combine title and description for sentiment analysis
                content = f"{article['title']} {article['description']}"
                sentiment = self.analyze_sentiment(content)
                
                article_data = {
                    'title': article['title'],
                    'sentiment': sentiment,
                    'source': source,
                    'pub_date': article['pub_date'],
                    'link': article['link']
                }
                all_articles.append(article_data)
        
        return pd.DataFrame(all_articles)
