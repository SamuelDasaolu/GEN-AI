"""
**Task 5: Student Score Tracker**

- Ask the user for 3 student names.

- For each student, ask for their score.

- Store the results in two lists (one for names, one for scores).

- Print a formatted output showing Name — Score, aligned neatly.
  - Tips: You are to start by creating two empty lists.
"""

student_list = []
score_list = []

names = input("Enter 3 student names(separated by commas): ")
name_list = names.split(',')
#using Control Loop
for name in name_list:
  formatted_name = name.strip().title()
  score = int(input(f"Enter score for {formatted_name}: ").strip())
  student_list.append(formatted_name)
  score_list.append(score)
  
print(f"""
Student \t\t Score \n
{student_list[0]} \t\t {score_list[0]}\n
{student_list[1]} \t\t {score_list[1]}\n
{student_list[2]} \t\t {score_list[2]}\n
""")