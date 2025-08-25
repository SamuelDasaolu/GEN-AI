# Task 12
print("This is Task 12")
print("Welcome to your mobile service network!")
while True:
    ussd_code = input("Please dial a USSD code to begin (e.g., *345#): ")
    if ussd_code.startswith('*') and ussd_code.endswith('#'):

        print("\nWelcome to the USSD service menu.")
        print("1. Check Balance")
        print("2. Buy Airtime")
        print("3. Buy Data")

        balance = 0.00
        while True: 
            user_choice = input("Enter your choice (1, 2, or 3): ")
            if user_choice == "1":
                print(f"\nThank you for choosing Option 1: Check Balance.")
                print(f"Your Balance: NGN {balance}")
                print("Your balance inquiry is being processed. You will receive an SMS shortly.")
            elif user_choice == "2":
                print(f"\nThank you for choosing Option 2: Buy Airtime.")
                airtime_amount = float(input("Enter the amount of airtime to buy: "))
                balance+=airtime_amount
                print(f"Purchase of NGN{airtime_amount} successful")
                print(f"Your balance is now NGN {balance}")
                print(f"\nTransaction complete. You have successfully purchased ₦{airtime_amount:,.2f} of airtime.")
            elif user_choice == "3":
                print(f"\nThank you for choosing Option 3: Buy Data.")
                data_amount = float(input("Enter the amount of data to buy (in GB)(250 per GB): "))
                data_price = data_amount*250
                if data_price <= balance:
                    balance-=data_price
                    print(f"\nTransaction complete. You have successfully purchased {data_amount:,.2f}GB of data valued at NGN {data_price}.")
                else:
                    print(f"Transaction failed, please recharge and try again later")
                    break
            else:
                print("\nInvalid option selected. Please try again.")
                break
    else:
        print("\nInvalid USSD code.")

    print("\nThank you for using our service! \n")