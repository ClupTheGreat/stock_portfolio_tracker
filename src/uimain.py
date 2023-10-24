from pathlib import Path
# from ui.build import dashboard
from ui.build import holdings
from ui.build import orders
from ui.build import testing
from ui.build import buysell

from tkinter import *
import stock_portfolio
import stock
import sqlite_commands
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Code\tkinter_des\figmatotk\build\assets\frame3")

# Button lift needed, as new canvas is placed on top of it

def button_lift():
    for button in [button_1, button_2, button_3, button_4]:
        button.lift()


# Accessing global variable state in order to hide and place canvas
def change_canvas(next_canvas):
    exists = 0
    global current_canvas
    global testing_canvas
    global orders_canvas
    current_canvas.place_forget()
    next_canvas.place(x = 0, y = 0)
    current_canvas = next_canvas
    if current_canvas == testing_canvas or current_canvas == orders_canvas:
        exists = 1
        print(exists)
        list_maker(exists)
    else:
        print("Overhead non")
        exists = 0
        list_maker(exists)
    button_lift()

    

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#242424")

portfolio = stock_portfolio.StockPortfolio()
portfolio.add_stock(stock.Stock("ZOMATO"), 12, 100)
portfolio.add_stock(stock.Stock("TCS"), 12, 100)
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
    text=portfolio.holdings_value(),
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
    text=portfolio.total_portfolio_value(),
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

buy_button_orders_image = PhotoImage(
        file=os.path.join("src\\ui\\build\\assets\\frame4\\button_1.png"))
buy_button_orders = Button(
    image=buy_button_orders_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    activebackground="#2C2C2C"
)

sell_button_orders_image = PhotoImage(
        file=os.path.join("src\\ui\\build\\assets\\frame4\\button_2.png"))
sell_button_orders = Button(
    image=sell_button_orders_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    activebackground="#2C2C2C"
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
    text="Buy Stocks",
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
    entry_stock.delete(0,END)
    entry_stock.insert(0, list_view_stocks.get(ACTIVE))


def update_listbox(list_of_stocks):
    list_view_stocks.delete(0, END)
    for item in list_of_stocks:
        list_view_stocks.insert(END,item)

entry_stock = Entry()


list_of_stocks = list(sqlite_commands.list_of_stocks())
clean_stocks = []
for i in list_of_stocks:
    clean_stocks.append(i[0])
list_view_stocks = Listbox(width=50)
update_listbox(clean_stocks)

list_view_stocks.bind("<<ListboxSelect>>",fillout)
entry_stock.bind("<KeyRelease>",check)


def list_maker(exists):
    if exists == 1:
        entry_stock.place(x=123, y=175)
        list_view_stocks.place(x = 123, y = 250)
        # It works because I placed it at the correct spot
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
        list_view_stocks.place_forget()
        buy_button_orders.place_forget()
        sell_button_orders.place_forget()
        
        

current_canvas.place(x = 0, y = 0)
# holdings_canvas.place(x = 0, y = 0)
# mainui_notebook.add(canvas)
window.resizable(False, False)
window.mainloop()

