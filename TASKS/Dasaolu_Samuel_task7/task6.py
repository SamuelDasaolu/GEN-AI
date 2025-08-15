"""
**Compulsory Task(but not graded): Student Profile Builder**

- This program collects student details, academic scores, hobbies, and guardian 
info, stores them in a nested dictionary, and performs automatic calculations and 
transformations using dictionary comprehension, tuple unpacking, and set operations.
"""


# Basic Info
name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter gender (Male/Female): ")

# Academic Scores (3 subjects)
subjects = ("Math", "English", "Science")
scores = tuple(float(input(f"Enter score for {subj}: ")) for subj in subjects)

# Guardian Info
guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

# Hobbies - ensure uniqueness with set
hobbies_input = input("Enter at least 3 hobbies (comma-separated): ")
hobbies_set = set(h.strip() for h in hobbies_input.split(","))

# Student Dictionary
student_profile = {
    "Basic Info": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.capitalize()
    },
    "Academics": {subj: score for subj, score in zip(subjects, scores)},
    "Guardian": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone
    },
    "Hobbies": list(hobbies_set)
}

# Derived Data
student_profile["Academics"]["Average"] = sum(scores) / len(scores)
student_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

# Output Section
print("\n\t=== STUDENT PROFILE ===")
print(f"Name:\t\t{student_profile['Basic Info']['Name']}")
print(f"Age:\t\t{student_profile['Basic Info']['Age']}")
print(f"Gender:\t\t{student_profile['Basic Info']['Gender']}")
print(f"Initials:\t{student_profile['Basic Info']['Initials']}")
print("\n--- Academic Scores ---")
print(student_profile["Academics"])
print("\n--- Guardian Info ---")
print(student_profile["Guardian"])
print("\n--- Hobbies ---")
print(student_profile["Hobbies"])
print(f"\nTotal Hobbies:\t{student_profile['Hobbies Count']}")
print(f"Average Score:\t{student_profile['Academics']['Average']:.2f}")
