### INF601 - Advanced Programming in Python
### Sokly Hour
### Mini Project 1

import copy
import yfinance as yf # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from pathlib import Path

mytickers = ["MSFT", "IBM", "GOOG", "META", "AMZN"]

try:
    Path("charts").mkdir()
except FileExistsError:
    pass

for ticker in mytickers:
    myticker = yf.Ticker(ticker)
    history = myticker.history(period="max").tail(10)

    closingList = []

    for price in history['Close']:
        closingList.append(price)

    lowprice = copy.copy(closingList)
    lowprice.sort()

    low_price = lowprice[0]
    high_price = lowprice[-1]

    myarray = np.array(closingList)
    plt.plot(myarray)
    plt.xlabel("Days Ago")
    plt.ylabel("Closing Price")
    plt.title(f"{ticker} last 10 Closing Prices")
    plt.axis((1, 10, low_price-2, high_price+2))

    plt.savefig(f"charts/{ticker}.png")

    plt.show()