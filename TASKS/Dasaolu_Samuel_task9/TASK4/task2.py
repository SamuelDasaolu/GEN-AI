"""
**Task 2: Shopping List Manager**
- Create an empty list.

- Ask the user to enter 3 shopping items (one by one).

- Add them to the list.

- Display the list as a single string, separated by commas.
"""
#Using Control Loops
shopping_list = []
shopping_list_string = ''
item_no = 1
while item_no <=3:
    item = input(f"Please input Item {item_no}: ")
    shopping_list.append(item)
    item_no+=1
    
for item in shopping_list:
    shopping_list_string += item + ', '
    
shopping_list_string = shopping_list_string.removesuffix(', ') #Removes the trailing comma
print("Shopping List: ", shopping_list_string)