"""
**Task4: Create a Unique Voters Registration System**

- Ask for voter names and store in a set.
- If a voter tries to register twice, display a warning.
- After registration, display the total number of unique voters.
"""

registered_voters = set()

try:
    while True:
        new_user = input("Please register with your name (or type 'done' to finish): ").strip().lower()

        if not new_user:  # empty input check
            print("Name cannot be empty. Please enter a valid name.")
            continue

        if new_user == "done":  # exit condition
            break

        if new_user in registered_voters:
            print("Warning: you've already been registered")
        else:
            registered_voters.add(new_user)

        print(f"Total Number of Unique Voters: {len(registered_voters)}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Voter registration session ended.")
    print(f"Final Total Unique Voters: {len(registered_voters)}")
    print(f"Registered Voters: {registered_voters}")
