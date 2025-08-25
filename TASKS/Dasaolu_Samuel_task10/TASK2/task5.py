# Task 5
print("This is Task 5")

try:
    market_name = input("Please input market name: ").strip()
    if not market_name:
        raise ValueError("Market name cannot be empty.")

    try:
        no_of_traders = int(input("Input number of traders: ").strip())
        daily_revenue = float(input("Input daily revenue in NGN: ").strip())
    except ValueError:
        print("Invalid input. Traders must be an integer and revenue must be a number.")
    else:
        result = (
            f"Market Name: {market_name} \n"
            f"Number of traders: {no_of_traders:,} \n"
            f"Daily Revenue in Naira: NGN{daily_revenue:,.2f} \n"
        )
        print(result)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Market information collection finished.")
