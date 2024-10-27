import tkinter
from tkinter import Menu, messagebox
from tkcalendar import *
from datetime import date
import json, os
from tanking import new_tanking  # Assuming you have defined tanking-related functions
from general import load_tanking_history, show_default, validate_decimal_input, BG_COLOR  # Import necessary functions
from statistics import *

tanking_history = load_tanking_history()

# Create the main window
window = tkinter.Tk()
window.title("Car Costs Tracker")
window.geometry("400x500")

content_frame = tkinter.Frame(window, bg = BG_COLOR)
content_frame.grid(row=0, column=0, padx=10, pady=10)
#content_frame.option_add("*Background", BG_COLOR) #sets the BG color to all widgets

# Create a menu
menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)
window.configure(bg = BG_COLOR)

fuel_menu = tkinter.Menu(menu_bar, tearoff=0)
fuel_menu.add_command(label="Add refuel", command=lambda: new_tanking(content_frame))  # Make sure new_tanking is defined in tanking.py
fuel_menu.add_command(label="Fuel statistics")
menu_bar.add_cascade(label="Fuel", menu=fuel_menu)

costs_menu = tkinter.Menu(menu_bar, tearoff=0)
costs_menu.add_command(label="New cost")
costs_menu.add_command(label="Cost statistics")
menu_bar.add_cascade(label="Costs", menu=costs_menu)

#service_menu = tkinter.Menu(menu_bar, tearoff=0)
#service_menu.add_command(label="New service")
#service_menu.add_command(label="Service statistics")
#menu_bar.add_cascade(label="Service", menu=service_menu)

# Register validation function for input
vcmd = (content_frame.register(validate_decimal_input), '%P')

show_default(content_frame)  # Show the default page in the application

window.mainloop()
