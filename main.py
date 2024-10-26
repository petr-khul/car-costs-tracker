import tkinter
from tkinter import Menu


FONT_HEADER = ("Arial", 14, "bold")
FONT_STANDARD_LABEL = ("Arial", 11, "bold")
FONT_BASIC = ("Arial", 11)
BG_COLOR = "#808080"
tanking_history = []

def clear_content():
    #Clears content of the current window
    for widget in content_frame.winfo_children():
        widget.destroy()
    
def show_default():
    clear_content()
    testing_label = tkinter.Label(content_frame, text = "Initial tanking history")
    testing_label.grid(row = 0, column = 0)

def new_tanking():
    clear_content() # Will refresh the window to enable new widgets
    
    new_tanking_label = tkinter.Label(content_frame, text = "ADD NEW REFUEL STOP", font = FONT_HEADER)
    new_tanking_label.grid(row = 0, column = 0, columnspan = 2, sticky = "w", padx = 10)
    
    odometer_label = tkinter.Label(content_frame, text = "Odometer:", font = FONT_STANDARD_LABEL)
    odometer_label.grid(row = 1, column= 0, pady = 10, padx = 10, sticky = "w")

    odometer_entry = tkinter.Entry(content_frame, width = 30, font = FONT_BASIC)
    odometer_entry.grid(row = 1, column = 1, pady = 10, padx = 10)

    amount_label = tkinter.Label(content_frame, text = "Fuel amount:", font = FONT_STANDARD_LABEL)
    amount_label.grid(row = 2, column= 0, pady = 2, padx = 10, sticky = "w")

    amount_entry = tkinter.Entry(content_frame, width = 30, font = FONT_BASIC)
    amount_entry.grid(row = 2, column = 1, pady = 2, padx = 2)

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

show_default() # show default page in the application    
     

window.mainloop()