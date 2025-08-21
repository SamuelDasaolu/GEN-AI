"""
**Task2: Unique Name Collector**
 - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
"""

attendees_list = set()
i = 1
while True:
    new_user = input("Please mark attendance with your name: ")
    if new_user in attendees_list:
        print("You can only mark attendance once daily")
        continue
    attendees_list.add(new_user)
    sorted_list = sorted(attendees_list)
    print(f"Attendees \n {sorted_list}")