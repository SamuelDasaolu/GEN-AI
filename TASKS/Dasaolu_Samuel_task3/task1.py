"""

1. Write a program to take a string input from the user and display it in uppercase.

2. Given the string "python", print its first and last characters.

3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.

4. Write a program to count the number of characters in a string without using len().

5. Given "Hello World", replace "World" with "Python"."""

# Task 1
text_to_convert = input("Please enter text to convert: ")
print(f"Corrected text is {text_to_convert.upper()}")

# Task 2
word = "python"
print(f"First Letter: {word[0]}, Last Letter {word[-1]}")

# Task 3
user_name = input("What is your name? ")
print(f"Hello, !".replace('!', user_name))

# Task 4
word_to_count = input("Type text to count: ")
last_character = word_to_count[-1]
print(f"It contains {word_to_count.rindex(last_character) + 1} characters \n")

# Task 5
print("Hello World".replace('World', 'Python'))