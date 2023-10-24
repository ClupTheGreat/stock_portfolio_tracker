from pathlib import Path
# from ui.build import dashboard
from ui.build import holdings
from ui.build import orders
from ui.build import testing
from ui.build import buysell

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, ttk
import stock_portfolio
import stock

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Code\tkinter_des\figmatotk\build\assets\frame3")

# Button lift needed, as new canvas is placed on top of it

def button_lift():
    for button in [button_1, button_2, button_3, button_4]:
        button.lift()


# Accessing global variable state in order to hide and place canvas
def change_canvas(next_canvas):
    global current_canvas
    current_canvas.place_forget()
    next_canvas.place(x = 0, y = 0)
    current_canvas = next_canvas
    button_lift()

    

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#242424")

portfolio = stock_portfolio.StockPortfolio()
portfolio.add_stock(stock.Stock("ZOMATO"), 10, 100)

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
    text="1234567",
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
    470.0,
    3.0,
    anchor="nw",
    text="YOUR PORTFOLIO",
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




current_canvas.place(x = 0, y = 0)
# holdings_canvas.place(x = 0, y = 0)
# mainui_notebook.add(canvas)
window.resizable(False, False)
window.mainloop()

