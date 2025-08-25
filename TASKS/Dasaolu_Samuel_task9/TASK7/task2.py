"""
**Task2: Super Market Price List**
- Create a program that stores items and their prices in a dictionary.

  - Items should come from a list.

  - Prices are entered by the user.

  - Display all items and prices, then allow the user to update the price of an item.

- Requirements:

  - Use dictionary update method `.update()` or assignment.

  - Use `.keys()` to display available items.

  - Use input validation (no advanced functions).
"""

items = ['orange', 'banana', 'apple']
price_list = {}
for item in items:price_list[item] = ' '
print(price_list)
while True:
    item_to_update = input(f'Type Item that you want to update price{items}: ').lower()
    if item_to_update in price_list.keys():
        price_list.update({item_to_update: input(f"What is the price of {item_to_update}: ")})
    else: print("Item not in stock")
    print(price_list)
    
