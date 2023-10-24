import sqlite3
import os
import time
import pandas as pd
from data_loader import DataLoader

#TODO: Create a method which allows you to delete

# print(time.perf_counter())

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



#Will be using this same function, since we have the latestdate, individually update whenever the stock is selected
def add_price_to_db(symbol, interval):
  get_stock_id = "SELECT DISTINCT stock_id FROM stock WHERE symbol = '{}'".format(symbol)
  c.execute(get_stock_id)
  stock_id = c.fetchone()[0]
  data_loader = DataLoader()
  
  if interval == "daily":
    #Date checking
    latest_date_query = "SELECT MAX(date) FROM stock_price_daily WHERE stock_id = {}".format(stock_id)
    c.execute(latest_date_query)
    latest_date = c.fetchone()[0]
    latest_date = pd.to_datetime(latest_date)

    #Loading in data
    stock_data = data_loader.get_stock_data(symbol)
    for index,row in stock_data.iterrows():
      date = index
      date = pd.to_datetime(date)
      if latest_date != None:
        if date > latest_date:
          open_value = row['Open']
          high_value = row['High']
          low_value = row['Low']
          close_value = row['Close']
          adj_close_value = row['Adj Close']
          volume_value = row['Volume']
          query = "INSERT INTO stock_price_daily (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
          c.execute(query)
      else:
        open_value = row['Open']
        high_value = row['High']
        low_value = row['Low']
        close_value = row['Close']
        adj_close_value = row['Adj Close']
        volume_value = row['Volume']
        query = "INSERT INTO stock_price_daily (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
        c.execute(query)
    
  elif interval == "weekly":
    #Date Checking
    latest_date_query = "SELECT MAX(date) FROM stock_price_weekly WHERE stock_id = {}".format(stock_id)
    c.execute(latest_date_query)
    latest_date = c.fetchone()[0]
    latest_date = pd.to_datetime(latest_date)

    #Loading data
    stock_data = data_loader.get_stock_data_weekly(symbol)
    for index,row in stock_data.iterrows():
      date = index
      date = pd.to_datetime(date)
      if latest_date != None:
        if date > latest_date:
          open_value = row['Open']
          high_value = row['High']
          low_value = row['Low']
          close_value = row['Close']
          adj_close_value = row['Adj Close']
          volume_value = row['Volume']
          query = "INSERT INTO stock_price_weekly (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
          c.execute(query)
      else:
        open_value = row['Open']
        high_value = row['High']
        low_value = row['Low']
        close_value = row['Close']
        adj_close_value = row['Adj Close']
        volume_value = row['Volume']
        query = "INSERT INTO stock_price_weekly (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
        c.execute(query)
    print("weekly")

  elif interval == "monthly":
    #Date Checking
    latest_date_query = "SELECT MAX(date) FROM stock_price_monthly WHERE stock_id = {}".format(stock_id)
    c.execute(latest_date_query)
    latest_date = c.fetchone()[0]
    latest_date = pd.to_datetime(latest_date)

    #Loading data
    stock_data = data_loader.get_stock_data_monthly(symbol)
    for index,row in stock_data.iterrows():
      date = index
      date = pd.to_datetime(date)
      if latest_date != None:
        if date > latest_date:
          open_value = row['Open']
          high_value = row['High']
          low_value = row['Low']
          close_value = row['Close']
          adj_close_value = row['Adj Close']
          volume_value = row['Volume']
          query = "INSERT INTO stock_price_monthly (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
          c.execute(query)
      else:
        open_value = row['Open']
        high_value = row['High']
        low_value = row['Low']
        close_value = row['Close']
        adj_close_value = row['Adj Close']
        volume_value = row['Volume']
        query = "INSERT INTO stock_price_monthly (stock_id, date, open, high, low, close, adj_close, volume) VALUES ({}, '{}', {}, {}, {}, {}, {}, {})".format(stock_id, date, open_value, high_value, low_value, close_value, adj_close_value, volume_value)
        c.execute(query)
    print("monthly")
  else:
     print("error")
  #  code
  return None

def get_stock_id_from_symbol(symbol):
  query = "SELECT stock_id FROM stock WHERE symbol == '{}';".format(symbol)
  c.execute(query)
  val = c.fetchone()[0]
  return val

def get_current_prices(symbol):
  add_price_to_db(symbol,"daily")
  stock_id = get_stock_id_from_symbol(symbol)
  query = 'SELECT close,MAX(date) FROM stock_price_daily WHERE stock_id == {};'.format(stock_id)
  c.execute(query)
  return c.fetchall()[0][0]

  
def list_of_stocks():
  # For now displays only top 10 stocks for visibility and performance reasons
  query = "SELECT symbol FROM stock"
  c.execute(query)
  return c.fetchall()

get_current_prices("TCS")

# Run this file to execute the above function and add all the stocks to database
# add_stock_to_db()

# stock_list = pd.read_csv(os.path.join("data","nse_symbols.csv"))
# for i in range(len(stock_list["Sr. No."])):
#   if i>10:
#     break
  # add_price_to_db(stock_list["Symbol"][i],"monthly")
  # add_price_to_db(stock_list["Symbol"][i],"daily")
  # add_price_to_db(stock_list["Symbol"][i],"weekly")


# add_price_to_db("TCS","monthly")
conn.commit()

# print(time.perf_counter())