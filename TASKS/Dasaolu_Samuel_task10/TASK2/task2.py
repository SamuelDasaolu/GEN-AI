# Task 2
print("This is Task 2")

try:
    while True:  # Loop infinitely
        try:
            price_of_garri = float(input("Please input the price of garri in Naira (0 to quit): ").strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if price_of_garri == 0:  # exit condition
            break

        print(f"Today, the price of garri is NGN{price_of_garri:,.2f} Kobo \n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Garri price reporting session ended.")
