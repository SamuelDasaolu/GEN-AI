# Task 8
print("This is Task 8")
while True: #Loop infinitely
    distance_km = float(input("Enter the distance in km: "))
    fare_per_km = float(input("Enter the fare per km: "))
    total_fare = distance_km * fare_per_km
    print(f"The total fare is: NGN{total_fare:.2f} \n")
