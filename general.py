from tkinter import messagebox, ttk
import tkinter
import json
import os
from datetime import datetime

FONT_HEADER = ("Arial", 12, "bold")
FONT_STANDARD_LABEL = ("Arial", 10, "bold")
FONT_BASIC = ("Arial", 10)
BG_COLOR = "#f4f4f4"

file_path = "tanking_history.json"

def save_tanking_history(tanking_history):
    with open(file_path, 'w') as f:
        json.dump(tanking_history, f, indent=4)

def load_tanking_history():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []  # Return an empty list if the file does not exist

def append_tanking_history(new_entry):
    data = load_tanking_history()  # Load existing data
    data.append(new_entry)  # Append the new entry
    save_tanking_history(data)  # Save updated data

def validate_decimal_input(P):
    # Allow only empty input (for when the entry is cleared)
    if P == "":
        return True
    try:
        # Convert input to a float to check if it's a valid decimal number
        float(P)
        return True
    except ValueError:
        # If conversion to float fails, it's not a valid decimal
        messagebox.showwarning("Invalid Input", "Please enter a valid number.\nWhen entering decimal number, use '.'")
        return False

def clear_content(content_frame):
    # Clears content of the current window
    for widget in content_frame.winfo_children():
        widget.destroy()

def show_fuel_overview(content_frame):
  
    fuel_header_separator = ttk.Separator(content_frame, orient='horizontal')
    fuel_header_separator.grid(row=1, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)
    
    last_avg_consumption_label = tkinter.Label(content_frame, text = "Last consumption")
    last_avg_consumption_label.grid(row=2, column=0, sticky = "w")
    last_avg_consumption_label = tkinter.Label(content_frame, text = f"{calcualate_last_consumption():.2f} l/100 km")
    last_avg_consumption_label.grid(row=2, column=1, sticky = "e")

    avg_consumption_label = tkinter.Label(content_frame, text = "Average consumption")
    avg_consumption_label.grid(row=3, column=0, sticky = "w")
    avg_consumption_label = tkinter.Label(content_frame, text = f"{calculate_avg_consumption():.2f} l/100 km")
    avg_consumption_label.grid(row=3, column=1, sticky = "e")

    tanking_history = load_tanking_history()
    last_refuel_stop = tanking_history[-1]
    last_refuel_date = last_refuel_stop["Refuel date"]
    last_refuel_date_label = tkinter.Label(content_frame, text = "Last refuel")
    last_refuel_date_label.grid(row=4, column=0, sticky = "w")
    last_refuel_date_value_label = tkinter.Label(content_frame, text = f"{last_refuel_date}\n({get_date_diff(last_refuel_date)} days ago)")
    last_refuel_date_value_label.grid(row=4, column = 1, sticky = "e")

    last_fuel_price_label = tkinter.Label(content_frame, text = "Last fuel price")
    last_fuel_price_label.grid(row=5, column=0, sticky = "w")
    last_fuel_price_value_label = tkinter.Label(content_frame, text = f"{get_last_fuel_price():.2f} CZK/l")
    last_fuel_price_value_label.grid(row=5, column=1, sticky = "e")

def show_default(content_frame):
    clear_content(content_frame)
    
    default_fuel_label = tkinter.Label(content_frame, text = "Fuel overview", font = FONT_HEADER)
    default_fuel_label.grid(row=0, column=0, columnspan=2, sticky = "w")
    show_fuel_overview(content_frame)

    from fuel_statistics import fuel_statistics_window

    show_detail_fuel_statistics_button = tkinter.Button(content_frame, text = "Show detail fuel statistics", command = lambda: fuel_statistics_window(content_frame))
    show_detail_fuel_statistics_button.grid(row = 6, column = 1, pady = 2, padx = 2)
    default_info_separator = ttk.Separator(content_frame, orient='horizontal')
    default_info_separator.grid(row=7, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)

def calcualate_last_consumption():
    tanking_history = load_tanking_history()
    last_refuel = tanking_history[-1]
    pre_last_refuel = tanking_history[-2]
    last_fuel_consumption = last_refuel["Fuel amount"]/((last_refuel["Odometer status"])-(pre_last_refuel["Odometer status"]))*100
    return last_fuel_consumption
    
def calculate_avg_consumption():   
    tanking_history = load_tanking_history()
    total_liters = 0
    #total_km = 0
    for refuel_stop in tanking_history:
        if "Fuel amount" in refuel_stop:
            total_liters += refuel_stop["Fuel amount"]
    first_refuel_record = tanking_history[0]
    initial_km = first_refuel_record["Odometer status"]
    latest_refuel_record = tanking_history[-1]
    current_km = latest_refuel_record["Odometer status"]
    total_km = current_km - initial_km
    
    avg_consumption = (total_liters/total_km)*100
    return avg_consumption

def get_last_fuel_price():
    tanking_history = load_tanking_history()
    last_refuel_stop = tanking_history[-1]
    last_refuel_price = last_refuel_stop["Price per liter"]
    return last_refuel_price

def get_date_diff(initial_date):
    date_format = "%d.%m.%Y"  # your date format
    initial_date_obj = datetime.strptime(initial_date, date_format).date()  # Convert to date object
    today = datetime.today().date()  # Get today's date

    # Calculate the difference
    date_difference = (today - initial_date_obj).days 
    return date_difference