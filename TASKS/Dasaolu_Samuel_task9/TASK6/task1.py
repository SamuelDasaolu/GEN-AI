"""
**Task1: Fruit collector**
- Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
"""
i = 1
fruits = set()
while i<=5: #Using Control Loop
    favorite_fruit = input(f"Favorite Fruit {i}: ")
    if favorite_fruit in fruits:
        print('That fruit has been entered before')
        continue
    else:
        fruits.add(favorite_fruit)
    i+=1
print(fruits)