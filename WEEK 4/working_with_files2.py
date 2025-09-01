# from pathlib import Path

# workspace = Path("WORKSPACE_FILES")
# workspace.mkdir(exist_ok=True)
# file_path = workspace / "notes.txt"

# f = open(file_path, "w", encoding="utf-8")
# f.write("Shopping List:\n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()

# # Append safely
# with open(file_path, "a", encoding="utf-8") as f:
#     f.write(" - Build a small project\n")

# # Try to read a file that doesn't exist
# try:
#     with open(workspace / "missing_file.txt", "r") as f:
#         content = f.read()
#         print("File content:", content)
# except FileNotFoundError:
#     print("Oops! That file doesn't exist yet.")
#     print("Let's create it first!")
    
#     # Now create the file
#     with open(workspace / "missing_file.txt", "w") as f:
#         f.write("Now I exist!")
#     print("File created successfully!")


# # Write safely
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("My Todo List:\n")
#     f.write(" - Revise Python file handling\n")
#     f.write(" - Practice error handling within a function")
#     f.write(" - Practice JSON & CSV\n")
    

# workspace = Path("workspace_files") ##CASE_Insensitve
# file_path = workspace / "NOTES.txt" ##Also case insensitive on windows

# # Check if our file exists
# if file_path.exists():
#     print(f"Found the file: {file_path.name}")
    
#     # Get some information about the file
#     file_size = file_path.stat().st_size
#     print(f"File size: {file_size} bytes")
    
#     # Read and show the content
#     with open(file_path, "r", encoding="utf-8") as f:
#         content = f.read()
#         print(f"Content preview: {content[:50]}...")  # First 50 characters
# else:
#     print(f"File {file_path.name} doesn't exist")
#     print("You might want to create it first!")
    

import json
from pathlib import Path

workspace = Path("workspace_files")

# Create some student data (like a mini database)
student_data = {
    "name": "Oyindamola",
    "age": 16,
    "courses": ["Python", "Data Science", "Web Development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
}

# Save the data to a JSON file
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2)  # indent=2 makes it pretty and readable

print("Student data saved to JSON file!")

# Now read it back
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("\nData read from JSON file:")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Courses: {', '.join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")


# import csv
# from pathlib import Path

# workspace_folder = Path("WORKSPACE_FILES")
# csv_file_path = workspace_folder/'students.csv'

# students = [
#     ["Name", "Age", "Course", "Grade"],
#     ["Precious", 20, "Python", "A"],
#     ["Favour", 22, "JavaScript", "B+"],
#     ["Ore", 21, "Python", "A-"],
#     ["Susan", 23, "Data Science", "A"]
# ]

# with open(csv_file_path, 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file) #Creates file
#     writer.writerows(students)
# print("Students data written to CSV file!")

# # Read the CSV file back
# print("\nReading CSV file:")
# with open(csv_file_path, "r", encoding="utf-8") as file:
#     reader = csv.reader(file)

    
#     for row_number, row in enumerate(reader):
#         if row_number == 0:  # Header row
#             print(f"Headers: {' | '.join(row)}")
#             print("-" * 40)
#         else:  # Data rows
#             name, age, course, grade = row
#             print(f"{name} ({age} years) - {course}: {grade}")

# from pathlib import Path

# workspace = Path("workspace_files")
# input_file = workspace / "original.txt"
# output_file = workspace / "processed.txt"

# # Create an input file with some text
# sample_text = """hello world
# python programming
# file handling tutorial
# learning is fun"""

# with open(input_file, "w", encoding="utf-8") as f:
#     f.write(sample_text)

# print("Created input file")

# # Process the file: read from input, write processed version to output

# with open(input_file, 'r', encoding='utf-8')as infile, open(output_file, 'w', encoding='utf 8') as outfile:
#     for line_number, line in enumerate(infile):
#         # Process each line: make it uppercase and add line numbers
#         processed_line = f"Line {line_number+1}: {line.strip().upper()}\n"
#         outfile.write(processed_line)

# print("File processing complete!")

# # Show the results
# print("\nOriginal file:")
# with open(input_file, "r", encoding="utf-8") as f:
#     print(f.read())

# print("\nProcessed file:")
# with open(output_file, "r", encoding="utf-8") as f:
#     print(f.read())

from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "story.txt"

# Create a sample story file
story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
she just want to know how things work behind the scene. 
Eventually she had an opportunity to hopp into the world of programming for the first time.
She started with python, now she codes in Python every day.
One day, she discovered file handling.
It opened up a whole new world of possibilities!
The end."""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(story)

print("Created a story file!")

# Now let's explore moving around in the file
with open(file_path, "r", encoding="utf-8") as f:
    print("\nFile positioning demo:")
    
    # Read first 20 characters
    first_part = f.read(20)
    print(f"First 20 characters: '{first_part}'")
    
    # Check where we are now
    current_position = f.tell()
    print(f"Current position in file: {current_position}")
    
    # Jump to the beginning
    f.seek(0)
    print(f"After seeking to beginning: position {f.tell()}")
    
    # Jump to position 50 and read from there
    f.seek(50)
    rest_of_line = f.readline()
    print(f"Reading from position 50: '{rest_of_line.strip()}'")
    
    # Go back to beginning and read the first line
    f.seek(0)
    first_line = f.readline()
    print(f"First line: '{first_line.strip()}'")