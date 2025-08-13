"""
**Task6: Attendance Tracker**
- Write a Python program that;

 - Stores the days of the week in a tuple.

 - Stores the months of the year in another tuple.

 - Asks the user to enter:

   - Student’s name

   - Gender

   - Course Track
   
   - Current month number (1-12)

   - Current day number (1-7)
"""
days_tuple = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
months_tuple = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
profile = (input('Name: '), input('Gender: '), input('Course Track: '), int(input('Current Month Number: ')), int(input('Current Day Number: ')))
current_month = months_tuple[profile[3]]
current_day = days_tuple[profile[4]]

print(f"Student {profile[0]}, you have just marked attendance for {current_day.title()} in {current_month.title()}")