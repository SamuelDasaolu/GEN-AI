"""
**Task2: Unique Name Collector**
 - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
"""

attendees_list = set()
while True:
    new_user = input("Please mark attendance with your name: ")
    attendees_list.add(new_user)
    sorted_list = sorted(attendees_list)
    print(f"Attendees \n {sorted_list}")