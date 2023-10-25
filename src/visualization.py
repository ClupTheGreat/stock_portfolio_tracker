import sys
from strategy_tester import *
from sqlite_commands import *
from stock_portfolio import *
from stock import *
from data_loader import *
import talib as ta
import matplotlib.pyplot as plt

def sma_visualization(data):
    data['SMA_100'] = ta.SMA(data['Close'], 100)
    plt.plot(data['Close'])
    plt.plot(data['SMA_100'])
    plt.show()

def macd_visualization(data):
    macd, macd_signal, macd_hist = ta.MACD(data['Close'])

    fig, axs = plt.subplots(2, 1, gridspec_kw={"height_ratios": [3,1]}, figsize = (10,6))
    axs[0].plot(data['Close'])
    axs[1].plot(macd,'b-')
    axs[1].plot(macd_signal,'--', color="orange")
    axs[1].bar(macd_hist.index, macd_hist)

    plt.show()

def rsi_visualization(data):
    data['RSI'] = ta.RSI(data['Close'])
    fig, axs = plt.subplots(2, 1, gridspec_kw={"height_ratios": [3,1]}, figsize = (10,6))

    axs[0].plot(data['Close'])
    axs[1].axhline(y=70, color="r", linestyle="--")
    axs[1].axhline(y=30, color="g", linestyle="--")
    axs[1].plot(data['RSI'], color="orange")

    plt.show()

    


# fig, axs = plt.subplots(2, 1, gridspec_kw={"highest_ratios": [3,1]}, figsize = (10,6))

#     axs[0].plot(data['Close'])
#     axs[1].axhline(y-70, color="r", linestyle="--")
#     axs[1].axhline(y-30, color="g", linestyle="--")
#     axs[1].plot(data['RSI'], color="orange")
