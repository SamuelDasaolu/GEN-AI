# import os

# print("Current working directory:", os.getcwd())
# # Absolute path example
# absolute_path = r"C:\Users\Chris\Desktop\my_path.py" # r"" is raw string formatter
# # Relative path example
# relative_path = "my_path.py"

# print("Absolute Path:", absolute_path)
# print("Relative Path:", relative_path)

# import os

# folder = "C:/Users/Chris/Desktop"
# filename = "my_path.py"

# new_path = os.path.join(folder, filename)
# print("Full path:", new_path)

# path = "working_with_files.py"

# if os.path.exists(path):
#     print("Yes, the file exists!")
# else:
#     print("File not found.")

# from pathlib import Path

# # Current working directory
# print("Current directory:", Path.cwd())

# # Create a Path object
# file = Path("myfile.txt").absolute()
# print(f"file: {file}")

# # Check if it exists
# print("File exists:", file.exists())

# # Combine paths
# folder = Path("C:/Users/Chris/Desktop")
# full_path = folder / "myfile.txt"
# print("Full path:", full_path)

from pathlib import Path

# Get parent folder of current file
print("Parent folder:", Path.cwd().parent)

# List all files in a directory
for file in Path.cwd().iterdir():
    print(file)