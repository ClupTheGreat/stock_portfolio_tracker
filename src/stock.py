import sys
from data_loader import DataLoader
from datetime import timedelta
import sqlite_commands
import time
import mplfinance as mpf

stock_names_list = []

# sys.getsizeof(object)
class Stock:
    def __init__(self, symbol, string = None):
        if string is not None:
            self.symbol = symbol
            self.data_loader = DataLoader()
            self.daily_data = self.data_loader.get_stock_data(symbol)
            self.price = float(self.daily_data.tail(1)['Close'])
        elif string is None:
            print("no stirng")
            self.symbol = symbol
            self.data_loader = DataLoader()
            self.daily_data = self.data_loader.get_stock_data(symbol)
            self.weekly_data = self.data_loader.get_stock_data_weekly(symbol)
            self.monthly_data = self.data_loader.get_stock_data_monthly(symbol)
            self.price = float(self.daily_data.tail(1)['Close'])
    
        
    # def get_data(self, time_period):
    #     self.time_period = time_period
    #     stock_data = self.data_loader.get_stock_data(self.symbol, self.time_period)
    #     return stock_data
        # print(stock_data)
    
    def save_historical(self):
        stock_historical = self.data_loader.get_stock_data_historical(self.symbol)
        print(stock_historical)
    
    def create_chart_daily(self):
        mpf.plot(self.daily_data, type = "candle", style="yahoo")

    def create_chart_weekly(self):
        mpf.plot(self.weekly_data, type = "candle", style="yahoo")

    def create_chart_monthly(self):
        mpf.plot(self.monthly_data, type = "candle", style="yahoo")


# start = time.time()
# stock1 = Stock("ZOMATO")
# stock2 = Stock("TCS")
# stock3 = Stock("INFY")
# stock4 = Stock("HDFCBANK")
# stock5 = Stock("LICI")
# end = time.time()
# stock1.create_chart_daily()
# stock1.create_chart_weekly()
# stock1.create_chart_monthly()
# print(end - start)
# stock1 = Stock('ZOMATO')
# print(stock1.symbol)
