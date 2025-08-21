"""

1. Write a program to take a string input from the user and display it in uppercase.

2. Given the string "python", print its first and last characters.

3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.

4. Write a program to count the number of characters in a string without using len().

5. Given "Hello World", replace "World" with "Python"."""


# Task 4
#OR (using for control loop)
count = 0
for ch in word_to_count:
    count+=1
print(f"It contains {count} characters (Counted using for loop)\n")


# Task 5
#OR using control loop
sentence = 'Hello World'
sentence_list = sentence.split(' ')
count = 0
for word in sentence_list:
    if word == 'World':
        sentence_list[count] = 'Python'
    count+=1

print(' '.join(sentence_list), 'Using for Control Loop')