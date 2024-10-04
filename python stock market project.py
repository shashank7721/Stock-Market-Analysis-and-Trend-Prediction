import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


ticker = 'TATAMOTORS.NS'
data = yf.download(ticker, start='2020-01-01', end='2024-06-06')


data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()
data['SMA20'] = data['Close'].rolling(window=20).mean()


plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA50'], label='50-day SMA', color='orange')
plt.plot(data['SMA200'], label='200-day SMA', color='purple')
plt.plot(data['SMA20'], label= '20-day SMA', color='green')
plt.title(f'{ticker} Price and Moving Averages')
plt.legend()
plt.show()
