"""
**Task5: Contact Quick Lookup**
- Store three names and their phone numbers in two separate tuples.

  - Create a dictionary from them using `dict(zip(...))`.

  - Ask the user for a name and display the corresponding number (or an error message).

- Requirements:

  - Use `zip()` and d`ict()` to combine tuples.

  - Use `.get()` for safe retrieval.

  - No loops.
"""


names = ('Samuel', 'Adaora', 'Lovelace')
phone_numbers = ('080-Samuel', '081-Adaora', '070-Lovelace')
phonebook = dict(zip(names, phone_numbers))

# Using Control Loop
while True: #Loop Indefinitely
  requested = input(f"Whose Contact do you want to look up? {names}: ").title()
  if phonebook.get(requested.strip()) is not None:
    print(f"Phone Number for {requested}: {phonebook[requested]}")
  else:
    print("The requested contact could not be found in our library")
