"""
Task2

6. Check if a given string contains the substring "python" (case-insensitive).

7. Write a program to reverse a string without using slicing ([::-1]).

8. Given a string with extra spaces, remove the leading and trailing spaces.

9. Ask the user to enter a sentence and print the number of vowels in it.

10. Convert a string "1234" to an integer and multiply it by 2.
"""

# Task 6
text_to_check = input("Input Text to check for python(case insensitive): ")
print("True") if 'python' in text_to_check.lower() else print("False")
# OR
print('python' in text_to_check.lower())

# Task 7
string_to_reverse = input("Input string to reverse: ")
# for each in reversed(string_to_reverse): 
#     print(each)
list = reversed(string_to_reverse)
print(''.join(list))

# Task 8
string_with_spaces = " I have trailing spaces "
print(string_with_spaces.strip())

# Task 9
sentence = input("Please, enter your sentence: ").lower()
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_count = sum(1 for letter in sentence if letter in vowel_list)
print(f"There are {vowel_count} vowels")
vowel_count = sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
print(f"There are {vowel_count} vowels")

# Task 10
string_number = input("Your number to multiply: ")
string_number_converted = int(string_number)
print(f"The answer is: {string_number_converted*2}")

