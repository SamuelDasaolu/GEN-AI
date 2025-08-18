"""
**Task6**

- The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 

- For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 

Breakdown of the Admission Process:
1. UTME:
Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
2. O'Level Requirements:
Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
3. Post-UTME:
Eligible candidates participate in the university's online Post-UTME screening. 
4. Departmental Cut-off Marks:
After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
(This can range from 200 to 320). 
5. Final Admission:
Candidates who meet the departmental cut-off marks are offered admission. 

- Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.
"""

# Declare Needed Variables
name = input("Enter Candidate Name: ").strip().title()
age = int(input("Enter Candidate Age: "))
first_choice = input("Enter First Choice University: ").strip().lower()
utme_score = int(input("Enter Candidate UTME SCORE(/400): "))
results = { #Stored in Dictionary
    'Mathematics': input("Score for Mathematics (A, B, C, D, E or F): ").upper().strip(),
    'English': input("Score for English (A, B, C, D, E or F): ").upper().strip(),
    'Computer': input("Score for Computer (A, B, C, D, E or F): ").upper().strip(),
    'Biology': input("Score for Biology (A, B, C, D, E or F): ").upper().strip(),
    'Physics': input("Score for Physics (A, B, C, D, E or F): ").upper().strip(),
    'Chemistry': input("Score for Chemistry (A, B, C, D, E or F): ").upper().strip(),
    'Economics': input("Score for Economics (A, B, C, D, E or F): ").upper().strip(),
    'Geography': input("Score for Geography (A, B, C, D, E or F): ").upper().strip(),
    'Civic': input("Score for Civic Education (A, B, C, D, E or F): ").upper().strip(),
}

# Determine Conditions for Eligibility
age_eligible = age >= 16
utme_eligible = utme_score >= 200
uni_eligible = first_choice == 'unilag'
no_of_credits = (list(results.values()).count('A')) + (list(results.values()).count('B')) + (list(results.values()).count('C'))
passed_maths = (results['Mathematics'].upper().strip() == 'A') or (results['Mathematics'].upper().strip() == 'B') or (results['Mathematics'].upper().strip() == 'C')
passed_english = (results['English'].upper().strip() == 'A') or (results['English'].upper().strip() == 'B') or (results['English'].upper().strip() == 'C')

if age_eligible and utme_eligible and uni_eligible and passed_maths and passed_english and (no_of_credits >= 5):
    print("You are eligible to take the POST UTME Examination")
    putme_score = int(input("Enter Candidate POST-UTME SCORE(/320): "))
    passed_putme = (putme_score >= 200) and (putme_score <= 320)
    
    # ELIGIBILITY RESULTS
    print('\n\t\t --- RESULTS --- \n')
    print(f"UTME Eligibility: {utme_eligible}")
    print(f"PUTME Eligibility: {passed_putme}")
    print(f"Passed Maths: {passed_maths}")
    print(f"Passed English: {passed_english}")
    print(f"Number of Credits: {no_of_credits}")
    print("\n\t\t----Final Admission Status----\n")
    print(f"Congratulations {name.title()}\n YOU ARE ELIGIBLE FOR ADMISSION")
    
else:
    print("\n\t\t----Final Admission Status----\n")   
    print("Sorry, you are not eligible to take the POST UTME Examination")
    print("You are not eligible for Admission")
