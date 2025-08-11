"""
Task3: Pattern Matching & Splitting
11. Given "apple,banana,orange", split the string into a list of fruits.

12. Ask the user for a sentence and print each word on a new line.

13. Replace all spaces in a string with underscores (_).

14. Count how many times the letter "a" appears in "Banana".

15. Check if a given string starts with "https://".
"""

# Task 11
fruit_string = "apple,banana,orange"
fruit_list = fruit_string.split(',')
print(f"Fruit list: {fruit_list}")

# Task 12
user_sentence = input("Please input a sentence: ")
sentence_list = user_sentence.split(" ")
print(' \n'.join(sentence_list))

# Task 13
user_string = input("Input your desired string: ")
print(user_string.replace(' ', '~'))

# Task 14
word = "banana"
print(f"Letter 'A' appears {word.lower().count('a')} times")

# Task 15
url = input("Please input valid url(https://): ")
print(url.startswith("https://"))