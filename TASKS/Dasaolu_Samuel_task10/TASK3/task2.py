"""
Task2

6. Check if a given string contains the substring "python" (case-insensitive).

7. Write a program to reverse a string without using slicing ([::-1]).

8. Given a string with extra spaces, remove the leading and trailing spaces.

9. Ask the user to enter a sentence and print the number of vowels in it.

10. Convert a string "1234" to an integer and multiply it by 2.
"""

# Task 7
#Using Control
string_to_reverse = input("Input string to reverse: ").strip()
i = -1
reversed_word = ''
for ch in string_to_reverse:
    reversed_word+=string_to_reverse[i]
    i-=1
print(f"Reveresed String: {reversed_word}")

# Task 9
#Using Control
sentence = input("Please, enter your sentence: ").lower()
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_count = sum(1 for letter in sentence if letter in vowel_list)
print(f"There are {vowel_count} vowels")
