from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
import talib as ta
from stock import Stock
import pandas as pd
import matplotlib.pyplot as plt

"""
Deprecated
"""



def RSIcalc(stock):
    df = stock.daily_data.copy()
    df['MA200'] = df['Adj Close'].rolling(window=200).mean()
    df['price change'] = df ['Adj Close'].pct_change()
    df['Upmove'] = df['price change'].apply(lambda x: x if x > 0 else 0)
    df['Downmove'] = df['price change'].apply(lambda x: abs(x) if x < 0 else 0)
    df['avg Up'] = df['Upmove'].ewm(span=19).mean()
    df['avg Down'] = df['Downmove'].ewm(span=19).mean()
    df = df.dropna()
    df['RS'] = df['avg Up']/df['avg Down']
    df['RSI'] = df['RS'].apply(lambda x: 100-(100/(x+1)))
    df.loc[(df['Adj Close'] > df['MA200']) & (df['RSI']<30), 'Buy'] = 'Yes'
    df.loc[(df['Adj Close'] < df['MA200']) | (df['RSI']>30), 'Buy'] = 'No'
    return df

def getSignals(df):
    Buying_dates = []
    Selling_dates = []
    for i in range(len(df)):
        if "Yes" in df['Buy'].iloc[i]:
            Buying_dates.append(df.iloc[i+1].name)
            for j in range(1,11):
                if df['RSI'].iloc[i + j] > 40:
                    Selling_dates.append(df.iloc[i+j+1].name)
                    break
                elif j == 10:
                    Selling_dates.append(df.iloc[i+j+1].name)
    return Buying_dates, Selling_dates

def runTest(stock):
    frame = RSIcalc(stock)
    buy, sell = getSignals(frame)
    plt.figure(figsize=(12,5))
    plt.scatter(frame.loc[buy].index, frame.loc[buy]['Adj Close'], marker='^', c='g')
    plt.plot(frame['Adj Close'], alpha=0.7)
    plt.show()