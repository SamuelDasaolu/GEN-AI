"""
file_path = workspace/ contacts.csv
Variables to Collect: name, age(strictly integer), phone number and track
Validate Inputs (Phone by length, non-empty etc)
handling Errors (reprompt if error)

details = {name, age, phone, track}
allow for multiple participants

"""

from pathlib import Path
import file_ops as op
from TASKS.Dasaolu_Samuel_task11.participant_pkg.file_ops import load_participants


def ask_user(detail, message=''):
    return input(f"Participant {detail} ({message if message else ''}): ")


while True:
    # Name Collection and Validation
    while True:
        name = input("Enter Participant Name: ").title()
        if name.strip() and len(name.strip().split()) == 2:
            break
        print('Name cannot be empty and must be of format: FirstName LastName e.g John Smith')

    # Age Collection and Validation
    while True:
        age = input("Enter Participant Age: ")
        if age and age.isdigit():
            age = int(age)
            break
        print("Age cannot be empty and must be a Whole Number")

    # Phone Number Collection and Validation:
    while True:
        phone_number = input("Enter Phone Number: ")
        if phone_number:
            if (phone_number.strip().startswith('+') or phone_number.strip().isdigit()) and len(phone_number) >= 10:
                break
            print("""
                Invalid Number Entered
                Phone Number can only be of Forms:
                0********* or +*************
                And is at least 10 digits
                """)
        print("Phone Number cannot be Empty")

    # Track Collection and Validation
    while True:
        track = input("Enter Participant Track: ")
        if track.strip():
            break
        print("Track cannot be empty")
    test_data = {
        'Name': name,
        'Age': age,
        'Phone Number': phone_number,
        'Track': track,
    }
    # Save and Read Participant Data
    workspace_path = Path("WORKSPACE_FILES")
    workspace_path.mkdir(exist_ok=True)
    file_path = workspace_path / 'contacts.csv'
    op.save_participant(file_path, test_data)
    print(f"Participant {name} saved successfully")

    # while True:
    save_another = input("Do you want to add another participant? (y/n): ").strip().lower()
    if save_another != 'y':
        break
    break


print("All Participants details collected successfully \n")

# Load Details
participants = load_participants(file_path)
print("\n📋 Final Summary:")
print(f"Total participants saved: {len(participants)}\n")
for i, p in enumerate(participants, start=1):
    name = p.get("Name", "N/A")
    age = p.get("Age", "N/A")
    phone = p.get("Phone", "N/A")
    track = p.get("Track", "N/A")

    print(f"{i}. {name} | Age: {age} | Phone: {phone} | Track: {track}")