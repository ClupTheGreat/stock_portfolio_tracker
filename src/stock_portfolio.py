import yfinance as yf
from data_loader import DataLoader
import stock
import sqlite_commands
import pickle

# stocks_data = stock.Stock("ZOMATO")

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
        #TODO
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
        self.stock_portfolio_value = 0.0
        list_of_qandv = list(self.stocks_owned.values())
        for i in range(0, len(list_of_qandv)):
            quant = list_of_qandv[i]['quantity']
            values = list_of_qandv[i]['purchase_price']
            total_money_value = quant*values
            self.stock_portfolio_value+=total_money_value
        #TODO
        # Calculate total portfolio value
        
        # for stock in self.stocks_owned.items():
            # print(stock)
            # symbol = stock[0]
            # data = self.data_loader.get_stock_data(symbol)
            # print(data['Close'].loc[data.index[0]]) getting price data
            # stock_portfolio_value += data['Close'].loc[data.index[0]]
        # for symbol, stock
        return self.stock_portfolio_value
    
    def holdings_value(self):
        self.stocks_holdings_value = 0.0
        list_of_stocks = list(self.stocks_owned.items())
        list_current_price = []
        for i in list_of_stocks:
            symbol = i[0]
            current_price = sqlite_commands.get_current_prices(symbol)
            list_current_price.append(current_price)
        for j in list_current_price:
            self.stocks_holdings_value+=j
        return self.stocks_holdings_value

        
        
        
    
# portfolio = StockPortfolio()
# portfolio.add_stock(stock.Stock("ZOMATO"), 10, 100)


# Saving and Loading a class
# with open('portfolio.pickle', 'wb') as file:
#     pickle.dump(portfolio, file)

# del portfolio
# try:
#     print(portfolio)
# except:
#     print("deleted")

# with open('portfolio.pickle', 'rb') as file:
#     print("open")
#     loaded_portfolio = pickle.load(file)

# try:
#     print("new",loaded_portfolio)
# except:
#     print("failed")



# stock1 = stock.Stock("WIPRO")
# stock2 = "INFY.NS"
# portfolio1 = StockPortfolio()
# portfolio1.add_stock(stock1,10,421)
# portfolio1.add_stock(stock2,10,1494)
# print(portfolio1.total_portfolio_value())