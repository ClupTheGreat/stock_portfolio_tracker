#Loading data using yfinance

import yfinance as yf
import pandas as pd
import os

# from pandas_datareader import data as pdr
#downloading dataframe
# yf.pdr_override()
class DataLoader:
    def get_stock_data(self, symbol):
        ticker = yf.download(symbol+".NS", interval='1d', period='3y')
        return ticker
        # return ticker.tail(1)

    def get_stock_data_weekly(self, symbol):
        ticker = yf.download(symbol+".NS", interval='1wk', period='10y')
        return ticker
    
    def get_stock_data_monthly(self, symbol):
        ticker = yf.download(symbol+".NS", interval='1mo', period='15y')
        return ticker

    def get_stock_data_historical(self, symbol):
        ticker = yf.Ticker(symbol+".NS")
        save_path = os.path.join("data", f"{symbol}_historical_data.csv")
        ticker.history(period="max").to_csv(save_path)
        print(f"Data saved to {save_path}")
        return ticker
# Example:
# loadstock = DataLoader()
# stock_name = "WIPRO.NS"
# a = loadstock.get_stock_data(stock_name)
# print(a)

