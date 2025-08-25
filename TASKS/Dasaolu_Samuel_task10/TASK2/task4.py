# Task 4
print("This is Task 4")

try:
    while True:  # Loop infinitely
        dish = input("Please, name a Nigerian dish (or type 'done' to quit): ").strip()
        if not dish:
            print("Dish cannot be empty. Please enter a valid dish.")
            continue
        if dish.lower() == "done":
            break

        dish_state = input("Please name the state it is popular in (or type 'done' to quit): ").strip()
        if not dish_state:
            print("State cannot be empty. Please enter a valid state.")
            continue
        if dish_state.lower() == "done":
            break

        print(f"The popular dish is: {dish} and it is popular in \n \t {dish_state} State \n\n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Dish collection session ended.")
