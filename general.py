from tkinter import messagebox, ttk
import tkinter
import json
import os
from datetime import datetime

FONT_HEADER = ("Arial", 10, "bold")
FONT_STANDARD_LABEL = ("Arial", 10)
FONT_BASIC = ("Arial", 10)
BG_COLOR = "white"

file_path = "tanking_history.json"
file_path_costs = "costs_history.json"

# -------------- Handling costs history file -----------------------
def save_costs_history(costs_history):
    with open(file_path_costs, 'w') as f2:
        json.dump(costs_history, f2, indent=4)

def load_costs_history():
    if os.path.exists(file_path_costs):
        with open(file_path_costs, 'r') as f2:
            try:
                data = json.load(f2)
                # Sort the list of entries by 'Odometer status'
                data.sort(key=lambda x: x['Odometer status'])
                return data
            except json.JSONDecodeError:
                print("Warning: file is empty or has invalid JSON, returning an empty list.")
                return []
    return []        

def append_costs_history(new_cost_entry):
    data = load_costs_history()  # Load existing data
    data.append(new_cost_entry)  # Append the new entry
    data.sort(key=lambda x: x['Odometer status'])
    save_costs_history(data)  # Save sorted data

# -------------- Handling tanking history file -----------------------
def save_tanking_history(tanking_history):
    with open(file_path, 'w') as f:
        json.dump(tanking_history, f, indent=4)

def load_tanking_history():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                #messagebox.showerror("Unable to load data", "Unable to load data from tanking history! :(")
                return []  # Return an empty list if the file does not exist
    return []

def append_tanking_history(new_entry):
    data = load_tanking_history()  # Load existing data
    data.append(new_entry)  # Append the new entry
    save_tanking_history(data)  # Save updated data

def validate_decimal_input(P): # Allow only empty input (for when the entry is cleared)
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

# function to remove all widget to refresh the window
def clear_content(content_frame):
    # Clears content of the current window
    for widget in content_frame.winfo_children():
        widget.destroy()

# window for showing fuel overview
def show_fuel_overview(content_frame):
    tanking_history = load_tanking_history()
    if tanking_history:
        if len(tanking_history) > 0 and len(tanking_history)<=2: #return temporary empty records for follwoing functions to work
            last_refuel = [
                    {
                    "Odometer status": 0,
                    "Fuel type": " ",
                    "Fuel amount": 0,
                    "Refuel total price": 0,
                    "Price per liter": 0,
                    "Refuel date": " ",
                    "Tank full": False,
                    "Gas station": " ",
                    "Refuel note": "\n"
                },
                {
                "Odometer status": 0,
                    "Fuel type": " ",
                    "Fuel amount": 0,
                    "Refuel total price": 0,
                    "Price per liter": 0,
                    "Refuel date": " ",
                    "Tank full": False,
                    "Gas station": " ",
                    "Refuel note": "\n"
                },
            ]
        else:
            last_refuel = tanking_history[-1]
    else:
        print("No refuel history available")

    # ------------------------ General fuel ovirview widgets -------------------------------------------------------
    #fuel_header_separator = ttk.Separator(content_frame, orient='horizontal')
    #fuel_header_separator.grid(row=1, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)

    last_refuel = tanking_history[-1]
    last_odometer_status = last_refuel["Odometer status"]
    last_odometer_status_label = tkinter.Label(content_frame, text="Last odometer status")
    last_odometer_status_label.grid(row = 2, column = 0, sticky = "w")
    last_odometer_status_value = tkinter.Label(content_frame, text=f"{last_odometer_status:.0f} km")
    last_odometer_status_value.grid(row = 2, column = 1, sticky = "e")
    
    last_avg_consumption_label = tkinter.Label(content_frame, text = "Last consumption")
    last_avg_consumption_label.grid(row=3, column=0, sticky = "w")
    last_avg_consumption_label = tkinter.Label(content_frame, text = f"{calcualate_last_consumption():.2f} l/100 km")
    last_avg_consumption_label.grid(row=3, column=1, sticky = "e")
    if calcualate_last_consumption() <= calculate_avg_consumption():
        last_avg_consumption_label.config(fg = "green")
    elif last_refuel["Tank full"] == False:
        last_avg_consumption_label.config(text = "Unknown", fg = "grey")
    else: 
        last_avg_consumption_label.config(fg = "red")

    avg_consumption_label = tkinter.Label(content_frame, text = "Average consumption")
    avg_consumption_label.grid(row=4, column=0, sticky = "w")
    avg_consumption_label = tkinter.Label(content_frame, text = f"{calculate_avg_consumption():.2f} l/100 km")
    avg_consumption_label.grid(row=4, column=1, sticky = "e")
 
    last_refuel_stop = tanking_history[-1]
    last_refuel_date = last_refuel_stop["Refuel date"]
    last_refuel_date_label = tkinter.Label(content_frame, text = "Last refuel")
    last_refuel_date_label.grid(row=5, column=0, sticky = "w")
    last_refuel_date_value_label = tkinter.Label(content_frame, text = f"{last_refuel_date}\n({get_date_diff(last_refuel_date)} days ago)")
    last_refuel_date_value_label.grid(row=5, column = 1, sticky = "e")

    last_fuel_price_label = tkinter.Label(content_frame, text = "Last fuel price")
    last_fuel_price_label.grid(row=6, column=0, sticky = "w")
    last_fuel_price_value_label = tkinter.Label(content_frame, text = f"{get_last_fuel_price():.2f} CZK/l")
    last_fuel_price_value_label.grid(row=6, column=1, sticky = "e")
    from fuel_statistics import calculate_average_fuel_price
    if get_last_fuel_price() <= calculate_average_fuel_price():
        last_fuel_price_value_label.config(fg = "green")
    else: 
        last_fuel_price_value_label.config(fg = "red")

# function to show default content
def show_default(content_frame):
    clear_content(content_frame)
    
    default_fuel_label = tkinter.Label(content_frame, text = "Fuel overview", font = FONT_HEADER)
    default_fuel_label.grid(row=0, column=0, columnspan=2, sticky = "w")
    show_fuel_overview(content_frame)

    from fuel_statistics import fuel_statistics_window, get_total_fuel_price

    show_detail_fuel_statistics_button = tkinter.Button(content_frame, text = "Show detail fuel statistics", command = lambda: fuel_statistics_window(content_frame))
    show_detail_fuel_statistics_button.grid(row = 7, column = 1, pady = 2, padx = 2)
    
    default_info_separator = ttk.Separator(content_frame, orient='horizontal')
    default_info_separator.grid(row=8, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)
    
    # ------------ costs overview ----------------------------------
    default_costs_overview_label = tkinter.Label(content_frame, text = "Costs overview", font = FONT_HEADER)
    default_costs_overview_label.grid(row=9, column=0, columnspan=2, sticky = "w")

    from costs_statistics import calculate_total_costs, calculate_costs_this_year, costs_statistics_window

    total_costs = calculate_total_costs()
    total_costs_overview_label = tkinter.Label(content_frame, text = "Total costs")
    total_costs_overview_label.grid(row= 11, column=0, sticky = "w")
    total_costs_overview_value = tkinter.Label(content_frame, text = f"{total_costs:.2f} CZK")
    total_costs_overview_value.grid(row= 11, column=1, sticky = "e")

    yearly_costs = calculate_costs_this_year()
    yearly_costs_overview_label = tkinter.Label(content_frame, text = "Costs this year")
    yearly_costs_overview_label.grid(row= 12, column=0, sticky = "w")
    yearly_costs_overview_value = tkinter.Label(content_frame, text = f"{yearly_costs:.2f} CZK")
    yearly_costs_overview_value.grid(row= 12, column=1, sticky = "e")

    show_detail_costs_statistics_button = tkinter.Button(content_frame, text = "Show detail costs statistics", command = lambda: costs_statistics_window(content_frame))
    show_detail_costs_statistics_button.grid(row = 13, column = 1, pady = 2, padx = 2)

    below_costs_separator = ttk.Separator(content_frame, orient='horizontal')
    below_costs_separator.grid(row=14, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)

    # --------------------------- Total expenses ---------------------------------------------
    default_expenses_overview_label = tkinter.Label(content_frame, text = "Total expenses overview", font = FONT_HEADER)
    default_expenses_overview_label.grid(row=15, column=0, columnspan=2, sticky = "w")
    
    total_expense = calculate_total_costs() + get_total_fuel_price()
    total_expenses_label = tkinter.Label(content_frame, text = "Total expenses")
    total_expenses_label.grid(row=16, column=0, sticky= "w")
    total_expenses_value = tkinter.Label(content_frame, text = f"{total_expense:.2f} CZK")
    total_expenses_value.grid(row=16, column=1, sticky="e")

    total_km = odometer_total()
    total_km_label = tkinter.Label(content_frame, text = "Total kilometers")
    total_km_label.grid(row=17, column=0, sticky= "w")
    total_km_value = tkinter.Label(content_frame, text = f"{total_km:.1f} km")
    total_km_value.grid(row=17, column=1, sticky="e")

    avg_expense_per_km = total_expense/total_km
    avg_expense_km_label = tkinter.Label(content_frame, text = "Average expense per km")
    avg_expense_km_label.grid(row=18, column=0, sticky= "w")
    avg_expense_km_value = tkinter.Label(content_frame, text = f"{avg_expense_per_km:.2f} CZK/km")
    avg_expense_km_value.grid(row=18, column=1, sticky="e")

    avg_expense_per_month = total_expense/float(get_date_diff_months())
    avg_expense_per_month_label = tkinter.Label(content_frame, text = "Average expense per month")
    avg_expense_per_month_label.grid(row=19, column=0, sticky= "w")
    avg_expense_per_month_value = tkinter.Label(content_frame, text = f"{avg_expense_per_month:.2f} CZK")
    avg_expense_per_month_value.grid(row=19, column=1, sticky="e")


# returns total distance
def odometer_total():
    tanking_history = load_tanking_history()
    costs_history = load_costs_history()
    min_odo_tanking = min(tanking_history, key=lambda x: x["Odometer status"])
    max_odo_tanking = max(tanking_history, key=lambda x: x["Odometer status"])
    min_odo_costs = min(costs_history, key=lambda x: x["Odometer status"])
    max_odo_costs = max(costs_history, key=lambda x: x["Odometer status"])


    min_odo = 0
    max_odo = 0

    min_odo = min(min_odo_tanking["Odometer status"], min_odo_costs["Odometer status"])
    max_odo = max(max_odo_tanking["Odometer status"], max_odo_costs["Odometer status"])
    
    total_km = max_odo - min_odo
    
    return total_km

# calculates last consumption on last refuel
def calcualate_last_consumption():
    tanking_history = load_tanking_history()
    if len(tanking_history) < 2:
        last_refuel = {}
    else:
        last_refuel = tanking_history[-1]
        pre_last_refuel = tanking_history[-2]
    if "Tank full" in last_refuel:
        if last_refuel["Tank full"] == False:
            return 0
        else:
            last_fuel_consumption = last_refuel["Fuel amount"]/((last_refuel["Odometer status"])-(pre_last_refuel["Odometer status"]))*100
            return last_fuel_consumption
    
# calculates average consumption on all refuels
def calculate_avg_consumption():   
    tanking_history = load_tanking_history()
    total_liters = 0
    #total_km = 0
    for refuel_stop in tanking_history:
        if refuel_stop.get("Fuel amount"):    
            total_liters += refuel_stop["Fuel amount"]
    first_refuel_record = tanking_history[0]
    initial_km = first_refuel_record["Odometer status"]
    latest_refuel_record = tanking_history[-1]
    current_km = latest_refuel_record["Odometer status"]
    total_km = current_km - initial_km
    
    if total_km > 0:
        avg_consumption = (total_liters/total_km)*100
        return avg_consumption
    else:
        return 0
    
# returns last price per liter for fuel
def get_last_fuel_price():
    tanking_history = load_tanking_history()
    last_refuel_stop = tanking_history[-1]
    last_refuel_price = last_refuel_stop["Price per liter"]
    return last_refuel_price

# calculates difference between two dates
def get_date_diff(initial_date): 
    date_format = "%d.%m.%Y"  # your date format
    initial_date_obj = datetime.strptime(initial_date, date_format).date()  # Convert to date object
    today = datetime.today().date()  # Get today's date

    # Calculate the difference
    date_difference = (today - initial_date_obj).days
    return date_difference

def get_date_diff_months():
    tanking_history = load_tanking_history()
    costs_history = load_costs_history()

    # Find the minimum date strings
    min_date_tanking = min(tanking_history, key=lambda x: x["Refuel date"])["Refuel date"]
    min_date_costs = min(costs_history, key=lambda x: x["Cost date"])["Cost date"]

    # Convert date strings to date objects
    date_format = "%d.%m.%Y"
    min_date_tanking = datetime.strptime(min_date_tanking, date_format).date()
    min_date_costs = datetime.strptime(min_date_costs, date_format).date()

    # Find the earliest of the two dates
    min_date = min(min_date_tanking, min_date_costs)

    today = datetime.today().date()  # Get today's date

    # Calculate difference in months and years
    years_diff = today.year - min_date.year
    months_diff = today.month - min_date.month

    # Adjust months if necessary
    if months_diff < 0:
        years_diff -= 1
        months_diff += 12

    date_difference_months = years_diff * 12 + months_diff
    return date_difference_months