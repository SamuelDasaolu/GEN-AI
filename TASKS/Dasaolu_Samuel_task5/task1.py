"""**Task1:  Create and Display**

- Ask the user to enter three favorite Nigerian dishes (one at a time).

 - Store them in a tuple called dishes.

- Print the tuple in a single line, separating items with commas.

- Use the \n escape sequence to print each dish on a new line.
"""

dish_1 = input("Favorite Dish 1: ")
dish_2 = input("Favorite Dish 2: ")
dish_3 = input("Favorite Dish 3: ")

dishes = (dish_1, dish_2, dish_3)
print(dishes) #Print tuple on single line
print("Each on a new line")
print(f"Dish 1: {dish_1} \n Dish 2: {dish_2} \n Dish 3: {dish_3}")