"""
**Task5: Store Inventory Update**
- Create a dictionary called store with items and their available quantities. Example:
```
store = {"Book": 10, "Pen": 20, "Bag": 5}
```


- Ask the user to input the item they want to buy (e.g., "Pen").

- Ask the user to input the quantity they want to purchase.

- Use the assignment operator -= to update (reduce) the item quantity in the dictionary.

- Print the updated dictionary in this format:

```
Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
```
"""

print("Available Items: (ITEM): QUANTITY")
store = {"Book": 10, "Pen": 20, "Bag": 5}
store_before = {key: value for key,value in store.items()}
item = input(f"Item to Purchase: ").title().strip()
quantity = int(input(f"Quantity of {item} to Purchase: "))
store[item] -= quantity

print(f"""
```
Before purchase: {store_before}
After purchase: {store}
```
""")

