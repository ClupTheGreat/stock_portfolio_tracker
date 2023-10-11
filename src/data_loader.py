#Loading data using yfinance

import yfinance as yf
import pandas as pd
import os

# from pandas_datareader import data as pdr
#downloading dataframe
# yf.pdr_override()
class DataLoader:
    def get_stock_data(self, symbol):
        ticker = yf.download(symbol, period = '1d' , interval='1m')
        return ticker.tail(1)

    def get_stock_data_historical(self, symbol):
        ticker = yf.download(symbol)
        save_path = os.path.join("data", f"{symbol}_historical_data.csv")
        ticker.to_csv(save_path)
        print(f"Data saved to {save_path}")
        return ticker
# Example:
# loadstock = DataLoader()
# stock_name = "WIPRO.NS"
# a = loadstock.get_stock_data(stock_name)
# print(a)

