from tkinter import messagebox
import tkinter
import json
import os

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
    tanking_history = load_tanking_history()
    if tanking_history:  # Check if there are any entries
        last_refuel_stop = tanking_history[-1]
        last_refuel_stop_odometer = last_refuel_stop["Odometer status"]
        last_refuel_stop_odometer_label = tkinter.Label(content_frame, text=last_refuel_stop_odometer)
        last_refuel_stop_odometer_label.grid(row=0, column=0)
    else:
        # If no history, you can add a label indicating so
        no_data_label = tkinter.Label(content_frame, text="No tanking history available.")
        no_data_label.grid(row=0, column=0)
