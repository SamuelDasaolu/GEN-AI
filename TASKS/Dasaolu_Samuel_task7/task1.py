"""
**Task1: Student Bio Data Storage**

- Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.

  - Courses should be stored as a list.

  - Display the bio-data neatly using escape sequences.

- Requirements:

  - Use `input()` to collect details.

  - Use dictionary operations `(dict[key] = value)` to store data.

  - Use `print()` formatting with `\n` and `\t` for better output.
"""
student_profile = {
    'name' : input('Name: '),
    'age' : int(input('Age: ')),
    'gender' : input('Gender: '),
    'courses' : (input('Courses(separated by commas): ').split(', ')),
}
for key, value in student_profile.items():
    if type(value) is list:
        value = ', '.join(value) #Turns Courses back to string
    print(f'\t {key} : {value} \n')
    
