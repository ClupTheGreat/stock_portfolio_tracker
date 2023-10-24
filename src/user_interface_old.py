from tkinter import *
from tkinter import ttk

def printhello():
    print("Hello world")

#create a window
window = Tk()
window.title('Stock Portfolio')
window.geometry('1280x720')

#creating a notebook
my_notebook = ttk.Notebook(master=window)
my_notebook.pack(pady=10)

#creating frames
my_frame1 = Frame(master=my_notebook, width=1200, height=720)
my_frame2 = Frame(master=my_notebook, width=1200, height=720)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

#adding frames
my_notebook.add(my_frame1, text="Home")
my_notebook.add(my_frame2, text="Portfolio")

#home page
button1 = ttk.Button(master=my_frame1,text="Game",command=printhello)
button1.pack()

#run
window.mainloop()