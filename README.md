# car costs tracker

Application for tracking basic costs for the car
- Currently available only for traking one default car, without option of addin second car
- Data being stored as list of dictionaries saved in json file - separate files for fuel and for costs

*** Home screen ***
- Fuel overview
--- overview of basic information about fuel and refuel stops
--- button for showing detail statistics
- Costs overview
--- basic info about costs different than fuel
--- by default shows total costs and costs in current year
--- button to show detail costs statistics
- Total expenses overview
--- overview of total expenses - fuel and costs together
--- summary of total kilometers and expenses
--- averages for expenses per km and per month

*** Fuel ***
- Add refuel
--- form for new refuel stop input
--- contains form validation with already saved data
- Fuel statistics
--- detail staitistics from previous data, dynamically re-calculated
--- green value - beter than average value
--- red value - worse than average value
- Fuel log
--- list of all refuel records with all the details
--- only last record can be deleted

*** Costs ***
- Add cost
--- for for adding new cost different than fuel
--- contains defined cost type for filtering
- Costs statistics
--- detail statistics with total costs
--- log with all the records
--- after filtering, the total price for filtered cost types will be calculated