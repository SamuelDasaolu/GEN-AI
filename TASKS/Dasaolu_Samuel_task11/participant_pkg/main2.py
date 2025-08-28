"""
file_path = workspace/ contacts.csv
Variables to Collect: name, age(strictly integer), phone number and track
Validate Inputs (Phone by length, non-empty etc)
handling Errors (reprompt if error)

details = {name, age, phone, track}
allow for multiple participants

"""

from pathlib import Path


def ask_user(detail, message = ''):
    return input(f"Participant {detail} ({message if message else ''}): ")

while True: 
    # Name Collection and Validation
    while True:
        name = input("Enter Participant Name: ").title()
        if name.strip() and len(name.strip().split()) == 2:
            break
        print('Name cannot be empty and must be of format: FirstName LastName e.g John Smith')
        
        
    #Age Collection and Validation    
    while True: 
        age = input("Enter Participant Age: ")
        if age and age.isdigit():
            break
        print("Age cannot be empty and must be a Whole Number")
        
    #Phone Number Collection and Validation:
    while True:
        phone_number = input("Enter Phone Number: ")
        if phone_number:
            if phone_number.strip().startswith('+') or phone_number.strip().isdigit() and len(phone_number) >= 10:
                print('Valid phone number')
                break
            print("""
                Invalid Number Entered
                Phone Number can only be of Forms:
                0********* or +*************
                """)
        print("Phone Number cannot be Empty")
        
    print('Outside the loop')
    break
