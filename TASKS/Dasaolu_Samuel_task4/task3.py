"""
**Task 3: Word Counter**
- Ask the user for a sentence.

- Split the sentence into a list of words.

- Print how many words are in the sentence.
"""

sentence = input("Please input sentence: ")
sentence_list = sentence.split(' ')
print(f"There are {len(sentence_list)} words in the sentence")
