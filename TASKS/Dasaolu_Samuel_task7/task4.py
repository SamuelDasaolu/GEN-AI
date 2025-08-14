"""
**Task4: Unique Members Registration**
- Ask the user to enter three names separated by commas.

   - Convert them to a set to ensure uniqueness.

   - Create a dictionary where each name is a key and its length is the value.

- Requirements:

   - Use `.split(",")` and `set()` to remove duplicates.

   - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.
"""
names_string = input("Enter three names(Separated by commas): ")
names_set = set(names_string.split(','))
members = {name: len(name) for name in names_set}
print(members)

print("Members Registered: ")
for name, length in members.items():
    print(f"Name: {name}, Length: {length}")