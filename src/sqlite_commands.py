import sqlite3
import os
import time
import pandas as pd
from data_loader import DataLoader
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect(os.path.join("data",'stocks.db'))

# Create a cursor object
c = conn.cursor()

# Create 'stock' table to store the list of stocks
c.execute("""CREATE TABLE IF NOT EXISTS stock (
          stock_id integer PRIMARY KEY,
          symbol text NOT NULL,
          company_text text NOT NULL
        )""")

def add_stock_to_db():
    """
    Add stock information to the 'stock' table in the database
    """
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
  
def list_of_stocks():
  """
  Gets a list of stock symbols from the 'stock' table and returns a list of it
  """
  query = "SELECT symbol FROM stock"
  c.execute(query)
  return c.fetchall()

conn.commit()