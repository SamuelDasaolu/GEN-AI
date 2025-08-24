"""
**Task2: Unique Name Collector**
 - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
"""

attendees_list = set()
i = 1

try:
    while True:
        new_user = input("Please mark attendance with your name (or type 'done' to finish): ").strip()

        if not new_user:  # Handle empty input
            print("Name cannot be empty. Please enter a valid name.")
            continue

        if new_user.lower() == "done":  # Exit condition
            break

        if new_user in attendees_list:
            print("You can only mark attendance once daily")
            continue

        attendees_list.add(new_user)
        sorted_list = sorted(attendees_list)
        print(f"Attendees \n {sorted_list}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Attendance collection attempt finished.")
    print(f"Final Attendees List: {sorted(attendees_list)}")
