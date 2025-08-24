# Task 6
print("This is Task 6")

try:
    while True:  # Loop infinitely
        name = input("Customer full Name (or type 'done' to quit): ").strip()
        if not name:
            print("Name cannot be empty. Please enter a valid customer name.")
            continue
        if name.lower() == "done":
            break

        try:
            units_consumed = int(input("Units consumed as Whole Number (kWh, 0 to quit): ").strip())
            if units_consumed == 0:  # exit condition
                break

            cost_per_unit = float(input("Cost per Unit (0 to quit): ").strip())
            if cost_per_unit == 0:  # exit condition
                break

        except ValueError:
            print("Invalid input. Units must be an integer and cost must be a number.")
            continue

        total_bill = units_consumed * cost_per_unit
        print(
            f"\n\t\t\t\t Receipt \n"
            f"Name \t\t\t Units Consumed \t Cost Per Unit \n"
            f"{name} \t\t {units_consumed} \t\t\t {cost_per_unit:.2f} \n"
            f"Total Price = NGN{total_bill:,.2f} \n"
        )

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Billing session ended.")
