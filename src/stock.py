import sys
from data_loader import DataLoader
from datetime import timedelta
import sqlite_commands

stock_names_list = []

# sys.getsizeof(object)
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data_loader = DataLoader()
        self.price = sqlite_commands.get_current_prices(symbol)

    def get_data(self, time_period):
        self.time_period = time_period
        stock_data = self.data_loader.get_stock_data(self.symbol, self.time_period)
        return stock_data
        # print(stock_data)
    
    def save_historical(self):
        stock_historical = self.data_loader.get_stock_data_historical(self.symbol)
        print(stock_historical)


        


# stock1 = Stock('ZOMATO')
# print(stock1.symbol)
