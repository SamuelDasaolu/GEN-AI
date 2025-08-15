"""
**Task3: Days and Activities Pairing**
- Store days of the week in a tuple and ask the user to input an activity for three specific days.

  - Use dictionary comprehension to pair days and activities.

  - Print the dictionary.

- Requirements:

  - Use a tuple for days.

  - Use {day: activity for day, activity in `zip(..., ...)`}.
  Tip: Research on how to use `zip()`
"""
days_tuple = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
activities_tuple = ('sunday_act', 'monday_act', 'tuesday_act', 'wednesday_act', 'thursday', 'friday')
zipped_data = zip(days_tuple, activities_tuple)
activities_pairing = {day: activity for day, activity in zipped_data}
days_string = input("Input three days to specify activity for(separated by commas): ").lower()
user_activity = input('Input activity to specify: ')
days_to_edit = days_string.split(',')
for day in days_to_edit:
  activities_pairing.update({day.strip(): user_activity})

print("Activities Pairing: ", activities_pairing)
