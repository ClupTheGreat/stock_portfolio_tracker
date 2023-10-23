# from stock_portfolio import StockPortfolio
# from data_loader import DataLoader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

# ticker = yf.download("HDFCBANK.NS",period='5y', interval='1d')

class SimpleMovingAverageBacktester:
    def __init__(self, data, short_window, long_window):
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
        self.signals = pd.DataFrame(index=data.index)
        self.signals['signal'] = 0.0 
    
    def calculate_pnl(self):
        capital = 100000.0  
        position = 0.0
        pnl = []

        for i in range(len(self.signals)):
            price = self.data['Close'].iloc[i]

            if self.signals['positions'].iloc[i] == 1.0: 
                position = capital / price
                capital = 0.0
            elif self.signals['positions'].iloc[i] == -1.0:  
                capital = position * price
                position = 0.0

            pnl.append(capital + position * price)

        return pnl

    def generate_signals(self):
        self.signals['short_mavg'] = self.data['Close'].rolling(window=self.short_window, min_periods=1, center=False).mean()
        self.signals['long_mavg'] = self.data['Close'].rolling(window=self.long_window, min_periods=1, center=False).mean()

        self.signals['signal'][self.short_window:] = \
            np.where(self.signals['short_mavg'][self.short_window:] > self.signals['long_mavg'][self.short_window:], 1.0, 0.0)

        self.signals['positions'] = self.signals['signal'].diff()

    def plot_signals(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(self.data['Close'], label='Price')
        ax.plot(self.signals['short_mavg'], label=f'Short {self.short_window} days MA')
        ax.plot(self.signals['long_mavg'], label=f'Long {self.long_window} days MA')

        ax.plot(self.signals.loc[self.signals.positions == 1.0].index,
                 self.signals.short_mavg[self.signals.positions == 1.0],
                 '^', markersize=10, color='g', label='Buy Signal')

        ax.plot(self.signals.loc[self.signals.positions == -1.0].index,
                 self.signals.short_mavg[self.signals.positions == -1.0],
                 'v', markersize=10, color='r', label='Sell Signal')

        plt.title('Moving Average Crossover Strategy')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.legend()
        plt.show()

    def print_pnl(self):
        pnl = self.calculate_pnl()
        start_capital = 100000.0
        
        end_of_trade = None

        for i, date in enumerate(self.data.index):
            if self.signals['positions'].iloc[i] == -1.0:  # Sell signal
                end_of_trade = f"{date}\t\tStarting Capital: {start_capital:.2f}, Resulting Capital: {pnl[i]:.2f}"

        if end_of_trade:
            total_profit = pnl[i] - start_capital
            percent_gain = (pnl[i]/start_capital) * 100
            print("Date\t\t\tCapital")
            print(end_of_trade)
            print("Total profit", total_profit)
            print("Percent Gain", percent_gain)

    def buy_and_hold_pnl(self):
        capital = 100000.0  
        position = capital / self.data['Close'].iloc[0]
        pnl = [capital + position * price for price in self.data['Close']]

        return pnl

short_window = 40
long_window = 100

def do_test(symbol):
    text = symbol+".NS"
    ticker = yf.download(text,period='5y', interval='1d')
    backtester = SimpleMovingAverageBacktester(ticker, short_window, long_window)
    backtester.generate_signals()

    backtester.print_pnl()

    # Buy and hold strategy for comparison
    buy_and_hold_pnl = backtester.buy_and_hold_pnl()
    print("\nBuy and Hold Strategy:")
    print(f"Starting Capital: 100000.0, Resulting Capital: {buy_and_hold_pnl[-1]:.2f}")

    backtester.plot_signals()
