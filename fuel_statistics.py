from tkinter import *
from tkinter import messagebox
import tkinter
from tkcalendar import *
from datetime import date, datetime
from general import *

tanking_history = load_tanking_history()
refuel_count = len(tanking_history)

def get_total_fuel_price():
    total_fuel_costs = 0
    for record in tanking_history:
        total_fuel_costs += record["Refuel total price"]
    return total_fuel_costs

def refuel_count_this_year():
    current_year = datetime.now().year
    this_year_refuel_counter = 0
    this_year_costs = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.year == current_year:
            this_year_refuel_counter += 1
            this_year_costs += record["Refuel total price"]
    return this_year_refuel_counter, this_year_costs

def refuel_count_last_year():
    last_year = (datetime.now().year)-1
    last_year_refuel_counter = 0
    last_year_costs = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.year == last_year:
            last_year_refuel_counter += 1
            last_year_costs += record["Refuel total price"]
    return last_year_refuel_counter, last_year_costs

def refuel_count_this_month():
    current_month = datetime.now().month
    current_year = datetime.now().year
    this_month_refuel_counter = 0
    this_month_costs = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.month == current_month and refuel_date.year == current_year:
            this_month_refuel_counter += 1
            this_month_costs += record["Refuel total price"]            
    return this_month_refuel_counter, this_month_costs

def refuel_count_last_month():
    last_month = (datetime.now().month)-1
    last_month_refuel_counter = 0
    last_month_costs = 0

    for record in tanking_history:
        refuel_date = datetime.strptime(record["Refuel date"], "%d.%m.%Y")
        if refuel_date.month == last_month:
            last_month_refuel_counter += 1
            last_month_costs += record["Refuel total price"]
    return last_month_refuel_counter, last_month_costs

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

def get_max_min_fuel_values():
    max_price_per_liter = float("-inf")
    min_price_per_liter = float("inf")
    max_refuel_amount = float("-inf")
    min_refuel_amount = float("inf")
    max_refuel_price = 0
    min_refuel_price = 0

    for record in tanking_history:
        # Update max and min for price per liter
        if record["Price per liter"] > max_price_per_liter:
            max_price_per_liter = record["Price per liter"]
        if record["Price per liter"] < min_price_per_liter:
            min_price_per_liter = record["Price per liter"]
        
        # Update max and min for fuel amount
        if record["Fuel amount"] > max_refuel_amount:
            max_refuel_amount = record["Fuel amount"]
            max_refuel_price = record["Refuel total price"]
        if record["Fuel amount"] < min_refuel_amount:
            min_refuel_amount = record["Fuel amount"]
            min_refuel_price = record["Refuel total price"]
    
    return max_price_per_liter, min_price_per_liter, max_refuel_amount, min_refuel_amount, max_refuel_price, min_refuel_price

def fuel_statistics_window(content_frame):
    clear_content(content_frame)

    fuel_statistics_label = tkinter.Label(content_frame, text = "Fuel statistics", font = FONT_HEADER)
    fuel_statistics_label.grid(row=0, column=0, columnspan=2, sticky = "w")
    show_fuel_overview(content_frame)

    avg_fuel_price_label = tkinter.Label(content_frame, text = "Average fuel price")
    avg_fuel_price_label.grid(row = 8, column = 0, sticky = "w")
    avg_fuel_price_value = tkinter.Label(content_frame, text = f"{calculate_average_fuel_price():.2f} CZK/l")
    avg_fuel_price_value.grid(row = 8, column = 1, sticky = "e")

    max_fuel_price, min_fuel_price, max_refuel, min_refuel, max_refuel_price, min_refuel_price = get_max_min_fuel_values()

    max_fuel_price_label = tkinter.Label(content_frame, text = "Maximal fuel price")
    max_fuel_price_label.grid(row = 9, column = 0, sticky = "w")
    max_fuel_price_value = tkinter.Label(content_frame, text = f"{max_fuel_price:.2f} CZK/l")
    max_fuel_price_value.grid(row = 9, column = 1, sticky = "e")

    min_fuel_price_label = tkinter.Label(content_frame, text = "Minimum fuel price")
    min_fuel_price_label.grid(row = 10, column = 0, sticky = "w")
    min_fuel_price_value = tkinter.Label(content_frame, text = f"{min_fuel_price:.2f} CZK/l")
    min_fuel_price_value.grid(row = 10, column = 1, sticky = "e")

    fuel_separator = ttk.Separator(content_frame, orient='horizontal')
    fuel_separator.grid(row=13, column=0, columnspan = 3, sticky="ew", padx=5, pady=5)
    
    refuel_count_label = tkinter.Label(content_frame, text = "Total refuels count")
    refuel_count_label.grid(row = 14, column = 0, sticky = "w")
    refuel_count_value = tkinter.Label(content_frame, text = refuel_count)
    refuel_count_value.grid(row = 14, column = 1, sticky = "ew")
    total_refuels_price_value = tkinter.Label(content_frame, text = f"Total {get_total_fuel_price():.1f} CZK")
    total_refuels_price_value.grid(row = 14, column = 2, sticky = "e")

    this_year_count, this_year_total = refuel_count_this_year()
    this_year_refuels_label = tkinter.Label(content_frame, text = "Refuels this year")
    this_year_refuels_label.grid(row = 15, column = 0, sticky = "w")
    this_year_refuels_value = tkinter.Label(content_frame, text = f"{this_year_count}")
    this_year_refuels_value.grid(row = 15, column = 1, sticky = "ew")
    this_year_refuels_price_value = tkinter.Label(content_frame, text = f"Total {this_year_total} CZK")
    this_year_refuels_price_value.grid(row = 15, column = 2, sticky = "e")

    last_year_count, last_year_total = refuel_count_last_year()
    last_year_refuels_label = tkinter.Label(content_frame, text = "Refuels last year")
    last_year_refuels_label.grid(row = 16, column = 0, sticky = "w")
    last_year_refuels_value = tkinter.Label(content_frame, text = f"{last_year_count}")
    last_year_refuels_value.grid(row = 16, column = 1, sticky = "ew")
    last_year_refuels_price_value = tkinter.Label(content_frame, text = f"Total {last_year_total} CZK")
    last_year_refuels_price_value.grid(row = 16, column = 2, sticky = "e")

    this_month_count, this_month_total = refuel_count_this_month()
    this_month_refuels_label = tkinter.Label(content_frame, text = "Refuels this month")
    this_month_refuels_label.grid(row = 17, column = 0, sticky = "w")
    this_month_refuels_value = tkinter.Label(content_frame, text = f"{this_month_count}")
    this_month_refuels_value.grid(row = 17, column = 1, sticky = "ew")
    this_month_refuels_price_value = tkinter.Label(content_frame, text = f"Total {this_month_total} CZK")
    this_month_refuels_price_value.grid(row = 17, column = 2, sticky = "e")

    last_month_count, last_month_total = refuel_count_last_month()
    last_month_refuels_label = tkinter.Label(content_frame, text = "Refuels last month")
    last_month_refuels_label.grid(row = 18, column = 0, sticky = "w")
    last_month_refuels_value = tkinter.Label(content_frame, text = f"{last_month_count}")
    last_month_refuels_value.grid(row = 18, column = 1, sticky = "ew")
    last_month_refuels_price_value = tkinter.Label(content_frame, text = f"Total {last_month_total} CZK")
    last_month_refuels_price_value.grid(row = 18, column = 2, sticky = "e")

    fuel_separator2 = ttk.Separator(content_frame, orient='horizontal')
    fuel_separator2.grid(row=19, column=0, columnspan = 3, sticky="ew", padx=5, pady=5)

    max_fuel_amount_label = tkinter.Label(content_frame, text = "Maximum refuel")
    max_fuel_amount_label.grid(row = 20, column = 0, sticky = "w")
    max_fuel_amount_value = tkinter.Label(content_frame, text = f"{max_refuel:.2f} l")
    max_fuel_amount_value.grid(row = 20, column = 1, sticky = "e")
    max_fuel_amount_price_value = tkinter.Label(content_frame, text = f"Total {max_refuel_price:.2f} CZK")
    max_fuel_amount_price_value.grid(row = 20, column = 2, sticky = "e")

    min_fuel_amount_label = tkinter.Label(content_frame, text = "Minimum refuel")
    min_fuel_amount_label.grid(row = 21, column = 0, sticky = "w")
    min_fuel_amount_value = tkinter.Label(content_frame, text = f"{min_refuel:.2f} l")
    min_fuel_amount_value.grid(row = 21, column = 1, sticky = "e")
    min_fuel_amount_price_value = tkinter.Label(content_frame, text = f"Total {min_refuel_price:.2f} CZK")
    min_fuel_amount_price_value.grid(row = 21, column = 2, sticky = "e")



