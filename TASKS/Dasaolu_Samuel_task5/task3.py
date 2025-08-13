"""
**Task3: Tuple Operations**
- Create a tuple of 5 Nigerian states entered by the user.

  - Print the first state and last state.

  - Check if "Lagos" is in the tuple and print "Yes" or "No".

  - Print the number of states entered.
    - (Hint: use the tuple membership)
"""

state_1 = input("Please Input State 1: ")
state_2 = input("Please Input State 2: ")
state_3 = input("Please Input State 3: ")
state_4 = input("Please Input State 4: ")
state_5 = input("Please Input State 5: ")

states = (state_1, state_2, state_3, state_4, state_5)
print(f"First State: {states[0]}")
print(f"Last State: {states[-1]}")
print(f"Is Lagos in States Entered: {'Lagos' in states or 'lagos' in states}")
print(f"Number of States Entered: {len(states)}")

