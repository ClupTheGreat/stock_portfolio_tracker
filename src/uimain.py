from pathlib import Path
from tkinter import *
import stock_portfolio
import stock
import sqlite_commands
import os
import pickle

"""
Deprecated
"""

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Code\tkinter_des\figmatotk\build\assets\frame3")

# Button lift needed, as new canvas is placed on top of it

# BuySell

def button_lift():
    for button in [button_1, button_2, button_3, button_4]:
        button.lift()


# Accessing global variable state in order to hide and place canvas
def change_canvas(next_canvas):
    exists = 0
    exists_buttons = 0
    global current_canvas
    global testing_canvas
    global orders_canvas
    global tkstring_total_value
    global tkstring_holdings_value
    tkstring_total_value = portfolio.total_portfolio_value()
    tkstring_holdings_value = portfolio.holdings_value()
    current_canvas.place_forget()
    next_canvas.place(x = 0, y = 0)
    current_canvas = next_canvas
    if current_canvas == testing_canvas:
        exists = 1
        exists_buttons = 0
        list_maker(exists, exists_buttons)
    elif current_canvas == orders_canvas:
        print("Overhead non")
        exists = 1
        exists_buttons = 1
        list_maker(exists, exists_buttons)
    else:
        exists = 0
        exists_buttons = 0
        list_maker(exists, exists_buttons)
    button_lift()


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#242424")

def load_portfolio():
    if os.path.exists("saved_portfolio.pickle"):
        with open("saved_portfolio.pickle", "rb") as file:
            portfolio = pickle.load(file)
            print("Existing portfolio loaded.")
    else:
        portfolio = stock_portfolio.StockPortfolio()
        print("New portfolio created.")
    
    return portfolio

def save_portfolio(portfolio):
    with open("saved_portfolio.pickle", "wb") as file:
        pickle.dump(portfolio, file)
        print("Portfolio saved.")

def delete_portfolio():
    if os.path.exists("saved_portfolio.pickle"):
        os.remove("saved_portfolio.pickle")
        print("Portfolio deleted.")
    else:
        print("No portfolio found.")

portfolio = load_portfolio()

tkstring_total_value = StringVar()
tkstring_holdings_value = StringVar()

tkstring_total_value.set(portfolio.total_portfolio_value())
tkstring_holdings_value.set(portfolio.holdings_value())

def trigger_buy(a, b):
    buy_stock_order(a, b)


# portfolio.add_stock(stock.Stock("ZOMATO"), 12, 100)
# portfolio.add_stock(stock.Stock("TCS"), 12, 100)

# delete_portfolio()
# save_portfolio(portfolio)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# style = ttk.Style()
# style.layout('TNotebook.Tab',[])
# style.configure('TNotebook', padding=(0,0))
# style.configure('TNotebook', bordercolor='red')

# mainui_notebook = ttk.Notebook(master=window)
# mainui_notebook.pack(fill="both",expand=1)

# dashboard_frame = ttk.Frame(master = mainui_notebook)
# dashboard_frame.pack(fill="both", expand=1)

#Dashboard Canvas

dashboard_canvas = Canvas(
    master=window,
    bg = "#242424",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    
)

dashboard_canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    45.0,
    fill="#3A3A3A",
    outline="")

dashboard_canvas.create_rectangle(
    0.0,
    45.0,
    1280.0,
    90.0,
    fill="#2B2B2B",
    outline="")

dashboard_canvas.create_text(
    470.0,
    3.0,
    anchor="nw",
    text="YOUR PORTFOLIO",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

dashboard_canvas.create_text(
    123.0,
    112.0,
    anchor="nw",
    text="Hello, User",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

dashboard_canvas.create_text(
    190.0,
    480.0,
    anchor="nw",
    text="Holdings",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

dashboard_canvas.create_text(
    120.0,
    550.0,
    anchor="nw",
    text=tkstring_holdings_value.get(),
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

dashboard_canvas.create_rectangle(
    29.0,
    199.0,
    1317.0,
    200.0,
    fill="#5E5E5E",
    outline="")

dashboard_canvas.create_rectangle(
    0.0,
    430.0,
    1288.0,
    431.0,
    fill="#5E5E5E",
    outline="")

dashboard_canvas.create_rectangle(
    24.0,
    645.0,
    1312.0,
    646.0,
    fill="#5E5E5E",
    outline="")

dashboard_canvas.create_text(
    117.0,
    265.0,
    anchor="nw",
    text="Total Investment",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

dashboard_canvas.create_text(
    117.0,
    327.0,
    anchor="nw",
    text=tkstring_total_value.get(),
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

dashboard_canvas.create_rectangle(
    115.0,
    477.0,
    165.0,
    527.0,
    fill="#FFFFFF",
    outline="")

#Holdings Canvas
holdings_canvas = Canvas(
        window,
        bg = "#242424",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

holdings_canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    45.0,
    fill="#3A3A3A",
    outline="")

holdings_canvas.create_rectangle(
    0.0,
    45.0,
    1280.0,
    90.0,
    fill="#2B2B2B",
    outline="")

holdings_canvas.create_text(
    470.0,
    3.0,
    anchor="nw",
    text="YOUR PORTFOLIO",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

#Orders Canvas

orders_canvas = Canvas(
        window,
        bg = "#242424",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

# orders_canvas.place(x = 0, y = 0)
orders_canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    45.0,
    fill="#3A3A3A",
    outline="")

orders_canvas.create_rectangle(
    0.0,
    45.0,
    1280.0,
    90.0,
    fill="#2B2B2B",
    outline="")

orders_canvas.create_text(
    620.0,
    3.0,
    anchor="nw",
    text="ORDERS",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

# orders_canvas.create_text(
#     123.0,
#     112.0,
#     anchor="nw",
#     text="Add Stocks (already purchased)",
#     fill="#FFFFFF",
#     font=("Inter", 34 * -1)
# )

orders_canvas.create_text(
    123.0,
    110.0,
    anchor="nw",
    text="Buy Stocks :   Quantity",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

#Testing Canvas

testing_canvas = Canvas(
        window,
        bg = "#242424",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

# testing_canvas.place(x = 0, y = 0)
testing_canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    45.0,
    fill="#3A3A3A",
    outline="")

testing_canvas.create_rectangle(
    0.0,
    45.0,
    1280.0,
    90.0,
    fill="#2B2B2B",
    outline="")

testing_canvas.create_text(
    470.0,
    3.0,
    anchor="nw",
    text="YOUR PORTFOLIO",
    fill="#FFFFFF",
    font=("Inter", 34 * -1)
)

# Canvas state

current_canvas = dashboard_canvas

# order_list_of_stocks_and_search()



#Buttons
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:change_canvas(holdings_canvas),
    relief="flat",
    background="#242424",
    border=0,
    activebackground="#2C2C2C"
)
button_1.place(
    x=1192.0,
    y=49.0,
    width=86.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas(dashboard_canvas),
    relief="flat",
    activebackground="#2C2C2C"
)
button_2.place(
    x=881.0,
    y=46.0,
    width=156.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas(orders_canvas),
    relief="flat",
    activebackground="#2C2C2C"
)
button_3.place(
    x=1114.0,
    y=48.0,
    width=77.0,
    height=42.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas(testing_canvas),
    relief="flat",
    activebackground="#2C2C2C"
)
button_4.place(
    x=1031.0,
    y=46.0,
    width=85.0,
    height=42.0
)

# if current_canvas == orders_canvas or current_canvas == testing_canvas:
#     exists = 1
#     print("Exist")
# else:
#     exists = 0
#     print("NonExist")

def check(e):
    typed = entry_stock.get()
    if typed == '':
        data = clean_stocks
    else:
        data = []
        for item in clean_stocks:
            if typed.lower() in item.lower():
                data.append(item)
    update_listbox(data)
    

def fillout(e):
    global current_symbol
    entry_stock.delete(0,END)
    entry_stock.insert(0, list_view_stocks.get(ACTIVE))
    current_symbol = list_view_stocks.get(ACTIVE)


def update_listbox(list_of_stocks):
    list_view_stocks.delete(0, END)
    for item in list_of_stocks:
        list_view_stocks.insert(END,item)

entry_stock = Entry()
entry_stock_qty = Entry()


list_of_stocks = list(sqlite_commands.list_of_stocks())
clean_stocks = []
for i in list_of_stocks:
    clean_stocks.append(i[0])
list_view_stocks = Listbox(width=50)
update_listbox(clean_stocks)

list_view_stocks.bind("<<ListboxSelect>>",fillout)
entry_stock.bind("<KeyRelease>",check)

buy_button_orders_image = PhotoImage(
        file=os.path.join("src\\ui\\build\\assets\\frame4\\button_1.png"))
buy_button_orders = Button(
    image=buy_button_orders_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: trigger_buy(list_view_stocks.get(ACTIVE),entry_stock_qty.get()),
    relief="flat",
    activebackground="#2C2C2C"
)

sell_button_orders_image = PhotoImage(
        file=os.path.join("src\\ui\\build\\assets\\frame4\\button_2.png"))
sell_button_orders = Button(
    image=sell_button_orders_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: buysell(list_view_stocks.get(ACTIVE),"sell"),
    relief="flat",
    activebackground="#2C2C2C"
)

def buy_stock_order(symbol, qty):
    price = sqlite_commands.get_current_prices(str(symbol).upper())
    portfolio.add_stock(stock.Stock(symbol),qty,price)
    save_portfolio(portfolio)
    window.update_idletasks()

def list_maker(exists, exists_buttons):
    if exists == 1 and exists_buttons == 0:
        entry_stock.place(x=123, y=175)
        entry_stock_qty.place(x=300, y=175)
        list_view_stocks.place(x = 123, y = 250)
        # test
        buy_button_orders.place(
        x=123.0,
        y=432.0,
        width=116.0,
        height=51.0
        )
        sell_button_orders.place(
        x=263.0,
        y=432.0,
        width=116.0,
        height=51.0
        )
        entry_stock_qty.place_forget()
        buy_button_orders.place_forget()
        sell_button_orders.place_forget()
    
    elif exists == 1 and exists_buttons == 1:
        entry_stock.place(x=123, y=175)
        entry_stock_qty.place(x=300, y=175)
        list_view_stocks.place(x = 123, y = 250)
        buy_button_orders.place(
        x=123.0,
        y=432.0,
        width=116.0,
        height=51.0
        )
        sell_button_orders.place(
        x=263.0,
        y=432.0,
        width=116.0,
        height=51.0
        )
        
    else:
        entry_stock.place_forget()
        entry_stock_qty.place_forget()
        list_view_stocks.place_forget()
        buy_button_orders.place_forget()
        sell_button_orders.place_forget()
        

current_canvas.place(x = 0, y = 0)
# holdings_canvas.place(x = 0, y = 0)
# mainui_notebook.add(canvas)
window.resizable(False, False)
window.mainloop()

