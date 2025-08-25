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

try:
    names = input("Enter 3 student names (separated by commas): ").strip()
    if not names:
        raise ValueError("No names entered. Please provide student names.")

    name_list = names.split(',')

    if len(name_list) != 3:
        raise ValueError("You must enter exactly 3 student names.")

    # Using Control Loop
    for name in name_list:
        formatted_name = name.strip().title()

        while True:  # keep asking until valid score is entered
            try:
                score = int(input(f"Enter score for {formatted_name}: ").strip())
                break
            except ValueError:
                print("Invalid score. Please enter a valid integer.")

        student_list.append(formatted_name)
        score_list.append(score)

    # formatted output
    print("\nStudent\t\tScore")
    print("-------------------------")
    for i in range(len(student_list)):
        print(f"{student_list[i]:<15}{score_list[i]}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("\nStudent score tracking attempt finished.")
