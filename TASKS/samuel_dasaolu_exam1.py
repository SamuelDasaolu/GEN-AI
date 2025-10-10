"""
Question 1

Write a Python program that works as a basic calculator with continuous use.

"""


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Invalid Operation, Denominator cannot be Zero")


while True:
    print('Welcome to Calculator Program')

    try:
        x = int(input("Enter First Number, X: "))
        y = int(input("Enter Second Numbber, Y: "))

        operation = input(
            "Choose operation (+, -, *, /) or 'exit' to quit: ").strip()

        if operation == '+':
            print(f"RESULT: {add(x, y)}")
        elif operation == '-':
            print(f"RESULT: {subtract(x, y)}")
        elif operation == '*':
            print(f"RESULT: {multiply(x, y)}")
        elif operation == '/':
            print(f"RESULT: {divide(x, y)}")
        elif operation.lower() == 'exit':
            print("Exiting calculator... Goodbye!")
            break
        else:
            print('Invalid Operation, Select only a valid operation')

    except ValueError:
        print("This program only accepts integers as inputs")


"""
Question 2

Complete the missing parts of the program below so that it keeps asking the user for a number and tells whether it is even or odd.
"""

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop

    num = int(user_input)   # convert to integer

    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


"""
Question 3

    The following code is supposed to ask for a user’s age repeatedly and say whether they are allowed to vote (18+).
    It should also exit if the user types 'exit'. However, the code contains errors.

"""

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == 'exit':
        print("Goodbye!")
        break

    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")
