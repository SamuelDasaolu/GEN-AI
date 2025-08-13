"""
**Task 2: Shopping List Manager**
- Create an empty list.

- Ask the user to enter 3 shopping items (one by one).

- Add them to the list.

- Display the list as a single string, separated by commas.
"""

shopping_list = []
item_1 = input("Please input Item 1: ")
shopping_list.append(item_1)
item_2 = input("Please input Item 2: ")
shopping_list.append(item_2)
item_3 = input("Please input Item 3: ")
shopping_list.append(item_3)
shopping_list_string = ', '.join(shopping_list)
print(shopping_list_string)