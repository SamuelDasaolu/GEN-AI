"""
**Task2**
- Comment the code below appropriately, and using doctring, explain what the code is doing.
-  Adapt the code to the case below.

- Federal Government Scholarship Key Eligibility Requirements:
  - Citizenship:
    - Applicant must be a citizen of Nigeria. 
  - Enrollment:
    - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
  - Other Scholarships:
    - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
  - Academic Qualification:
    - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
"""
# # variable declaration 
# name = input("Enter your name: ")
# age = int(input("Enter your age: ")) #Typecasting to integers
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)  #Condition for eligibility: is underage and passing grade
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}") #Print Result
"""
What the code above does is compute eligibility based on age and score
"""

# FEDERAL GOVERNMENT ELIGIBILITY
name = input("Applicant's Name: ")
country = input('Country of Origin: ')
enrollment_status = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university? (Yes/No): ")
other_schorlarships_status = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international? (Yes/No): ")
print("---O'level Results Verification---")
results = { #Stored in Dictionary
    'Mathematics': input("Score for Mathematics (A, B, C, D, E or F): ").upper(),
    'English': input("Score for English (A, B, C, D, E or F): ").upper(),
    'Computer': input("Score for Computer (A, B, C, D, E or F): ").upper(),
    'Biology': input("Score for Biology (A, B, C, D, E or F): ").upper(),
    'Physics': input("Score for Physics (A, B, C, D, E or F): ").upper(),
    'Chemistry': input("Score for Chemistry (A, B, C, D, E or F): ").upper(),
    'Economics': input("Score for Economics (A, B, C, D, E or F): ").upper(),
    'Geography': input("Score for Geography (A, B, C, D, E or F): ").upper(),
    'Civic': input("Score for Civic Education (A, B, C, D, E or F): ").upper(),
}

passed_maths = (results['Mathematics'].upper().strip() == 'A') or (results['Mathematics'].upper().strip() == 'B')
passed_english = (results['English'].upper().strip() == 'A') or (results['English'].upper().strip() == 'B')
no_of_distinctions = ((list(results.values()).count('A')) + (list(results.values()).count('B')))
# Eligibility Computation
country_eligible = country.title().strip() == 'Nigeria'
enrollment_status_eligible = enrollment_status.lower().strip() == 'yes'
other_schorlarships_status_eligible = other_schorlarships_status.lower().strip() != 'yes'
academic_qualification_eligible = passed_maths and passed_english and (no_of_distinctions >= 5)
overall_eligible = country_eligible and enrollment_status_eligible and other_schorlarships_status_eligible and academic_qualification_eligible

print('\n\t\t --- RESULTS --- \n')
print(f"Country Eligibility: {country_eligible}")
print(f"Enrollment Status Eligibility: {enrollment_status_eligible}")
print(f"Student not on Other Schorlarships: {other_schorlarships_status_eligible}")
print(f"Passed Maths: {passed_maths}")
print(f"Passed English: {passed_english}")
print(f"Number of Distinctions: {no_of_distinctions}")
print(f"Academically Qualified: {academic_qualification_eligible} \n\n")

print(f"Candidate: {name.title()}\nCountry: {country.capitalize()}\nOther Scholarships: {other_schorlarships_status.capitalize()}\nEligible: {overall_eligible}") #Print Result