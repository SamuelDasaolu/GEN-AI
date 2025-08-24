# Task 7
print("This is Task 7")

try:
    while True:  # Loop infinitely
        try:
            age = int(input("Enter your age (0 to quit): ").strip())
            if age == 0:  # exit condition
                break

            height = float(input("Enter your height in meters: ").strip())
            name = input("Enter your name: ").strip()

            if not name:
                print("Name cannot be empty. Please enter a valid name.")
                continue

        except ValueError:
            print("Invalid input. Please enter numeric values for age and height.")
            continue

        print(f"My name is {name}, I am {age} years old, and my height is {height} meters. \n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("User information collection session ended.")
