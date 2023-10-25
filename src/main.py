from strategy_tester import *
from sqlite_commands import *
from stock_portfolio import *
from stock import *
from data_loader import *

"""
Text based main ( Deprecated )
"""

all_list_of_stocks = list_of_stocks()

def in_portfolio_menu(selection_key):
    current_portfolio = portfolios[selection_key]
    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Total Portfolio Value")
        print("3. List Stocks")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Available Stocks\n")
            print(all_list_of_stocks)
            symbol = input("Enter symbol from the above list: ")
            quantity = int(input("Enter quantity of stocks: "))
            value = float(input("Enter value at which stock was purchased: "))
            current_portfolio.add_stock(Stock(symbol),quantity,value)
        
        elif choice == 2:
            print("Your total portfolio value is: ",current_portfolio.total_portfolio_value())
        
        elif choice == 3:
            print("List of stocks owned: ",list(current_portfolio.stocks_owned.keys()))

        elif choice == 4:
            break
    
    current_portfolio.add_stock(Stock("ZOMATO"),10,106.5)
    print(current_portfolio.total_portfolio_value())


def create_portfolio(portfolios):
    portfolio_key = input("Enter a key for your portfolio: ")
    portfolio = StockPortfolio()
    portfolios[portfolio_key] = portfolio
    print(f"Portfolio with key '{portfolio_key}' created!\n")

def select_portfolio(portfolios):
    print("Select a portfolio:")
    for key, portfolio in portfolios.items():
        print(f"{key}. Portfolio")

    selection_key = input("Enter the key of the portfolio you want to select: ")
    if selection_key in portfolios:
        in_portfolio_menu(selection_key)
    else:
        print("Invalid selection. Please try again.")
        return select_portfolio(portfolios)

portfolios = {}


while True:
    print("\nMenu:")
    print("1. Create Portfolio")
    print("2. Select Portfolio")
    print("3. Run Backtesting")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_portfolio(portfolios)
    elif choice == "2":
        if portfolios:
            selected_portfolio = select_portfolio(portfolios)
            print(f"Selected Portfolio: {selected_portfolio}")
        else:
            print("No portfolios created yet.")
    elif choice == "3":
        if portfolios:
            print("Available Stocks\n")
            print(all_list_of_stocks)
            symbol = input("Enter one of the symbols above to backtest: ")
            do_test(symbol)
        else:
            print("No portfolios selected.")
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")