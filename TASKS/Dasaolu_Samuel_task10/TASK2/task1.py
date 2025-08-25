# Task 1
print("This is Task 1")

try:
    while True:  # Loop infinitely
        name = input("What is your Name? (or type 'done' to quit): ").strip()
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        if name.lower() == "done":
            break

        age_input = input("What is your Age? (or type 0 to quit): ").strip()
        if not age_input:
            print("Age cannot be empty. Please enter a valid number.")
            continue
        if age_input == "0":
            break

        try:
            age = int(age_input)
        except ValueError:
            print("Invalid age. Please enter a numeric value.")
            continue

        print(f"Welcome {name}, you are {age} years old \n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("User greeting session ended.")
