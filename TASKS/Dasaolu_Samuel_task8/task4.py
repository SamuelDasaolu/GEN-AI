"""
**Task4: Student Record**
- Create an empty dictionary called student.

- Ask the user to input their name and age, then store them in the dictionary.

- Add a list of scores (e.g., [70, 85, 90]) to the dictionary.

- Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

- Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

- Print out the complete record in this format:

```
Student Record:
Name: John
Age: 16
Scores: [70, 85, 90]
Passed: True
Teenager: True
```
"""

student = {'ala': 23}
name = input("Student Name: ")
age = int(input("Student Age: "))
student.update({'name': name, 'age': age})
student.update({'scores': [70, 85, 90]})
student.update({'passed': (sum(student['scores'])/len(student['scores'])) >= 50})
is_teenager = (student['age'] >= 13) and (student['age'] <= 19)
student.update({'teenager': is_teenager})

print(f"""
```
Student Record:
Name: {student['name'].title()}
Age: {student['age']}
Scores: {student['scores']}
Passed: {student['passed']}
Teenager: {student['teenager']}
```
""")