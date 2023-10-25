from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
import talib as tal
import ta
import pandas as pd
from stock import Stock

# Creating Strategies by creating classes

class SMACross(Strategy):
    n1=50
    n2=100

    def init(self):
        # Initialize moving averages for SMACross strategy
        price = self.data.Close
        self.ma1 = self.I(ta.trend.sma_indicator, pd.Series(price), self.n1)
        self.ma2 = self.I(ta.trend.sma_indicator, pd.Series(price), self.n2)
    
    def next(self):
        # Buy and sell signals based on moving average crossover
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2,self.ma1):
            self.sell()

# Not in use
class MySMAStrategy(Strategy):

    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)
    
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2,self.ma1):
            self.sell()

class MACDStrategy(Strategy):
    n_short = 12
    n_long = 26

    def init(self):
        # Initialize MACD indicator for MACDStrategy
        price = self.data.Close
        self.macd = self.I(lambda x: tal.MACD(x, fastperiod=self.n_short, slowperiod=self.n_long)[0], price)
        self.macd_signal = self.I(lambda x: tal.MACD(x, fastperiod=self.n_short, slowperiod=self.n_long)[1], price)

    def next(self):
        # Buy and sell signals based on MACD crossover
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal, self.macd):
            self.sell()


# Usage:variable = run_backtest(stock object)
def run_backtest_sma(stock):
    # Run backtest for SMACross strategy
    data = stock.daily_data
    backtest = Backtest(data, SMACross,cash = 20000, commission=0.002, exclusive_orders=True)

    # Optimize the strategy
    optim = backtest.optimize(n1 = range(50,160,10),
                        n2 = range(50,160,10),
                        constraint= lambda x: x.n2 - x.n1 > 20,
                        maximize='Return [%]')
    backtest.plot()

    # Display optimization results
    optim = pd.DataFrame(optim)
    list_return = optim.head(25).to_string(index=False).split('\n')
    additional_list = [
        'Head','Start', 'End', 'Duration', 'Exposure Time [%]', 'Equity Final [$]', 'Equity Peak [$]',
        'Return [%]', 'Buy & Hold Return [%]', 'Return (Ann.) [%]', 'Volatility (Ann.) [%]',
        'Sharpe Ratio', 'Sortino Ratio', 'Calmar Ratio', 'Max. Drawdown [%]', 'Avg. Drawdown [%]',
        'Max. Drawdown Duration', 'Avg. Drawdown Duration', '# Trades', 'Win Rate [%]',
        'Best Trade [%]', 'Worst Trade [%]', 'Avg. Trade [%]', 'Max. Trade Duration',
        'Avg. Trade Duration', 'Profit Factor'
    ]

    concatenated_list = [f"{key}   :   {value}" for key, value in zip(additional_list, list_return)]
    return concatenated_list

def run_backtest_macd(stock):
    # Run backtest for MACDStrategy
    data = stock.daily_data
    backtest = Backtest(data, MACDStrategy,cash = 20000, commission=0.002, exclusive_orders=True)

    # Optimize the strategy
    params = {
        'n_short': range(12, 26),
        'n_long': range(26, 40),
    }
    optim = backtest.optimize(**params, maximize='Return [%]')
    backtest.plot()

    # Display optimization results
    optim = pd.DataFrame(optim)
    list_return = optim.head(25).to_string(index=False).split('\n')
    additional_list = [
        'Head','Start', 'End', 'Duration', 'Exposure Time [%]', 'Equity Final [$]', 'Equity Peak [$]',
        'Return [%]', 'Buy & Hold Return [%]', 'Return (Ann.) [%]', 'Volatility (Ann.) [%]',
        'Sharpe Ratio', 'Sortino Ratio', 'Calmar Ratio', 'Max. Drawdown [%]', 'Avg. Drawdown [%]',
        'Max. Drawdown Duration', 'Avg. Drawdown Duration', '# Trades', 'Win Rate [%]',
        'Best Trade [%]', 'Worst Trade [%]', 'Avg. Trade [%]', 'Max. Trade Duration',
        'Avg. Trade Duration', 'Profit Factor'
    ]

    concatenated_list = [f"{key}   :   {value}" for key, value in zip(additional_list, list_return)]
    return concatenated_list
