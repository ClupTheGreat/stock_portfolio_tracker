from data_loader import DataLoader
import mplfinance as mpf
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, symbol, string = None):
        """
        Constructor for the Stock class.

        Parameters:
        - symbol (str): The stock symbol.
        - string (str): Optional parameter for only processing stock price.
        """
        if string is not None:
            self.symbol = symbol
            self.data_loader = DataLoader()
            self.daily_data = self.data_loader.get_stock_data(symbol)
            self.price = float(self.daily_data.tail(1)['Close'])
        elif string is None:
            # Initialize daily, weekly and monthly stock data
            self.symbol = symbol
            self.data_loader = DataLoader()
            self.daily_data = self.data_loader.get_stock_data(symbol)
            self.weekly_data = self.data_loader.get_stock_data_weekly(symbol)
            self.monthly_data = self.data_loader.get_stock_data_monthly(symbol)
            self.price = float(self.daily_data.tail(1)['Close'])
    
    def save_historical(self):
        """
        Save historical stock data to a file.
        """
        stock_historical = self.data_loader.get_stock_data_historical(self.symbol)
        print(stock_historical)
    
    def create_chart_daily(self):
        """
        Create and display a daily candlestick chart.
        """
        mpf.plot(self.daily_data, type = "candle", style="binance")

    def create_chart_weekly(self):
        """
        Create and display a weekly candlestick chart.
        """
        mpf.plot(self.weekly_data, type = "candle", style="binance")

    def create_chart_monthly(self):
        """
        Create and display a monthly candlestick chart.
        """
        mpf.plot(self.monthly_data, type = "candle", style="binance")

