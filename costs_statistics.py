from tkinter import *
from tkinter import messagebox
import tkinter
from tkcalendar import *
from datetime import date, datetime
from general import *

costs_history = load_costs_history()

def calculate_total_costs():
    total_costs = 0
    for record in costs_history:
        total_costs += record["Price"]
    return total_costs

def calculate_costs_this_year():
    this_year = (datetime.now().year)
    this_year_costs_sum = 0

    for record in costs_history:
        cost_date = datetime.strptime(record["Cost date"], "%d.%m.%Y")
        if cost_date.year == this_year:
            this_year_costs_sum += record["Price"]
    return this_year_costs_sum

def costs_statistics_window(content_frame):
    clear_content(content_frame)
    calculate_total_costs() # to refresh the label content everytime when window is being shown
    calculate_costs_this_year() # to refresh the label content everytime when window is being shown

    costs_statistics_label = tkinter.Label(content_frame, text = "Costs statistics", font = FONT_HEADER)
    costs_statistics_label.grid(row=0, column=0, columnspan=2, sticky = "w")

    costs_header_separator = ttk.Separator(content_frame, orient='horizontal')
    costs_header_separator.grid(row=1, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)

    total_costs_label = tkinter.Label(content_frame, text = "Total costs")
    total_costs_label.grid(row = 2, column = 0, sticky = "w")
    total_costs_value = tkinter.Label(content_frame, text = f"{calculate_total_costs():.2f} CZK")
    total_costs_value.grid(row = 2, column = 1, sticky = "e")

    costs_this_year_label = tkinter.Label(content_frame, text = "Costs this year")
    costs_this_year_label.grid(row = 3, column = 0, sticky = "w")
    costs_this_year_value = tkinter.Label(content_frame, text = f"{calculate_costs_this_year():.2f} CZK")
    costs_this_year_value.grid(row = 3, column = 1, sticky = "e")

    costs_filter_separator = ttk.Separator(content_frame, orient='horizontal')
    costs_filter_separator.grid(row=4, column=0, columnspan= 2, sticky="ew", padx=5, pady=5)

    selected_cost_filter = tkinter.StringVar(value = "Select a cost_type")
    cost_type_filter = []
    for record in costs_history:
        if len(costs_history) > 0:    
            cost_type_filter.append(record["Cost type"]) # will append all cost types from the list
        else: 
            cost_type_filter[0] = "No records found"
    cost_type_filter = list(set(cost_type_filter)) # to remove duplicates
        
    costs_filter_dropdown = tkinter.OptionMenu(content_frame, selected_cost_filter, *cost_type_filter)
    costs_filter_dropdown.config(width = 15)
    costs_filter_dropdown.grid(row = 6, column = 0, pady = 2, padx = 2)