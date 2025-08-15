"""
**Task 7: List Manipulation**
- Create a list of five cities.

- Replace the third city with a new one (entered by the user).

- Remove the last city.

- Add a new city to the beginning of the list.

- Print the updated list.
"""
city_list = ['abk', 'lag', 'benin', 'ijemo', 'kuto']
print("City List: ", city_list)
replacement = input("Enter replacement city: ")
city_list[2] = replacement
print(f"New city list: ", city_list)
city_list.pop()
print("Last City Removed")
print("New City List: ", city_list)
beginning_city = input("Enter City to place at the beginning: ")
city_list.insert(0, beginning_city)
print(f"New City List: {city_list}")