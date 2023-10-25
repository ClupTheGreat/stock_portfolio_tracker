import pandas_datareader as web
import datetime as dt
import yfinance as yf
import data_loader

start_daily = dt.datetime(2023,1,1)
start_weekly = dt.datetime(2022,1,1)
start_monthly = dt.datetime(2019,1,1)
end = dt.datetime.now()

def get_current_price(symbol):
    data = web.DataReader('TSLA','yahoo',start_daily,end)
    print(data)

get_current_price("ZOMATO")