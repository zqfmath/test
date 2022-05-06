import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

pd.set_option('display.max_columns', None)

ticker=input("Enter the ticker: ")
length_window=10

def animate(i):
    global ticker
    global period
    data = yf.download(tickers=ticker, period="1d", interval="1m")
    prices=(data['Open']+data['Close'])/2
    volumes=data['Volume']/1000
    ave_prices=prices.copy()
    for index in range(len(prices)):
        if index<length_window:
            left=0
            right=index+1
        else:
            left=index+1-length_window
            right=index+1
        ave_prices[index]=sum(prices[left:right]*volumes[left:right])/sum(volumes[left:right])
    plt.cla()
    plt.plot(prices)
    plt.plot(ave_prices)
    plt.grid()
    plt.tight_layout()

ani = FuncAnimation(fig=plt.gcf(), func=animate, interval=1000*30,fargs=[])

plt.tight_layout()
plt.show()