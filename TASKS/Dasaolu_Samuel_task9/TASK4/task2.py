"""
**Task 2: Shopping List Manager**
- Create an empty list.
- Ask the user to enter 3 shopping items (one by one).
- Add them to the list.
- Display the list as a single string, separated by commas.
"""
# Using Control Loops
shopping_list = []
shopping_list_string = ''
item_no = 1

try:
    while item_no <= 3:
        item = input(f"Please input Item {item_no}: ").strip()

        if not item:  # empty input check
            print("Item cannot be empty. Please enter a valid shopping item.")
            continue

        shopping_list.append(item)
        item_no += 1

    for item in shopping_list:
        shopping_list_string += item + ', '

    shopping_list_string = shopping_list_string.removesuffix(', ')  # Removes the trailing comma
    print("Shopping List: ", shopping_list_string)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Shopping list collection attempt finished.")
