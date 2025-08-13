"""
**Task4: Tuple Unpacking**
 - Ask a user for their;

  - First name

  - Age

  - Favorite color

  - Home town

  - Store them in a tuple profile and unpack into variables.

  - Print and use  escape sequence to align each piece of information nicely.
  """

profile = input("First Name: "), input("Age: "), input("Favorite Colour: "), input('Home Town: ')
name, age, fav_colour, home_town = profile
print(f"Name: {name} \n Age: {age} \n Favorite Colour: {fav_colour} \n Home town: {home_town}")
