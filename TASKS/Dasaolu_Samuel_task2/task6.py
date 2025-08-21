# Task 6
print("This is Task 6")
name = input("Customer full Name: ")
units_consumed = int(input("Units consumed as Whole Number(kWh): "))
cost_per_unit = float(input("Cost per Unit: "))
total_bill = str(units_consumed * cost_per_unit)
print(f"\t\t\t\t Receipt \n Name \t\t\t Units Consumed \t Cost Per Unit \n {name} \t\t {units_consumed} \t\t {cost_per_unit} \n "
      f"Total Price = {total_bill} \n")
