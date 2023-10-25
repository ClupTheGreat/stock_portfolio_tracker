import yfinance as yf
import pandas as pd
import os

class DataLoader:
    """
    Download daily, weekly, monthly and all historical data using the given symbol.

    Parameters:
    -symbol (str): The stock symbol.

    Returns:
    -pandas.DatafFrame: the specific time period's stock data
    """
    def get_stock_data(self, symbol):
        ticker = yf.download(symbol+".NS", interval='1d', period='2y')
        return ticker

    def get_stock_data_weekly(self, symbol):
        ticker = yf.download(symbol+".NS", interval='1wk', period='5y')
        return ticker
    
    def get_stock_data_monthly(self, symbol):
        ticker = yf.download(symbol+".NS", interval='1mo', period='10y')
        return ticker

    def get_stock_data_historical(self, symbol):
        ticker = yf.Ticker(symbol+".NS")
        save_path = os.path.join("data", f"{symbol}_historical_data.csv")
        ticker.history(period="max").to_csv(save_path)
        print(f"Data saved to {save_path}")
        return ticker

