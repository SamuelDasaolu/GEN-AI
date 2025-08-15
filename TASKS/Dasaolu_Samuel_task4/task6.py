"""
**Task 6: Word Analyzer**
- Ask the user to input a word.

- Print the length of the word.

- Check if it is all uppercase, all lowercase, or title case.

- Reverse the word using slicing.
"""

word = input('Please input your word: ')
print(f"Your word has {len(word)} characters")
if word.isupper(): print("Word is Uppercase")
if word.islower(): print("Word is Lowercase")
if word.istitle(): print("Word is Titlecase")
print(f"Reversed word is: {word[::-1]}")