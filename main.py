import tkinter
from tkinter import Menu, messagebox
from tkcalendar import *
from datetime import date
import json, os

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


FONT_HEADER = ("Arial", 12, "bold")
FONT_STANDARD_LABEL = ("Arial", 10, "bold")
FONT_BASIC = ("Arial", 10)
BG_COLOR = "#808080"

tanking_history = load_tanking_history()

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

def clear_content():
    #Clears content of the current window
    for widget in content_frame.winfo_children():
        widget.destroy()
    
def show_default():
    clear_content()
    tanking_history = load_tanking_history()
    last_refuel_stop = tanking_history[-1]
    last_refuel_stop_odometer = last_refuel_stop["Odometer status"]
    last_refuel_stop_odometer_label = tkinter.Label(content_frame, text = last_refuel_stop_odometer)
    last_refuel_stop_odometer_label.grid(row = 0, column = 0)

def new_tanking():
    clear_content() # Will refresh the window to enable new widgets

    def add_tanking_record():
        
        tanking_history = load_tanking_history()
        last_refuel_stop = tanking_history[-1]
        last_odometer_status = last_refuel_stop["Odometer status"]
        odometer_status = float(odometer_entry.get())
        if odometer_status < last_odometer_status:
            messagebox.showwarning("Invalid Input", "New odometer value cannot be lower than last one.")
            return
        fuel_type = selected_fuel_type.get()
        fuel_amount = float(fuel_amount_entry.get())
        refuel_total_price = float(refuel_price_entry.get())
        price_per_liter = refuel_total_price/fuel_amount
        refuel_date = refuel_date_entry.get()
        tank_full_value = tank_full.get()
        previous_refuelling_missing_value = previous_refuelling_missing.get()
        gas_station = gas_station_entry.get()
        refuel_note = refuel_note_entry.get("1.0", tkinter.END)

        #print(odometer_status, fuel_type, fuel_amount, refuel_price, refuel_date, tank_full_value, previous_refuelling_missing_value, gas_station, refuel_note)

        refuel_record = {
            "Odometer status" : odometer_status, 
            "Fuel type" : fuel_type, 
            "Fuel amount" : fuel_amount, 
            "Refuel total price" : refuel_total_price,
            "Price per liter" : price_per_liter, 
            "Refuel date" : refuel_date, 
            "Tank full" : tank_full_value, 
            "Previous_refuelling_missing" : previous_refuelling_missing_value, 
            "Gas station" : gas_station, 
            "Refuel note" : refuel_note
        }

        append_tanking_history(refuel_record)
        clear_content()
        show_default()
        print(tanking_history)
   
    
    new_tanking_label = tkinter.Label(content_frame, text = "ADD NEW REFUEL STOP", font = FONT_HEADER)
    new_tanking_label.grid(row = 0, column = 0, columnspan = 2, sticky = "w", padx = 10, pady = 10)
    
    odometer_label = tkinter.Label(content_frame, text = "Odometer status", font = FONT_STANDARD_LABEL)
    odometer_label.grid(row = 1, column= 0, pady = 2, padx = 10, sticky = "w")
    odometer_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC, validate = "key", validatecommand=vcmd)
    #odometer_entry.insert(0, last_odometer_status, fg = "lightgrey")
    odometer_entry.grid(row = 1, column = 1, pady = 2, padx = 10)

    fuel_type_label = tkinter.Label(content_frame, text = "Fuel type", font = FONT_STANDARD_LABEL)
    fuel_type_label.grid(row = 2, column= 0, pady = 2, padx = 10, sticky = "w")
    fuel_type_dropdown_options = ["Natural 95", "Natural 95+", "Diesel", "Diesel +", "Ethanol"]
    selected_fuel_type = tkinter.StringVar()
    selected_fuel_type.set("Select the fuel type")
    fuel_type_dropdown = tkinter.OptionMenu(content_frame, selected_fuel_type, *fuel_type_dropdown_options)
    fuel_type_dropdown.config(width = 25)
    fuel_type_dropdown.grid(row = 2, column = 1, pady = 2, padx = 2)

    fuel_amount_label = tkinter.Label(content_frame, text = "Amount of fuel", font = FONT_STANDARD_LABEL)
    fuel_amount_label.grid(row = 3, column= 0, pady = 2, padx = 10, sticky = "w")
    fuel_amount_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC, validate = "key", validatecommand=vcmd)
    fuel_amount_entry.grid(row = 3, column = 1, pady = 2, padx = 2)

    refuel_price_label = tkinter.Label(content_frame, text = "Refuel price", font = FONT_STANDARD_LABEL)
    refuel_price_label.grid(row = 4, column= 0, pady = 2, padx = 10, sticky = "w")
    refuel_price_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC, validate = "key", validatecommand=vcmd)
    refuel_price_entry.grid(row = 4, column = 1, pady = 2, padx = 2)

    refuel_date_label = tkinter.Label(content_frame, text = "Date", font = FONT_STANDARD_LABEL)
    refuel_date_label.grid(row = 5, column= 0, pady = 2, padx = 10, sticky = "w")
    refuel_date_entry = DateEntry(content_frame, selectmode = "day", date_pattern = "dd.mm.yyyy")
    refuel_date_entry.config(width = 25)
    refuel_date_entry.grid(row = 5, column= 1, pady = 2, padx = 10, sticky = "w")

    tank_full_label = tkinter.Label(content_frame, text = "Full tank", font = FONT_STANDARD_LABEL)
    tank_full_label.grid(row = 6, column= 0, pady = 2, padx = 10, sticky = "w")
    tank_full = tkinter.BooleanVar()
    tank_full_checkbox = tkinter.Checkbutton(content_frame, text = "", variable = tank_full)
    tank_full_checkbox.grid(row = 6, column= 1, pady = 2, padx = 10, sticky = "w") 

    previous_refuelling_missing_label = tkinter.Label(content_frame, text = "Previous missing", font = FONT_STANDARD_LABEL)
    previous_refuelling_missing_label.grid(row = 7, column= 0, pady = 2, padx = 10, sticky = "w")
    previous_refuelling_missing = tkinter.BooleanVar()
    previous_refuelling_missing_checkbox = tkinter.Checkbutton(content_frame, text = "", variable = previous_refuelling_missing)
    previous_refuelling_missing_checkbox.grid(row = 7, column= 1, pady = 2, padx = 10, sticky = "w") 

    gas_station_label = tkinter.Label(content_frame, text = "Gas station", font = FONT_STANDARD_LABEL)
    gas_station_label.grid(row = 8, column= 0, pady = 2, padx = 10, sticky = "w")
    gas_station_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC)
    gas_station_entry.grid(row = 8, column = 1, pady = 2, padx = 2)

    refuel_note_label = tkinter.Label(content_frame, text = "Note", font = FONT_STANDARD_LABEL)
    refuel_note_label.grid(row = 9, column= 0, pady = 2, padx = 10, sticky = "w")
    refuel_note_entry = tkinter.Text(content_frame, width = 25, font = FONT_BASIC, height = 5, wrap = "word")
    refuel_note_entry.grid(row = 9, column = 1, pady = 2, padx = 2)

    add_refuel_button = tkinter.Button(content_frame, text = "Add refuel stop", command = add_tanking_record, width = 25)
    add_refuel_button.grid(row = 10, column = 1, pady = 2, padx = 2)


window = tkinter.Tk()
window = window
window.title("Cool Fuel Tracker")
window.geometry("400x500")



# Create a menu
menu_bar = tkinter.Menu(window)
window.config(menu = menu_bar)
fuel_menu = tkinter.Menu(menu_bar, tearoff = 0)
fuel_menu.add_command(label = "New tanking", command = new_tanking)
fuel_menu.add_command(label = "Fuel statistics")
menu_bar.add_cascade(label = "Fuel", menu = fuel_menu)

service_menu = tkinter.Menu(menu_bar, tearoff = 0)
service_menu.add_command(label = "New service")
service_menu.add_command(label = "Service statistics")
menu_bar.add_cascade(label = "Service", menu = service_menu)

costs_menu = tkinter.Menu(menu_bar, tearoff = 0)
costs_menu.add_command(label = "New cost")
costs_menu.add_command(label = "Cost statistics")
menu_bar.add_cascade(label = "Costs", menu = costs_menu)

content_frame = tkinter.Frame(window)
content_frame.grid(row=0, column=0, padx=10, pady=10)
# register validation function 
vcmd = (content_frame.register(validate_decimal_input), '%P')

show_default() # show default page in the application    


     

window.mainloop()