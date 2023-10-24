"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "Forest-ttk-theme-master/forest-dark.tcl")
root.geometry("1280x720")
# Set the theme with the theme_use method
style.theme_use("forest-dark")

#Frame
Frame1 = ttk.Button()
Frame1.pack()

# Start the main loop
root.mainloop()
