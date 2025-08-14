# student = {
#     "name": "Ada",
#     45: 20,
#     ('apple', 'ball'): "Computer Science"
# }
# print(student)

# Using the dict() constructor
# student_info = dict(name="John", age=25, course="Maths")
# print(student_info)

# empty_dict = {}
# print(empty_dict)

# # Create a dictionary of numbers and their squares
# squares = {x: x**2 for x in range(1, 6)}
# print(f" Squares: {squares}")
# evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
# print(f"Evens Cube: {evens_cube}")
# odds_cube = {x: x**3 for x in range(1, 10) if x % 2 != 0}
# print(f"Odds Cube {odds_cube}")

# #  From Existing Dictionary
# students = {"Ada": 85, "John": 40, "Musa": 65}
# # Filter students who passed (score >= 50)
# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)
# for name, score in students.items(): 
#     if score <= 50:
#         failed_students = {name: score} 
        
# print(f"Failed Students: {failed_students}")

# # Using String Keys
# names = ["Ada", "John", "Musa", "Musa", "John"]
# lengths = {name: len(name) for name in names}
# print(lengths) #Simply ignores duplicate keys

# # Define a dictionary
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# student['grade'] = 'JJS2'
# # Using key
# print(student["name"])
# # Using get() method (avoids error if key is missing)
# print(student.get("age"))
# print(student.get("grade", "Not Found"))

# 1.  Using pop()
# student.pop("grade")

# # 2. Using popitem() - removes last inserted key-value
# student.popitem()

# # 3. Using del keyword
# del student["course"]

# # 4. Using clear() - removes all items
# student.clear()

# # 4. update()
# student.update({"age": 31, "city": "Lagos"}) #Adds key/value pair if it doesn't exist
# print(student)

# students = {
#     "student1": {"name": "Ada", "age": 20},
#     "student2": {"name": "John", "age": 22}
# }

# print(students["student1"]["name"])  # Access nested data

student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# # Loop through keys
# for key in student:
#     print(key)
    
# # Loop through values
# for value in student.values():
#     print(value)

# Loop through key-value pairs
# for key, value in student.items():
#     print(f"{key}: {value}")

# Storing a student's biodata
# student = {
#     "name": "Chinedu",
#     "age": 19,
#     "department": "Engineering",
#     "subjects": ["Maths", "Physics", "Chemistry"],
#     "is_full_time": True
# }

# print(f"Name: {student['name']}")
# print(f"Subjects: {', '.join(student['subjects'])}")