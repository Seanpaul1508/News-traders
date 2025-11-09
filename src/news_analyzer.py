import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time

class NewsAnalyzer:
    def __init__(self):
        self.sources = [
            'https://feeds.reuters.com/reuters/businessNews',
            'https://feeds.bloomberg.com/markets/news.rss'
        ]
    
    def fetch_news(self) -> List[Dict]:
        """Fetch news from RSS feeds"""
        articles = []
        for source in self.sources:
            try:
                response = requests.get(source, timeout=10)
                soup = BeautifulSoup(response.content, 'xml')
                
                for item in soup.find_all('item')[:5]:
                    article = {
                        'title': item.title.text if item.title else 'No title',
                        'description': item.description.text if item.description else 'No description',
                        'pub_date': item.pubDate.text if item.pubDate else 'No date',
                        'link': item.link.text if item.link else 'No link',
                        'source': source
                    }
                    articles.append(article)
            except Exception as e:
                print(f"Error fetching from {source}: {e}")
        
        return articles
    
    def analyze_news(self) -> pd.DataFrame:
        """Analyze fetched news"""
        articles = self.fetch_news()
        return pd.DataFrame(articles)
