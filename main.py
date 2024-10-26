import tkinter
from tkinter import Menu

tanking_history = []

class CarFuelTracker:
    def __init__(self, window):
        self.window = window
        self.window.title("Cool Fuel Tracker")
        self.window.geometry("400x500")

        # Create a menu
        menu_bar = tkinter.Menu(window)
        fuel_menu = tkinter.Menu(menu_bar, tearoff = 0)
        fuel_menu.add_command(label = "New tanking", command = self.clear_content)
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

        self.content_frame = tkinter.Frame(self.window)
        self.content_frame.pack(pady = 10)

        window.config(menu = menu_bar)


    
    def clear_content(self):
        #Clears content of the current window
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_default(self):
        self.clear_content()
        testing_label = tkinter.Label(self.content_frame, text = "Initial tanking history")
        testing_label.grid(row = 0, column = 0)

    def new_tanking(self):
        self.clear_content() # Will refresh the window to enable new widgets
        


    

if __name__ == "__main__":
    window = tkinter.Tk()
    app = CarFuelTracker(window)
    window.mainloop()