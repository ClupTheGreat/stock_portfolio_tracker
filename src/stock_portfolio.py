import yfinance as yf
from data_loader import DataLoader
import stock
import sqlite_commands

stocks_data = stock.Stock("ZOMATO")

class StockPortfolio:
    def __init__(self):
        #initialize empty portfolio
        self.stocks_owned = {}
        self.data_loader = DataLoader()
    
    def add_stock(self, stocks_data, quantity, purchase_price):
        #Add stock to portfolio
        if stocks_data.symbol not in self.stocks_owned:
            self.stocks_owned[stocks_data.symbol] = {'quantity' : quantity, 'purchase_price' : purchase_price}
        else:
            # Adds the stock quantity and averages the price
            self.stocks_owned[stocks_data.symbol]['quantity'] += quantity
            self.stocks_owned[stocks_data.symbol]['purchase_price'] += (self.stocks_owned[stocks_data.symbol]['purchase_price']+purchase_price)/2
        
    def remove_stock(self, stocks, quantity):
        #FIX
        #Remove stock from portfolio
        if stocks.symbol in self.stocks:
            if quantity == self.stocks_owned['quantity']:
                del self.stocks_owned[stocks.symbol]
            elif quantity <= self.stocks_owned['quantity']:
                self.stocks_owned['quantity'] -= quantity
            elif quantity > 0:
                print ("Wrong amout")
            else:
                print ("You cant sell stocks more than what you own")
        else:
            print("Enter a valid stock to remove")
    
    def total_portfolio_value(self):
        #FIX
        # Calculate total portfolio value
        stock_portfolio_value = 0.0
        for stock in self.stocks_owned.items():
            # print(stock)
            symbol = stock[0]
            data = self.data_loader.get_stock_data(symbol)
            # print(data['Close'].loc[data.index[0]]) getting price data
            stock_portfolio_value += data['Close'].loc[data.index[0]]
        # for symbol, stock
        return stock_portfolio_value
        
stock1 = "WIPRO.NS"
stock2 = "INFY.NS"
portfolio1 = StockPortfolio()
portfolio1.add_stock(stock1,10,421)
portfolio1.add_stock(stock2,10,1494)
print(portfolio1.total_portfolio_value())
    