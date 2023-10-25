from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from ui1 import Ui_MainWindow
import sys
from strategy_tester import *
from sqlite_commands import *
from stock_portfolio import *
from stock import *
from data_loader import *

#Creating a portfolio and saving function
def load_portfolio():
    if os.path.exists("saved_portfolio.pickle"):
        with open("saved_portfolio.pickle", "rb") as file:
            portfolio = pickle.load(file)
            print("Existing portfolio loaded.")
    else:
        portfolio = StockPortfolio()
        print("New portfolio created.")
    
    return portfolio

def save_portfolio(portfolio):
    with open("saved_portfolio.pickle", "wb") as file:
        pickle.dump(portfolio, file)
        print("Portfolio saved.")

def delete_portfolio():
    if os.path.exists("saved_portfolio.pickle"):
        os.remove("saved_portfolio.pickle")
        print("Portfolio deleted.")
    else:
        print("No portfolio found.")

portfolio = load_portfolio()
# delete_portfolio()
# Test adding stocks
# portfolio.add_stock(Stock("ZOMATO"), 12, 100)
# portfolio.add_stock(Stock("TCS"), 12, 100)

#Creates a list of all owned stocks by the portfolio

# for i in portfolio.stocks_owned.items():
#     list_of_owned_stocks.append(i[0]+"@"+str(f"{i[1]['purchase_price']:.2f}")+" - Quantity: "+str(i[1]['quantity']))
#     print(i)
def loading_stocks():
    list_of_owned_stocks = []
    for i in portfolio.stocks_owned.items():
        print(portfolio.stocks_owned)
        stock_name = i[0]
        purchase_price = i[1]['purchase_price']
        # Convert purchase_price to float if it's a string
        if isinstance(purchase_price, str):
            purchase_price = float(purchase_price)

        formatted_price = f"{purchase_price:.2f}"
        
        stock_info = f"{stock_name}@{formatted_price} - Quantity: {i[1]['quantity']}"
        list_of_owned_stocks.append(stock_info)
        print(i)
    return list_of_owned_stocks

def global_all_stocks():
    stocks = list(sqlite_commands.list_of_stocks())
    clean_stocks = []
    for i in stocks:
        clean_stocks.append(i[0])
    return clean_stocks

#PYQT UI

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadStocks()
        self.ui.add_stock.clicked.connect(self.addStock)
        self.ui.buy_stock.clicked.connect(self.buyStock)
        self.ui.lineEdit.textChanged.connect(self.filter_items)
        self.ui.pushButton.clicked.connect(self.buyStock_o)
        self.ui.sell_stock.clicked.connect(self.sellStock)
        self.ui.pushButton_2.clicked.connect(self.sellStock_o)
        self.ui.pushButton_3.clicked.connect(self.analyze)
        self.loadGlobalStocks()
        self.portfolioValue()
        self.holdingsValue()


    def portfolioValue(self):
        portfolio_value = portfolio.total_portfolio_value()
        formatted_portfolio_value = f"{portfolio_value:.2f}"
        self.ui.value_investment.setText(str(formatted_portfolio_value))
    
    def holdingsValue(self):
        holdings_value = portfolio.holdings_value()
        formatted_holdings_value = f"{holdings_value:.2f}"
        self.ui.value_investment_2.setText(str(formatted_holdings_value))

    def loadGlobalStocks(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(global_all_stocks())
        self.ui.listWidget.setCurrentRow(0)
    
    def loadStocks(self):
        self.ui.list_stock.clear()
        self.ui.list_stock.addItems(loading_stocks())
        self.ui.list_stock.setCurrentRow(0)

    def addStock(self):
        currentIndex = self.ui.list_stock.currentRow()
        stock = self.ui.list_stock.item(currentIndex).text().split('@')[0]
        stock_qty, ok = QInputDialog.getText(self,"Add to your stock", "Stock Quantity")
        stock_value, ok = QInputDialog.getText(self,"Add to your stock", "Purchased at what price?")
        if ok and stock_qty is not None and stock_value is not None:
            portfolio.add_stock(Stock(stock),stock_qty, stock_value)
            save_portfolio(portfolio)
            self.loadStocks()
            self.portfolioValue()
    
    def buyStock(self):
        currentIndex = self.ui.list_stock.currentRow()
        stock = self.ui.list_stock.item(currentIndex).text().split('@')[0]
        stock_qty, ok = QInputDialog.getText(self,"Add to your stock", "Stock Quantity")
        if ok and stock_qty is not None:
            stocks = Stock(stock)
            portfolio.add_stock(stocks,stock_qty,stocks.price)
            save_portfolio(portfolio)
            self.loadStocks()
            self.portfolioValue()
            self.holdingsValue()
    
    def buyStock_o(self):
        currentIndex = self.ui.listWidget.currentRow()
        stock = self.ui.listWidget.item(currentIndex).text()
        stock_qty, ok = QInputDialog.getText(self,"Add to your stock", "Stock Quantity")
        if ok and stock_qty is not None:
            stocks = Stock(stock)
            portfolio.add_stock(stocks,stock_qty,stocks.price)
            save_portfolio(portfolio)
            self.loadStocks()
            self.portfolioValue()
            self.holdingsValue()
    
    def sellStock(self):
        currentIndex = self.ui.list_stock.currentRow()
        stock = self.ui.list_stock.item(currentIndex).text().split('@')[0]
        stock_qty, ok = QInputDialog.getText(self,"How many stocks to sell?", "Stock Quantity")
        if ok and stock_qty is not None:
            portfolio.remove_stock(stock,stock_qty)
            save_portfolio(portfolio)
            self.loadStocks()
            self.portfolioValue()
            self.holdingsValue()
    
    def sellStock_o(self):
        currentIndex = self.ui.listWidget.currentRow()
        stock = self.ui.listWidget.item(currentIndex).text()
        stock_qty, ok = QInputDialog.getText(self,"How many stocks to sell?", "Stock Quantity")
        if ok and stock_qty is not None:
            portfolio.remove_stock(stock,stock_qty)
            save_portfolio(portfolio)
            self.loadStocks()
            self.portfolioValue()
            self.holdingsValue()
    
    def analyze(self):
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        do_test(symbol)
    
    def filter_items(self):
        search_text = self.ui.lineEdit.text().lower()

        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            if search_text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)
                
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()