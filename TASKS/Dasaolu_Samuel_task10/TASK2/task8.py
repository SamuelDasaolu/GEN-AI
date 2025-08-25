# Task 8
print("This is Task 8")

try:
    while True:  # Loop infinitely
        try:
            distance_km = float(input("Enter the distance in km (0 to quit): ").strip())
            if distance_km == 0:
                break

            fare_per_km = float(input("Enter the fare per km (0 to quit): ").strip())
            if fare_per_km == 0:
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        total_fare = distance_km * fare_per_km
        print(f"The total fare is: NGN{total_fare:.2f} \n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Fare calculation session ended.")
