### INF601 - Advanced Programming in Python
### Sokly Hour
### Mini Project 1

import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

# Create 'charts' directory if it doesn't exist
os.makedirs("charts", exist_ok=True)

# Get today's date
today = datetime.now()

# Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=15)

# List of tickers to analyze
myTickers = ["AAPL", "DIS", "GOOG", "NFLX", "MSFT"]

for ticker in myTickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    
    if len(last10days) == 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        
        # Plot the data
        plt.plot(myarray, marker='o')
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")

    else:
        print(f"Insufficient data for 10 days of data. Only available for {len(last10days)} days.")