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

    selected_cost_filter = tkinter.StringVar(value = "All cost types")
    cost_type_filter = []
    cost_type_dates_filter = []
    for record in costs_history:
        if len(costs_history) > 0:    
            cost_type_filter.append(record["Cost type"]) # will append all cost types from the list
            cost_type_dates_filter.append(record["Cost date"])
        else: 
            cost_type_filter[0] = "No records found"
    
    cost_type_filter = list(set(cost_type_filter)) # to remove duplicates
    cost_type_filter.insert(0, "All cost types") # potentially to add all records filter
    
    cost_type_years_filter = [datetime.strptime(date, "%d.%m.%Y").year for date in cost_type_dates_filter]
    cost_type_years_filter = sorted(list(set(cost_type_years_filter)))
    cost_type_years_filter.insert(0, "All years")
        
    costs_filter_dropdown = tkinter.OptionMenu(content_frame, selected_cost_filter, *cost_type_filter)
    costs_filter_dropdown.config(width = 15)
    costs_filter_dropdown.grid(row = 8, column = 0, pady = 2, padx = 2)

    selected_cost_year_filter = tkinter.StringVar(value = "All years")
    costs_year_filter_dropdown = tkinter.OptionMenu(content_frame, selected_cost_year_filter, *cost_type_years_filter)
    costs_year_filter_dropdown.config(width = 10)
    costs_year_filter_dropdown.grid(row = 8, column = 1, pady = 2, padx = 2)

    filter_statistics_button = tkinter.Button(content_frame, text = "Filter", 
                                              command = lambda: display_costs_log(content_frame, selected_cost_filter.get(), selected_cost_year_filter.get(), filtered_costs_value))
    filter_statistics_button.grid(row = 8, column = 2, pady = 2, padx = 2)

    filtered_costs_label = tkinter.Label(content_frame, text = "Total filtered costs")
    filtered_costs_label.grid(row = 10, column = 0, sticky = "w")
    filtered_costs_value = tkinter.Label(content_frame, text = f"{calculate_total_costs():.2f} CZK")
    filtered_costs_value.grid(row = 10, column = 1, sticky = "e")

    display_costs_log(content_frame, "All cost types", "All years", filtered_costs_value)

def show_filtered_costs_label(filtered_costs_total, filtered_costs_value):
    filtered_costs_value.config(text = f"{filtered_costs_total} CZK")

def display_costs_log(content_frame, cost_type, year, filtered_costs_value):
    # Clear previous content
    #clear_content(content_frame)
    cost_type = cost_type
    year = year
    filtered_costs_total = 0

    costs_history = load_costs_history()
    filtered_costs_history = []
    if cost_type == "All cost types" and year == "All years":
        filtered_costs_history = costs_history
    elif cost_type != "All cost types" and year == "All years":
        for record in costs_history:
            if record["Cost type"] == cost_type:  # Check if the cost type matches
                filtered_costs_history.append(record)  # Append the entire record
                filtered_costs_total += record["Price"]
    elif cost_type == "All cost types" and year != "All years":
        for record in costs_history:
            cost_date = datetime.strptime(record["Cost date"], "%d.%m.%Y")  # Parse the cost date
            if cost_date.year == int(year):  # Check if the year matches
                filtered_costs_history.append(record)  # Append the entire record
                filtered_costs_total += record["Price"]
    elif cost_type != "All cost types" and year != "All years":
        for record in costs_history:
            cost_date = datetime.strptime(record["Cost date"], "%d.%m.%Y")  # Parse the cost date
            if record["Cost type"] == cost_type and cost_date.year == int(year):  # Check both conditions
                filtered_costs_history.append(record)  # Append the entire record
                filtered_costs_total += record["Price"]
    
    show_filtered_costs_label(filtered_costs_total, filtered_costs_value)


    content_frame.pack_propagate(False)

    # Create a canvas and scrollbar
    canvas = tkinter.Canvas(content_frame, width = 350)
    scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar
    #canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    #scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    canvas.grid(row=9, column=0, columnspan = 3, sticky="nsew")  # Change to row 9
    scrollbar.grid(row=9, column=3, sticky="ns")

    # Create an inner frame to hold all the records
    inner_frame = tkinter.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")
    #inner_frame_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Populate the inner_frame with records
    for index, record in enumerate(reversed(filtered_costs_history)):
        record_text = (
            f"Record {len(costs_history) - index}:\n"
            f"Odometer Status: {record['Odometer status']}\n"
            f"Cost Type: {record['Cost type']}\n"
            f"Cost Clarification: {record['Cost clarification']}\n"
            f"Price: {record['Price']}\n"
            f"Cost Date: {record['Cost date']}\n"
            f"Cost Note: {record['Cost note'].strip()}\n"
        )
        record_frame = tkinter.Frame(inner_frame)
        record_frame.pack(anchor="w", padx=10, pady=5, fill=tkinter.X)

        label = tkinter.Label(record_frame, text=record_text, justify="left", anchor="w")
        label.pack(side=tkinter.LEFT, padx=5)

        # Create a delete button for each record
        delete_button = tkinter.Button(record_frame, text="Delete", command=lambda r=record: delete_record(r, content_frame))
        delete_button.pack(side=tkinter.RIGHT, padx=5)

    # Update the canvas scroll region after adding all records
    def update_scroll_region(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the Configure event to update scroll region on inner_frame resizing
    inner_frame.bind("<Configure>", update_scroll_region)
    # Function to handle mouse wheel scrolling
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Bind the mouse wheel event to the canvas
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)


def delete_record(record, content_frame):
    # Load current costs history
    costs_history = load_costs_history()

    # Remove the record from the history
    costs_history.remove(record)

    # Save the updated costs history back to the JSON file
    with open(file_path_costs, 'w') as f:
        json.dump(costs_history, f, indent=4)

    # Refresh the display to reflect the deletion
    display_costs_log(content_frame, "All cost types", "All years") 
