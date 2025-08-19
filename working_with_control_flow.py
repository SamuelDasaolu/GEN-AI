# age = 20
# if age >= 18:
#     print("You are eligible to vote")

# wallet = 400
# price = 500

# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")

# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")


# number_list = list(range(30))
# for number in number_list:
#     print(number, end= ' ')

# count = 0
# while count < 6:
#     if count == 3: 
#         break
#     else:
#         print("Number:", count)       #NB: weird behaviour for pass and contnue in while loop
                
#         count+=1
#     print("out level 1", count)
# print("completely outside")

# Do you remember this?

balance = 1000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
