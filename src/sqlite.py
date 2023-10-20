import sqlite3
import os
import time

print(time.perf_counter())

conn = sqlite3.connect(os.path.join("data",'stocks.db'))

c = conn.cursor()

# Create a portfolio table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS portfolio (
          portfolio_id integer NOT NULL,
          password text NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS stock (
          stock_id integer NOT NULL,
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

c.execute("""CREATE TABLE IF NOT EXISTS stock_price (
          id integer NOT NULL,
          stock_id integer NOT NULL,
          date text NOT NULL,
          open real NOT NULL,
          high real NOT NULL,
          low real NOT NULL,
          close real NOT NULL,
          FOREIGN KEY (stock_id) REFERENCES stock (stock_id)
        )""")

conn.commit()

print(time.perf_counter())