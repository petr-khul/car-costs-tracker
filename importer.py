import csv
import json

csv_file_path = "data.csv"
json_file_path = "imported.json"

data_list = []

with open(csv_file_path, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")

    header = next(csv_file)

    for row in csv_reader:
        date = row[0]
        odo = row[1]
        fuel_amount = row[2]
        price = row[4]
        avg_consumption = row[5]
        gas_station = row[9]
        price_per_liter = row[13]
    

        record = {
        "Odometer status": float(odo),
        "Fuel type": "Natural 95",
        "Fuel amount": float(fuel_amount),
        "Refuel total price": float(price),
        "Price per liter": float(price_per_liter),
        "Refuel date": date,
        "Tank full": True,
        "Gas station": gas_station,
        "Refuel note": "\n"
        }
        data_list.append(record)   
    
    with open(json_file_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)  # indent=4 for pretty formatting
