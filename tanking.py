
from tkinter import *
from tkinter import messagebox
import tkinter
from tkcalendar import *
from datetime import date, datetime
from general import *

def new_tanking(content_frame):
    clear_content(content_frame) # Will refresh the window to enable new widgets

    def add_tanking_record():
        
        tanking_history = load_tanking_history()
        last_refuel_stop = tanking_history[-1]
        last_odometer_status = last_refuel_stop["Odometer status"]
        odometer_status = odometer_entry.get().strip()
        if not odometer_status:
            messagebox.showwarning("Invalid Input", "All required fields needs to be filled")
            return
        elif float(odometer_status) < last_odometer_status:
            messagebox.showwarning("Invalid Input", "New odometer value cannot be lower than last one.")
            return
        else:
            odometer_status = float(odometer_status)
        fuel_type = selected_fuel_type.get()
        if fuel_type == "Select the fuel type":
            messagebox.showwarning("Missing input", "Please select valid fuel type")
            return
        fuel_amount = fuel_amount_entry.get().strip()
        if not fuel_amount:
            messagebox.showwarning("Invalid Input", "All required fields needs to be filled")
            return
        else:
            fuel_amount = float(fuel_amount)
        refuel_total_price = refuel_price_entry.get()
        if not refuel_total_price:
            messagebox.showwarning("Invalid Input", "All required fields needs to be filled")
            return
        else:
            refuel_total_price = float(refuel_total_price)
        price_per_liter = float(refuel_total_price)/float(fuel_amount)
        refuel_date = refuel_date_entry.get()
        tank_full_value = tank_full.get()
        previous_refuelling_missing_value = previous_refuelling_missing.get()
        gas_station = gas_station_entry.get()
        if not gas_station:
            messagebox.showwarning("Invalid Input", "All required fields needs to be filled")
            return
        refuel_note = refuel_note_entry.get("1.0", tkinter.END)

        #print(odometer_status, fuel_type, fuel_amount, refuel_price, refuel_date, tank_full_value, previous_refuelling_missing_value, gas_station, refuel_note)

        refuel_record = {
            "Odometer status" : float(odometer_status), 
            "Fuel type" : fuel_type, 
            "Fuel amount" : float(fuel_amount), 
            "Refuel total price" : float(refuel_total_price),
            "Price per liter" : float(price_per_liter), 
            "Refuel date" : refuel_date, 
            "Tank full" : tank_full_value, 
            "Previous_refuelling_missing" : previous_refuelling_missing_value, 
            "Gas station" : gas_station, 
            "Refuel note" : refuel_note
        }

        append_tanking_history(refuel_record)
        last_tank_full = last_refuel_stop["Tank full"]
        if tank_full_value == True and last_tank_full == True:
            avg_consumption = fuel_amount/(odometer_status-last_odometer_status)*100
            price_per_km = refuel_total_price/(odometer_status-last_odometer_status)
            messagebox.showinfo("Refuel stop added", f"Refuel stop added successfully!\nAverage consumption {avg_consumption:.2f} l/km\nPrice per kilometer {price_per_km:.2f} CZK")
        else:
            messagebox.showinfo("Refuel stop added", "Refuel stop added successfully!")
        clear_content(content_frame)
        show_default(content_frame)
        #print(tanking_history) #was only for testing
    
    # Register validation function for input
    vcmd = (content_frame.register(validate_decimal_input), '%P')
    
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



        
