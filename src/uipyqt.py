from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from ui1 import Ui_StockManager
import sys
from strategy_tester import *
from sqlite_commands import *
from stock_portfolio import *
from stock import *
from data_loader import *
from visualization import *
from strats import *

# Creating a portfolio and saving function
def load_portfolio(username):
    """
    Load existing portfolio from a pickle file or create a new one if not found.
    """
    if os.path.exists(username+"_portfolio.pickle"):
        with open(username+"_portfolio.pickle", "rb") as file:
            portfolio = pickle.load(file)
            print("Existing portfolio loaded.")
    else:
        portfolio = StockPortfolio()
        print("New portfolio created.")
    
    return portfolio

def save_portfolio(portfolio,username):
    """
    Save the portfolio to a pickle file.
    """
    with open(username+"_portfolio.pickle", "wb") as file:
        pickle.dump(portfolio, file)
        print("Portfolio saved.")

def delete_portfolio(username):
    """
    Delete the saved portfolio file if it exists.
    """
    if os.path.exists("saved_portfolio.pickle"):
        os.remove("saved_portfolio.pickle")
        print("Portfolio deleted.")
    else:
        print("No portfolio found.")


# Create / load portfolio according to the username
portfolio = load_portfolio("Rohan")

def loading_stocks():
    """
    Load the list of owned stocks from the portfolio.
    """
    list_of_owned_stocks = []
    for i in portfolio.stocks_owned.items():
        stock_name = i[0]
        purchase_price = i[1]['purchase_price']
        # Convert purchase_price to float if it's a string
        if isinstance(purchase_price, str):
            purchase_price = float(purchase_price)

        formatted_price = f"{purchase_price:.2f}"
        
        stock_info = f"{stock_name}@{formatted_price} - Quantity: {i[1]['quantity']}"
        list_of_owned_stocks.append(stock_info)
    return list_of_owned_stocks

def global_all_stocks():
    """
    Get a list of all available stocks from the database.
    """
    stocks = list(sqlite_commands.list_of_stocks())
    clean_stocks = []
    for i in stocks:
        clean_stocks.append(i[0])
    return clean_stocks

#PYQT UI

class windowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(windowManager, self).__init__()
        self.ui = Ui_StockManager()
        self.ui.setupUi(self)

        self.ui.add_stock.clicked.connect(self.addStock)
        self.ui.buy_stock.clicked.connect(self.buyStock)
        self.ui.lineEdit.textChanged.connect(self.filter_items)
        self.ui.pushButton.clicked.connect(self.buyStock_o)
        self.ui.sell_stock.clicked.connect(self.sellStock)
        self.ui.pushButton_2.clicked.connect(self.sellStock_o)
        self.ui.daily_chart.clicked.connect(self.dailyChart)
        self.ui.weekly_chart.clicked.connect(self.weeklyChart)
        self.ui.monthly_chart.clicked.connect(self.monthlyChart)
        self.ui.get_sma.clicked.connect(self.getSMA)
        self.ui.get_macd.clicked.connect(self.getMACD)
        self.ui.get_rsi.clicked.connect(self.getRSI)
        self.ui.anal_macd.clicked.connect(self.analMACD)
        self.ui.anal_sma.clicked.connect(self.analSMA)
        self.loadGlobalStocks()
        self.update()

    def update(self):
        self.loadStocks()
        self.portfolioValue()
        self.holdingsValue()

    def portfolioValue(self):
        """
        Update and display the total value of the portfolio.
        """
        portfolio_value = portfolio.total_portfolio_value()
        formatted_portfolio_value = f"{portfolio_value:.2f}"
        self.ui.value_investment.setText(str(formatted_portfolio_value))
    
    def holdingsValue(self):
        """
        Update and display the current value of holdings in the portfolio.
        """
        holdings_value = portfolio.holdings_value()
        formatted_holdings_value = f"{holdings_value:.2f}"
        self.ui.value_investment_2.setText(str(formatted_holdings_value))

    def loadGlobalStocks(self):
        """
        Load and display the list of all available stocks in the global stocks list widget.
        """
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(global_all_stocks())
        self.ui.listWidget.setCurrentRow(0)
    
    def loadStocks(self):
        """
        Load and display the list of owned stocks in the user's stocks list widget.
        """
        self.ui.list_stock.clear()
        self.ui.list_stock.addItems(loading_stocks())
        self.ui.list_stock.setCurrentRow(0)

    def addStock(self):
        """
        Add a new stock to the user's portfolio
        """
        currentIndex = self.ui.list_stock.currentRow()
        stock = self.ui.list_stock.item(currentIndex).text().split('@')[0]
        stock_qty, ok = QInputDialog.getText(self,"Add to your stock", "Stock Quantity")
        stock_value, ok = QInputDialog.getText(self,"Add to your stock", "Purchased at what price?")
        if ok and stock_qty is not None and stock_value is not None:
            portfolio.add_stock(Stock(stock),stock_qty, stock_value)
            save_portfolio(portfolio)
            self.update()
    
    def buyStock(self):
        """
        Buy additional stock
        """
        currentIndex = self.ui.list_stock.currentRow()
        stock = self.ui.list_stock.item(currentIndex).text().split('@')[0]
        stock_qty, ok = QInputDialog.getText(self,"Add to your stock", "Stock Quantity")
        if ok and stock_qty is not None:
            stocks = Stock(stock)
            portfolio.add_stock(stocks,stock_qty,stocks.price)
            save_portfolio(portfolio)
            self.update()
    
    def buyStock_o(self):
        """
        Buy additional stock from the other tab
        """
        currentIndex = self.ui.listWidget.currentRow()
        stock = self.ui.listWidget.item(currentIndex).text()
        stock_qty, ok = QInputDialog.getText(self,"Add to your stock", "Stock Quantity")
        if ok and stock_qty is not None:
            stocks = Stock(stock, None)
            portfolio.add_stock(stocks,stock_qty,stocks.price)
            save_portfolio(portfolio)
            self.update()
    
    def sellStock(self):
        """
        Sell stock
        """
        currentIndex = self.ui.list_stock.currentRow()
        stock = self.ui.list_stock.item(currentIndex).text().split('@')[0]
        stock_qty, ok = QInputDialog.getText(self,"How many stocks to sell?", "Stock Quantity")
        if ok and stock_qty is not None:
            portfolio.remove_stock(stock,stock_qty)
            save_portfolio(portfolio)
            self.update()
    
    def sellStock_o(self):
        """
        Sell stock from the other tab
        """
        currentIndex = self.ui.listWidget.currentRow()
        stock = self.ui.listWidget.item(currentIndex).text()
        stock_qty, ok = QInputDialog.getText(self,"How many stocks to sell?", "Stock Quantity")
        if ok and stock_qty is not None:
            portfolio.remove_stock(stock,stock_qty)
            save_portfolio(portfolio)
            self.update()
    
    def dailyChart(self):
        """
        Display daily stock chart for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        stock.create_chart_daily()

    def weeklyChart(self):
        """
        Display weekly stock chart for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        stock.create_chart_weekly()
    
    def monthlyChart(self):
        """
        Display monthly stock chart for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        stock.create_chart_monthly()

    def getSMA(self):
        """
        Display a Simple Moving Average (SMA) visualization for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        sma_visualization(stock.daily_data)


    def getMACD(self):
        """
        Display a Moving Average Convergence Divergence (MACD) visualization for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        macd_visualization(stock.daily_data)

    def getRSI(self):
        """
        Display a Relative Strength Index (RSI) visualization for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        rsi_visualization(stock.daily_data)

    def analMACD(self):
        """
        Run MACD backtest for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        optim = run_backtest_macd(stock)
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(optim)

    def analSMA(self):
        """
        Run MACD backtest for the selected stock
        """
        currentIndex = self.ui.listWidget.currentRow()
        symbol = self.ui.listWidget.item(currentIndex).text()
        stock = Stock(symbol)
        optim = run_backtest_sma(stock)
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(optim)
    
    def filter_items(self):
        """
        Filter the list of owned stocks based on the entered text.
        """
        search_text = self.ui.lineEdit.text().lower()

        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            if search_text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)


# def portfolio_manager(username):
#     print(username)
#     win = window()
#     win.show()
#     print("after show")
    # def register_account(username, password):
    #     if is_valid_username(username):
    #         if is_valid_password(password):
    #             res = register(username,password)
    #             if res == True:
    #                 show_info_messagebox("Registration successful, login with your username and password")
    #                 registerWindow.hide()
    #                 return True
    #             else:
    #                 show_info_messagebox("Username not available, Try Again!")
    #                 return False
    #         else:
    #             show_info_messagebox("Wrong password length")
    #     else:
    #         show_info_messagebox("Wrong username length")
    # # app = QtWidgets.QApplication(sys.argv)
    # registerWindow = QtWidgets.QMainWindow()
    # ui = Ui_registerWindow()
    # ui.setupUi(registerWindow)
    # ui.finishRegistration.clicked.connect(lambda: register_account(ui.plainTextEdit.toPlainText(), ui.plainTextEdit_2.toPlainText()))
    # ui.cancel.clicked.connect(lambda: registerWindow.close())
    # registerWindow.show()

# def appMain(username):
#     print(username)
#     app = QtWidgets.QApplication(sys.argv)
#     win = windowManager()
#     win.show()
#     sys.exit(app.exec_())

# appMain("Rohan")