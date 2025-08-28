import csv
from pathlib import Path


def save_participant(file_path: Path, participant_dictionary: dict):
    """Update A CSV file with a Participants Details 
    Creates A New File if it doesn't exist
    Creates Header if It Doesn't Exist"""
    try:
        with open(file_path, 'a', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['Name', 'Age', 'Phone Number', 'Track']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_path.exists():  # File is New, update headers
                writer.writeheader()

            # File Exists, update record
            writer.writerow(participant_dictionary)
    except Exception as e:
        print("An error occurred while saving: ", e)


def load_participants(file_path: Path) -> list:
    """This reads all participants from the CSV and 
    returns them as a list of dictionaries."""
    participants = []
    if not file_path.exists(): return participants

    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                participants.append(row)

    except Exception as e:
        print('An error occurred while loading participants: ', e)

    return participants
