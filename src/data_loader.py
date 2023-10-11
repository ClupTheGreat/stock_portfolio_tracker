#Loading data using yfinance

import yfinance as yf
import pandas as pd
import os

# from pandas_datareader import data as pdr
#downloading dataframe
# yf.pdr_override()
class DataLoader:
    def get_stock_data(self, tick):
        ticker = yf.download(tick)
        save_path = os.path.join("data", f"{tick}_historical_data.csv")
        ticker.to_csv(save_path)
        print(f"Data saved to {save_path}")
        return ticker

# Example:
# loadstock = DataLoader()
# stock_name = "WIPRO.NS"
# loadstock.get_stock_data(stock_name)

