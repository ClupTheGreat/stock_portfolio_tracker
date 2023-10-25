from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
import talib as tal
import ta
import pandas as pd
from stock import Stock

# stock1 = Stock("ZOMATO")
# stock2 = Stock("TCS")
# stock3 = Stock("INFY")
# stock4 = Stock("HDFCBANK")
# stock5 = Stock("LICI")
# stock6 = Stock('BRITANNIA')

class SMACross(Strategy):
    n1=50
    n2=100

    def init(self):
        price = self.data.Close
        self.ma1 = self.I(ta.trend.sma_indicator, pd.Series(price), self.n1)
        self.ma2 = self.I(ta.trend.sma_indicator, pd.Series(price), self.n2)
    
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2,self.ma1):
            self.sell()

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

# class MACDStrategy(Strategy):
#     def init(self):
#         price = self.data.Close
#         self.macd = self.I(lambda x: tal.MACD(x)[0],price)
#         self.macd_signal = self.I(lambda x: tal.MACD(x)[1],price)
    
#     def next(self):
#         if crossover(self.macd, self.macd_signal):
#             self.buy()
#         elif crossover(self.macd_signal,self.macd):
#             self.sell()
class MACDStrategy(Strategy):
    n_short = 12
    n_long = 26

    def init(self):
        price = self.data.Close
        self.macd = self.I(lambda x: tal.MACD(x, fastperiod=self.n_short, slowperiod=self.n_long)[0], price)
        self.macd_signal = self.I(lambda x: tal.MACD(x, fastperiod=self.n_short, slowperiod=self.n_long)[1], price)

    def next(self):
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal, self.macd):
            self.sell()


# print(GOOG)
# backtest = Backtest(GOOG, MySMAStrategy, commission=0.002, exclusive_orders=True)
# stats = backtest.run()
# backtest.plot()
# print(stats)

# Usage:variable = run_backtest(stock object)
def run_backtest_sma(stock):
    data = stock.daily_data

    backtest = Backtest(data, SMACross,cash = 20000, commission=0.002, exclusive_orders=True)
    optim = backtest.optimize(n1 = range(50,160,10),
                        n2 = range(50,160,10),
                        constraint= lambda x: x.n2 - x.n1 > 20,
                        maximize='Return [%]')
    backtest.plot()
    optim = pd.DataFrame(optim)
    list_return = optim.head(25).to_string(index=False).split('\n')
    additional_list = [
        'Start', 'End', 'Duration', 'Exposure Time [%]', 'Equity Final [$]', 'Equity Peak [$]',
        'Return [%]', 'Buy & Hold Return [%]', 'Return (Ann.) [%]', 'Volatility (Ann.) [%]',
        'Sharpe Ratio', 'Sortino Ratio', 'Calmar Ratio', 'Max. Drawdown [%]', 'Avg. Drawdown [%]',
        'Max. Drawdown Duration', 'Avg. Drawdown Duration', '# Trades', 'Win Rate [%]',
        'Best Trade [%]', 'Worst Trade [%]', 'Avg. Trade [%]', 'Max. Trade Duration',
        'Avg. Trade Duration', 'Profit Factor'
    ]

    concatenated_list = [f"{key}   :   {value}" for key, value in zip(additional_list, list_return)]
    return concatenated_list

def run_backtest_macd(stock):
    data = stock.daily_data

    backtest = Backtest(data, MACDStrategy,cash = 20000, commission=0.002, exclusive_orders=True)
    params = {
        'n_short': range(12, 26),
        'n_long': range(26, 40),
    }

    # Run the optimization
    optim = backtest.optimize(**params, maximize='Return [%]')
    # optim = backtest.optimize(n1 = range(50,160,10),
    #                     n2 = range(50,160,10),
    #                     constraint= lambda x: x.n2 - x.n1 > 20,
    #                     maximize='Return [%]')
    backtest.plot()
    optim = pd.DataFrame(optim)
    list_return = optim.head(25).to_string(index=False).split('\n')
    additional_list = [
        'Start', 'End', 'Duration', 'Exposure Time [%]', 'Equity Final [$]', 'Equity Peak [$]',
        'Return [%]', 'Buy & Hold Return [%]', 'Return (Ann.) [%]', 'Volatility (Ann.) [%]',
        'Sharpe Ratio', 'Sortino Ratio', 'Calmar Ratio', 'Max. Drawdown [%]', 'Avg. Drawdown [%]',
        'Max. Drawdown Duration', 'Avg. Drawdown Duration', '# Trades', 'Win Rate [%]',
        'Best Trade [%]', 'Worst Trade [%]', 'Avg. Trade [%]', 'Max. Trade Duration',
        'Avg. Trade Duration', 'Profit Factor'
    ]

    concatenated_list = [f"{key}   :   {value}" for key, value in zip(additional_list, list_return)]
    return concatenated_list
