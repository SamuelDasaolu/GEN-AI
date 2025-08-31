from calculator.calc import *


def main():
    while True:
        try:
            # Display operation options to the user
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Quit")
            operation = input("Enter Choice 1, 2, 3, 4, 5: ")
            if operation.isdigit() and int(operation.strip()) <= 4:
                num1 = float(input("Enter Value for X: "))
                num2 = float(input("Enter Value for Y: "))
                if int(operation.strip()) == 1:
                    print(f" \n Results: {num1} + {num2} = {add(num1, num2)}")
                elif int(operation.strip()) == 2:
                    print(f" \n Results: {num1} - {num2} = {subtract(num1, num2)}")
                elif int(operation.strip()) == 3:
                    print(f" \n Results: {num1} * {num2} = {multiply(num1, num2)}")
                elif int(operation.strip()) == 4:
                    print(f" \n Results: {num1} / {num2} = {divide(num1, num2)}")

            elif int(operation.strip()) == 5:
                print("\n Operation Canceled by user")
                break

            else:
                print("\n User has entered an invalid choice, try again")

        except ValueError:
            print("\n This calculator program only accepts numbers as input")
        except KeyboardInterrupt:
            print("\n Program canceled by user. Safely Exiting...")
            break

if __name__ == '__main__':
    main()
