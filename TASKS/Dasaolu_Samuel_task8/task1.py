"""
**Task1**
- Explain each output of the program below.
- Give 3 usecases or cenarios where you can apply the program below.
- Write the code for 1 of the 3 use cases.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# Explanation: Outputs True if num1 and num2 are the same, else, False
print(f"{num1} != {num2} : {num1 != num2}")
# Explanation: Outputs True if num1 and num2 are different, else, False
print(f"{num1} > {num2} : {num1 > num2}")
# Explanation: Outputs True if  num1 is strictly greater than num2, else False
print(f"{num1} < {num2} : {num1 < num2}")
# Explanation: Outputs True if num1 is strictly less than num2, else False

# USECASES
# CASE1: Age verification systems for users
# CASE2: Score verification systems for school management systems
# CASE3: Filtering from a list, set, e.t.c

# Example for case 3:
# This program filters students who passed or failed 
# in a bigger dictionary using operators
disctintion_score = 90
pass_score = 50

students = {'Samuel': 90,
            'Paul': 75, 
            'John': 70, 
            'Smith': 73, 
            'Ada': 67, 
            'Peter': 69, 
            'Lovelace': 95, 
            'David': 99, 
            'James': 40, 
            'Edward': 29, 
            }

distinction = {name: score for name, score in students.items() if score >= disctintion_score}
passed = {name: score for name, score in students.items() if score >= pass_score}
failed = {name: score for name, score in students.items() if score < disctintion_score}

print(f"Distinction Students: {distinction}")
print(f"Pass Students: {passed}")
print(f"Fail Students: {failed}")