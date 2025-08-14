names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Zipping two lists
zipped_data = zip(names, ages)

# Converting the zip object to a list for viewing
list_of_tuples = dict(zipped_data)
print(list_of_tuples)

# Iterating through zipped data
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")