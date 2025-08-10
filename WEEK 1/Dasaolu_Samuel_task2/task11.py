# Task 11
print("This is Task 11")
naira_amount = float(input("Enter the amount in Naira (₦): "))
usd_rate = float(input("Enter the exchange rate for US Dollars ($): "))
gbp_rate = float(input("Enter the exchange rate for British Pounds (£): "))
dollars_amount = naira_amount / usd_rate
pounds_amount = naira_amount / gbp_rate
print("\n--- Currency Conversion Results ---\n")
print(f"Naira (₦):\t\t{naira_amount:,.2f}")
print(f"US Dollars ($):\t\t{dollars_amount:,.2f}")
print(f"British Pounds (£):\t{pounds_amount:,.2f}")
