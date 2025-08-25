"""
**Task4: Create a Unique Voters Registration System**

- Ask for voter names and store in a set.

- If a voter tries to register twice, display a warning.

- After registration, display the total number of unique voters.
"""

registered_voters = set()
while True:
    new_user = input("Please register with your name: ").lower()
    print("Warning: you've already been registered") if new_user in registered_voters else registered_voters.add(new_user)
    print(f"Total Number of Unique Voters: {len(registered_voters)}")