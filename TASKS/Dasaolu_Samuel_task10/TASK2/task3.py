# Task 3
print("This is Task 3")

try:
    while True:  # Loop infinitely
        name = input("What is your Name? (or type 'done' to quit): ").strip()
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        if name.lower() == "done":
            break

        student_class = input("What class are you? (or type 'done' to quit): ").strip()
        if not student_class:
            print("Class cannot be empty. Please enter a valid class.")
            continue
        if student_class.lower() == "done":
            break

        state_of_origin = input("What is your state of origin? (or type 'done' to quit): ").strip()
        if not state_of_origin:
            print("State of origin cannot be empty. Please enter a valid state.")
            continue
        if state_of_origin.lower() == "done":
            break

        print(f"Student {name} is in {student_class} and is from {state_of_origin} \n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Student data collection session ended.")
