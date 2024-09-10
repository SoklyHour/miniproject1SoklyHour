### INF601 - Advanced Programming in Python
### Sokly Hour
### Mini Project 1

import yfinance as yf # type: ignore
from pprint import pprint

mytickers = ["MSFT", "AAPL", "", "",]

msft = yf.Ticker("MSFT")

# get all stock info
# print(msft.info)
pprint(msft.info)

# get historical market data
hist = msft.history(period="1mo")
last_10_days = hist.tail(10)
pprint(last_10_days)