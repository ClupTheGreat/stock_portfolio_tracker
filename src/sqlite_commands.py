import sqlite3
import os
import time
import pandas as pd
from data_loader import DataLoader

print(time.perf_counter())

conn = sqlite3.connect(os.path.join("data",'stocks.db'))

c = conn.cursor()

# Create a portfolio table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS portfolio (
          portfolio_id integer PRIMARY KEY,
          password text NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS stock (
          stock_id integer PRIMARY KEY,
          symbol text NOT NULL,
          company_text text NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS owned_stocks (
          portfolio_id integer NOT NULL,
          stock_id integer NOT NULL,
          amount integer NOT NULL,
          price real NOT NULL,
          FOREIGN KEY (stock_id) REFERENCES stock (stock_id),
          FOREIGN KEY (portfolio_id) REFERENCES portfolio (portfolio_id)
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS stock_price_daily (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          stock_id integer NOT NULL,
          date text NOT NULL,
          open real NOT NULL,
          high real NOT NULL,
          low real NOT NULL,
          close real NOT NULL,
          adj_close real NOT NULL,
          volume real NOT NULL,
          FOREIGN KEY (stock_id) REFERENCES stock (stock_id)
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS stock_price_weekly (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          stock_id integer NOT NULL,
          date text NOT NULL,
          open real NOT NULL,
          high real NOT NULL,
          low real NOT NULL,
          close real NOT NULL,
          adj_close real NOT NULL,
          volume real NOT NULL,
          FOREIGN KEY (stock_id) REFERENCES stock (stock_id)
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS stock_price_monthly (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          stock_id integer NOT NULL,
          date text NOT NULL,
          open real NOT NULL,
          high real NOT NULL,
          low real NOT NULL,
          close real NOT NULL,
          adj_close real NOT NULL,
          volume real NOT NULL,
          FOREIGN KEY (stock_id) REFERENCES stock (stock_id)
        )""")

def add_stock_to_db():
    # Add all the stocks to database, takes in a csv file nse_symbols downloaded from nse website which will have all the available stocks
    stock_list = pd.read_csv(os.path.join("data","nse_symbols.csv"))
    for i in range(len(stock_list["Sr. No."])):
      stock_id = str(stock_list["Sr. No."][i])
      symbol = str(stock_list["Symbol"][i])
      company_text = str(stock_list["Company Name"][i])
      query = """INSERT INTO stock (stock_id, symbol, company_text) VALUES ({},"{}","{}")""".format(stock_id, symbol, company_text)
      try:
        c.execute(query)
      except:
         print("stock already present")

def add_price_to_db(symbol, interval,stock_id):
  stock_id = 107
  data_loader = DataLoader()

  latest_date_query = "SELECT MAX(date) FROM stock_price_daily WHERE stock_id = {}".format(stock_id)
  c.execute(latest_date_query)
  latest_date = c.fetchone()[0]
  latest_date = pd.to_datetime(latest_date)
  
  if interval == "daily":
    stock_data = data_loader.get_stock_data(symbol, 30)
    for index,row in stock_data.iterrows():
      date = index
      date = pd.to_datetime(date)
      if date > latest_date:
        open_value = row['Open']
        high_value = row['High']
        low_value = row['Low']
        close_value = row['Close']
        adj_close_value = row['Adj Close']
        volume_value = row['Volume']
        query = "INSERT INTO stock_price_daily (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
        c.execute(query)
    
  elif interval == "weekly":
    print("weekly")
  elif interval == "monthly":
    print("monthly")
  else:
     print("error")
  #  code
  return None
  
# Run this file to execute the above function and add all the stocks to database
# add_stock_to_db()
add_price_to_db("ZOMATO","daily",107)
conn.commit()

print(time.perf_counter())