# News-traders
A web application that aggregates financial news and provides real-time trading insights to help investors make informed decisions.
# News Traders 📰➡️📈

[![News Traders CI/CD](https://github.com/Seanpaul1508/News-traders/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Seanpaul1508/News-traders/actions/workflows/python-app.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

AI-powered trading system that analyzes news sentiment to generate trading signals in real-time.

## 🚀 Features

- **Real-time News Analysis**: Monitor financial news from multiple sources
- **Sentiment Scoring**: AI-powered sentiment analysis using NLP
- **Trading Signals**: Generate BUY/SELL/HOLD signals based on news sentiment
- **Technical Indicators**: Combine news sentiment with technical analysis
- **REST API**: Easy integration with trading platforms
- **CI/CD Pipeline**: Automated testing and deployment

## 📊 How It Works

1. **News Collection**: Fetch financial news from Reuters, Bloomberg, and other sources
2. **Sentiment Analysis**: Analyze news content using VADER and TextBlob
3. **Technical Analysis**: Calculate RSI, Moving Averages, and other indicators
4. **Signal Generation**: Combine sentiment and technicals to generate trading signals
5. **API Exposure**: Provide signals via REST API for integration

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Seanpaul1508/News-traders.git
cd News-traders

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
