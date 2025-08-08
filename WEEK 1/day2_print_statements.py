#Basic Usage
print('1. Hello World')
print('2. Welcome to python programming language')

# Using print with variables
name = "Samuel"
age = 23
print("3. Name:", name)
print("4. Age:", age)

# Using formatted strings with print()
name = "Bola"
score = 92
print(f"{name} scored {score} in the exam.")

# Using string concatenation
first_name = "Samuel"
last_name = "Dasaolu"
print("Full name: " + first_name + " " + last_name)


# Comma vs concatenation
print("Hello", "world!")       # With comma
print("Hello" + " " + "world!")  # With concatenation

# Escape sequences in print - "\n", "\t"
print("Line1\nLine2")              # New line
print("Item1\tItem2")              # Tab space
print("He said, \"Hello\"")        # Quoted string
print('It\'s Python!')             # Apostrophe in single quote

# Newline (\n)
print("Welcome to Python\nLet's learn together!")

# Tab (\t)
print("Name\tAge\tLocation")
print("Aisha\t25\tLagos")

# Quotes inside string
print("She said, \"Hello there!\"")
print('It\'s a sunny day.')

# Backslash
print("File path: C:\\Users\\Aisha\\Documents")

#fun little pyramid scheme
print(
    '\t', '|||||||||\n' 
    '\t', ' |||||||\n' 
    '\t', '  |||||\n'
    '\t', '   |||\n'
    '\t', '    |\n' 
)
print(
    '\t', '    |\n'
    '\t', '   |||\n'
    '\t', '  |||||\n'
    '\t', ' |||||||\n' 
    '\t', '|||||||||\n' 
)

print('\t', '|||||||||\n\t', ' ||||||| \n\t', '  ||||| \n\t    |||\n\t     |\n')
print('\t', '    |\n\t', '   |||\n\t', '  |||||\n\t',' |||||||\n\t','|||||||||')



print('''\t\t
    |||||||||
     |||||||
      |||||
       |||
        |
''')
# shape = input('Type Character you want to use as your pyramid shape: ')
# n=int(input("Please input number of lines: "))
# i=1
# while i<=n:
#     print(
#         f'''{shape}'''
#     )
#     i+=1

# '''