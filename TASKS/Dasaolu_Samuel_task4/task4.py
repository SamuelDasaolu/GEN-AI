"""
**Task 4: Name Organizer**
- Ask the user to enter 5 names (separated by spaces).

- Convert all names to lowercase.

- Sort the list alphabetically.

- Display them one name per line.
  -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 
"""

name_string = input("Please enter 5 names separated by spaces: ").lower()
name_list = name_string.split(' ')
name_list.sort()
for name in name_list: print(name)