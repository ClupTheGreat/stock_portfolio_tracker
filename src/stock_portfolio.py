import yfinance as yf
from data_loader import DataLoader
import stock
import sqlite_commands
import pickle

class StockPortfolio:
    def __init__(self):
        """
        Initialize an empty stock portfolio
        """
        self.stocks_owned = {}
        self.data_loader = DataLoader()
    
    def add_stock(self, stocks_data, quantity, purchase_price):
        """
        Add or update a stock in the portfolio

        Parameters:
        - stocks_data (Stock): Pass a Stock object
        - quantity (int) : Quantity of stock to add
        - purchase_price (float) : Purchase price per stock
        """
        if stocks_data.symbol not in self.stocks_owned:
            # Add a new stock to the portfolio
            self.stocks_owned[stocks_data.symbol] = {'quantity' : quantity, 'purchase_price' : purchase_price}
        else:
            # Update existing stock's quantity and purchase price
            self.stocks_owned[stocks_data.symbol]['quantity'] = int(quantity) + int(self.stocks_owned[stocks_data.symbol]['quantity'])
            self.stocks_owned[stocks_data.symbol]['purchase_price'] = (float((self.stocks_owned[stocks_data.symbol]['purchase_price']+float(purchase_price)))/2)
        
    def remove_stock(self, stocks, quantity):
        """
        Remove a specified quantity of stocks from the portfolio

        Parameters:
        - stocks (str): Stock symbol.
        - quantity (int): Quantity of stocks to remove
        """
        if stocks in self.stocks_owned:
            if quantity == self.stocks_owned[stocks]['quantity']:
                del self.stocks_owned[stocks]
            elif int(quantity) <= int(self.stocks_owned[stocks]['quantity']):
                self.stocks_owned[stocks]['quantity'] = int(self.stocks_owned[stocks]['quantity']) - int(quantity)
            elif quantity > 0:
                print ("Wrong amount")
            else:
                print ("You cant sell stocks more than what you own")
        else:
            print("Enter a valid stock to remove")

        # Remove the stock if it's quantity == 0
        if stocks in self.stocks_owned:
            if self.stocks_owned[stocks]['quantity'] == 0:
                del self.stocks_owned[stocks]
    
    def total_portfolio_value(self):
        """
        Calculates the total stock portfolio value

        Returns:
        - float: Total portfolio value.
        """
        self.stock_portfolio_value = 0.0
        list_of_qandv = list(self.stocks_owned.values())
        for i in range(0, len(list_of_qandv)):
            quant = float(list_of_qandv[i]['quantity'])
            values = float(list_of_qandv[i]['purchase_price'])
            
            total_money_value = quant*values
            self.stock_portfolio_value+=total_money_value
        return self.stock_portfolio_value
    
    def holdings_value(self):
        """
        Calculates the current holdings portfolio value

        Returns:
        - float: Current holdings value.
        """
        self.stocks_holdings_value = 0.0
        list_of_stocks = list(self.stocks_owned.items())
        list_current_price = []
        for i in list_of_stocks:
            symbol = i[0]
            get_price = stock.Stock(symbol,"")
            current_price = get_price.price
            list_current_price.append(current_price*float(i[1]["quantity"]))
        for j in list_current_price:
            self.stocks_holdings_value+=j
        return self.stocks_holdings_value