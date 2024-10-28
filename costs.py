from tkinter import *
from tkinter import messagebox
import tkinter
from tkcalendar import *
from datetime import date, datetime
from general import *

def new_costs(content_frame):
    clear_content(content_frame)

    def add_cost():
        pass

    vcmd = (content_frame.register(validate_decimal_input), '%P') #register form validation function

    new_cost_label = tkinter.Label(content_frame, text = "ADD NEW COSTS", font = FONT_HEADER)
    new_cost_label.grid(row = 0, column = 0, columnspan = 2, sticky = "w", padx = 10, pady = 10)

    cost_type_dropdown_options = ["Service", "Maintenance", "Parking", "Wash", "Sanction", "Insurance", "Tuning", "Other"]
    cost_type_label = tkinter.Label(content_frame, text = "Cost type", font = FONT_STANDARD_LABEL)
    cost_type_label.grid(row = 1, column= 0, pady = 2, padx = 10, sticky = "w")
    selected_cost_type = tkinter.StringVar()
    selected_cost_type.set("Select the cost type")
    cost_type_dropdown = tkinter.OptionMenu(content_frame, selected_cost_type, *cost_type_dropdown_options)
    cost_type_dropdown.config(width = 25)
    cost_type_dropdown.grid(row = 1, column = 1, pady = 2, padx = 2)

    cost_clarification_label = tkinter.Label(content_frame,text = "Cost clarification", font = FONT_STANDARD_LABEL)
    cost_clarification_label.grid(row = 2, column = 0, padx = 10, sticky = "w")
    cost_clarification_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC)
    cost_clarification_entry.grid(row = 2, column = 1, pady = 2, padx = 2)

    cost_price_label = tkinter.Label(content_frame, text = "Cost price", font = FONT_STANDARD_LABEL)
    cost_price_label.grid(row = 3, column= 0, pady = 2, padx = 10, sticky = "w")
    cost_price_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC, validate = "key", validatecommand=vcmd)
    cost_price_entry.grid(row = 3, column = 1, pady = 2, padx = 2)

    cost_odometer_label = tkinter.Label(content_frame, text = "Odometer status", font = FONT_STANDARD_LABEL)
    cost_odometer_label.grid(row = 4, column= 0, pady = 2, padx = 10, sticky = "w")
    cost_odometer_entry = tkinter.Entry(content_frame, width = 25, font = FONT_BASIC, validate = "key", validatecommand=vcmd)
    cost_odometer_entry.grid(row = 4, column = 1, pady = 2, padx = 10)

    cost_date_label = tkinter.Label(content_frame, text = "Date", font = FONT_STANDARD_LABEL)
    cost_date_label.grid(row = 5, column= 0, pady = 2, padx = 10, sticky = "w")
    cost_date_entry = DateEntry(content_frame, selectmode = "day", date_pattern = "dd.mm.yyyy")
    cost_date_entry.config(width = 25)
    cost_date_entry.grid(row = 5, column= 1, pady = 2, padx = 10, sticky = "w")

    cost_note_label = tkinter.Label(content_frame, text = "Note", font = FONT_STANDARD_LABEL)
    cost_note_label.grid(row = 6, column= 0, pady = 2, padx = 10, sticky = "w")
    cost_note_entry = tkinter.Text(content_frame, width = 25, font = FONT_BASIC, height = 5, wrap = "word")
    cost_note_entry.grid(row = 6, column = 1, pady = 2, padx = 2)

    add_refuel_button = tkinter.Button(content_frame, text = "Add refuel stop", command = add_cost, width = 25)
    add_refuel_button.grid(row = 7, column = 1, pady = 2, padx = 2)