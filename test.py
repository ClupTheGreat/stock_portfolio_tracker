import yfinance as yf

ticker = yf.download("ZOMATO.NS",period = '1mo', interval='1wk')
# print(ticker)
# print(ticker["Open"])
# print(str(ticker.index[3])[0:10])

for index,row in ticker.iterrows():
    date = index
    open_value = row['Open']
    high_value = row['High']
    low_value = row['Low']
    close_value = row['Close']
    adj_close_value = row['Adj Close']
    volume_value = row['Volume']
    print(str(date)[0:10])

