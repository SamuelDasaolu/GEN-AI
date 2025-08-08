# # Basic usage of input()
# name = input("Enter your name: ")
# print("Hello,", name)

# # Convert input to integer
# age = int(input("Enter your age: "))
# print(f"You will be {age + 1} years old next year.")

# type casting entails turning variables into desired data type--//shows error if wrong datatype supplied
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}.")


message = 'Welcome to Banking Services'
option_1 = '1. Add Balance'
option_2 = '2. Recharge Balance'
option_3 = '3. Recharge Airtime'

print(f"""
{message}
With this platform, you can: 
{option_1}
{option_2}
{option_3}

""")
option_chosen = int(input("What can we help you with today: "))

print("You've chosen to Add Balance")
deposit = float(input("Enter Amount to Deposit: "))

print(f"""
You've chosen to deposit {deposit} naira only

Please wait, we are processing your payment

Payment Completed Successfully
""")

