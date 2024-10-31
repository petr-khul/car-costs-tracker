import tkinter
from tkinter import Menu, messagebox, ttk
from tkcalendar import *
from datetime import date
from tanking import new_tanking, display_refuel_log  # Assuming you have defined tanking-related functions
from general import load_tanking_history, show_default, validate_decimal_input, BG_COLOR  # Import necessary functions
from fuel_statistics import *
from costs_statistics import *
from costs import *

tanking_history = load_tanking_history() # load the history from json file

# Create the main window
window = tkinter.Tk()
window.title("Car Costs Tracker")
window.geometry("400x500")
window.resizable(False, False)
window.configure(bg = BG_COLOR)

# Crate content frame with dynamic content
content_frame = tkinter.Frame(window, bg = BG_COLOR)
content_frame.pack(fill=tkinter.BOTH, expand=True, pady = 10, padx = 10)
content_frame.option_add("*Background", BG_COLOR) #sets the BG color to all widgets

# Create a menu
menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)

fuel_menu = tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Home", command = lambda: show_default(content_frame))
fuel_menu.add_command(label="Add refuel", command=lambda: new_tanking(content_frame))  # Make sure new_tanking is defined in tanking.py
fuel_menu.add_command(label="Fuel statistics", command = lambda: fuel_statistics_window(content_frame))
fuel_menu.add_command(label="Fuel log", command = lambda: display_refuel_log(content_frame))
menu_bar.add_cascade(label="Fuel", menu=fuel_menu)

costs_menu = tkinter.Menu(menu_bar, tearoff=0)
costs_menu.add_command(label="Add cost", command = lambda: new_costs(content_frame))
costs_menu.add_command(label="Cost statistics", command = lambda: costs_statistics_window(content_frame))
menu_bar.add_cascade(label="Costs", menu=costs_menu)

# Register validation function for input
vcmd = (content_frame.register(validate_decimal_input), '%P')

show_default(content_frame)  # Show the default page in the application

window.mainloop()