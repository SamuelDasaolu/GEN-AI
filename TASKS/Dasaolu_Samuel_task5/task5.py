"""
**Task5: Modify Tuple Indirectly**
Ask a user to enter three items for their shopping list.

  - Store in a tuple shopping_list.

  - Convert it to a list, then ask for two more items to add.

  - Convert back to a tuple and print the updated list using join() to display items separated by " | ".
"""
  
print("Enter Shopping List")  
shopping_list_tuple = (input("Item 1: "), input("Item 2: "), input("Item 3: "))
shopping_list = list(shopping_list_tuple)
item_4 = input("Add 4th Item: ")
item_5 = input("Add 5th Item: ")
shopping_list.append(item_4)
shopping_list.append(item_5)
shopping_list_tuple = tuple(shopping_list)

print(' | '.join(shopping_list_tuple))