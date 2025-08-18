"""
**Task3: Online Store Cart Calculation**

- Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

- Start with an empty cart total (cart_total = 0).

- Use assignment operators (+=) to add the price of some items into cart_total.

- Print the list of items and the total price using an f-string like this:

```
Items: ['Book', 'Pen', 'Bag']
Total Price: ₦600
```
"""

cart_items = ['item1', 'item2', 'item3']
prices = list(input(f'Enter price of {item.capitalize()}: ') for item in cart_items)
total_price = 0
for price in prices: total_price += int(price)
print(f"""```
Items: ['Book', 'Pen', 'Bag']
Total Price: ₦{total_price}
```""")