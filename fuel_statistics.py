from tkinter import *
from tkinter import messagebox
import tkinter
from tkcalendar import *
from datetime import date, datetime
from general import *

tanking_history = load_tanking_history()
refuel_count = len(tanking_history)

def refuel_count_this_year():
    current_year = datetime.now().year
    this_year_refuel_counter = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.year == current_year:
            this_year_refuel_counter += 1
    return this_year_refuel_counter

def refuel_count_last_year():
    last_year = (datetime.now().year)-1
    last_year_refuel_counter = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.year == last_year:
            last_year_refuel_counter += 1
    return last_year_refuel_counter

def refuel_count_this_month():
    current_month = datetime.now().month
    this_month_refuel_counter = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.month == current_month:
            this_month_refuel_counter += 1
    return this_month_refuel_counter

def refuel_count_last_month():
    last_month = (datetime.now().month)-1
    last_month_refuel_counter = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.month == last_month:
            last_month_refuel_counter += 1
    return last_month_refuel_counter

def calculate_average_fuel_price():
    total_fuel_price = 0
    total_liters = 0
    first_record = tanking_history[0]
    initial_odometer = first_record["Odometer status"]
    last_record = tanking_history[-1]
    current_odometer = last_record["Odometer status"]

    for record in tanking_history:
        total_fuel_price += record["Refuel total price"]
        total_liters += record["Fuel amount"]
    return total_fuel_price/total_liters

def fuel_statistics_window(content_frame):
    clear_content(content_frame)

    fuel_statistics_label = tkinter.Label(content_frame, text = "Fuel statistics", font = FONT_HEADER)
    fuel_statistics_label.grid(row=0, column=0, columnspan=2, sticky = "w")
    show_fuel_overview(content_frame)
    
    refuel_count_label = tkinter.Label(content_frame, text = "Total refuels count")
    refuel_count_label.grid(row = 8, column = 0, sticky = "w")
    refuel_count_value = tkinter.Label(content_frame, text = refuel_count)
    refuel_count_value.grid(row = 8, column = 1, sticky = "e")

    this_year_refuels_label = tkinter.Label(content_frame, text = "Refuels this year")
    this_year_refuels_label.grid(row = 9, column = 0, sticky = "w")
    this_year_refuels_value = tkinter.Label(content_frame, text = f"{refuel_count_this_year()}")
    this_year_refuels_value.grid(row = 9, column = 1, sticky = "e")

    last_year_refuels_label = tkinter.Label(content_frame, text = "Refuels last year")
    last_year_refuels_label.grid(row = 10, column = 0, sticky = "w")
    last_year_refuels_value = tkinter.Label(content_frame, text = f"{refuel_count_last_year()}")
    last_year_refuels_value.grid(row = 10, column = 1, sticky = "e")

    this_month_refuels_label = tkinter.Label(content_frame, text = "Refuels this month")
    this_month_refuels_label.grid(row =11, column = 0, sticky = "w")
    this_month_refuels_value = tkinter.Label(content_frame, text = f"{refuel_count_this_month()}")
    this_month_refuels_value.grid(row = 11, column = 1, sticky = "e")

    last_month_refuels_label = tkinter.Label(content_frame, text = "Refuels last month")
    last_month_refuels_label.grid(row = 12, column = 0, sticky = "w")
    last_month_refuels_value = tkinter.Label(content_frame, text = f"{refuel_count_last_month()}")
    last_month_refuels_value.grid(row = 12, column = 1, sticky = "e")

    avg_fuel_price_label = tkinter.Label(content_frame, text = "Average fuel price")
    avg_fuel_price_label.grid(row = 13, column = 0, sticky = "w")
    avg_fuel_price_value = tkinter.Label(content_frame, text = f"{calculate_average_fuel_price():.2f} CZK/l")
    avg_fuel_price_value.grid(row = 13, column = 1, sticky = "e")


