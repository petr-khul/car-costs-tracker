import tkinter

class CarFuelTracker:
    def __init__(self, window):
        self.window = window
        self.window.title("Cool Fuel Tracker")
        self.window.geometry("400x500")

        # Create a menu
        menu_bar = tkinter.Menu(window)
        fuel_menu = tkinter.Menu(menu_bar, tearoff = 0)
        fuel_menu.add_command(label = "New tanking")
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

        window.config(menu = menu_bar)
    
    
    

if __name__ == "__main__":
    window = tkinter.Tk()
    app = CarFuelTracker(window)
    window.mainloop()