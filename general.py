from tkinter import messagebox
import tkinter
import json
import os
from statistics import *

FONT_HEADER = ("Arial", 12, "bold")
FONT_STANDARD_LABEL = ("Arial", 10, "bold")
FONT_BASIC = ("Arial", 10)
BG_COLOR = "#808080"

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

def show_default(content_frame):
    clear_content(content_frame)
    #tanking_history = load_tanking_history()
    default_fuel_label = tkinter.Label(content_frame, text = "Fuel overview", font = FONT_HEADER)
    default_fuel_label.grid(row=0, column=0, columnspan=2, sticky = "w")
    
    last_avg_consumption_label = tkinter.Label(content_frame, text = "Last consumption")
    last_avg_consumption_label.grid(row=1, column=0, sticky = "w")
    last_avg_consumption_label = tkinter.Label(content_frame, text = f"{calcualate_last_consumption():.2f} l/km")
    last_avg_consumption_label.grid(row=1, column=1, sticky = "e")

    avg_consumption_label = tkinter.Label(content_frame, text = "Average consumption")
    avg_consumption_label.grid(row=2, column=0, sticky = "w")
    avg_consumption_label = tkinter.Label(content_frame, text = f"{calculate_avg_consumption():.2f} l/km")
    avg_consumption_label.grid(row=2, column=1, sticky = "e")

    #if tanking_history:  # Check if there are any entries
        #last_refuel_stop = tanking_history[-1]
        #last_refuel_stop_odometer = last_refuel_stop["Odometer status"]
        #last_refuel_stop_odometer_label = tkinter.Label(content_frame, text=fuel_statitics)
        #last_refuel_stop_odometer_label.grid(row=0, column=0)
    #else:
        # If no history, you can add a label indicating so
        #no_data_label = tkinter.Label(content_frame, text="No tanking history available.")
        #no_data_label.grid(row=0, column=0)

def calcualate_last_consumption():
    tanking_history = load_tanking_history()
    last_refuel = tanking_history[-1]
    pre_last_refuel = tanking_history[-2]
    last_fuel_consumption = (last_refuel["Fuel amount"]/(last_refuel["Odometer status"]-pre_last_refuel["Odometer status"])*100)
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