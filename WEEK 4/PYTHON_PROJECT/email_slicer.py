"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""

def slice_email(email: str) -> tuple:
    # Validate email
    if '@' in email and '.' in email.split('@')[1]:
        username = email.split('@')[0]
        domain = email.split('@')[1]
        
        return username, domain
    return None, None
    


while True:
    email = input("Enter Email Address: ")
    username, domain = slice_email(email)
    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else: print("The email you have entered is invalid")