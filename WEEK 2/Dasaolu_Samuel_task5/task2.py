"""**Task2: Tuple and Input**

- Ask the user for 5 best friends’ names.

- Store them in a tuple friends.

- Print the tuple in reverse order.
"""

print("Please Enter your best friend's names")
bestfriend_1 = input("Best Friend 1: ")
bestfriend_2 = input("Best Friend 2: ")
bestfriend_3 = input("Best Friend 3: ")
bestfriend_4 = input("Best Friend 4: ")
bestfriend_5 = input("Best Friend 5: ")

friends = (bestfriend_1, bestfriend_2, bestfriend_3, bestfriend_4, bestfriend_5)
reversed_friends_string = ', '.join(reversed(list(friends)))
reversed_friends_list = reversed_friends_string.split(', ')
reversed_friends_tuple = tuple(reversed_friends_list)

print(reversed_friends_tuple)
