"""
Task3: Pattern Matching & Splitting
11. Given "apple,banana,orange", split the string into a list of fruits.

12. Ask the user for a sentence and print each word on a new line.

13. Replace all spaces in a string with underscores (_).

14. Count how many times the letter "a" appears in "Banana".

15. Check if a given string starts with "https://".
"""

# Task 12
#using Control Loop
user_sentence = input("Please input a sentence: ")
sentence_list = user_sentence.split(" ")
for word in sentence_list:
    print(word, '\n')

# Task 13
#Using Control Loop
user_string = input("Input your desired string: ")
new_string = ''
for ch in user_string:
    if ch == ' ':
        ch = '~'
    new_string+=ch
print('New String: ', new_string, '\n')

# Task 14
#Using Control Loop
word = "banana"
count = 0
for ch in word:
    if ch == 'a':
        count+=1
print(f"Letter 'A' appears {count} times in the word banana")