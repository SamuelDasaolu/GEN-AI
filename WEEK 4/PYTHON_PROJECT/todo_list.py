# @title 2. To-Do List Application

"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""

from pathlib import Path
import json
data = {

    'ongoing_tasks': {

    },

    'completed_tasks': {

    },
}

workspace = Path("WORKSPACE_FILES")
workspace.mkdir(exist_ok=True)
file_path = workspace / 'todolist.json'


def add_task(task: str):
    """Collects Task Information and Adds to To-do List"""

    if not file_path.exists():
        length = len(data['ongoing_tasks'])
        data['ongoing_tasks'][f"TASK {length+1}"] = task
        with open(file_path, 'w', encoding='utf-8', newline='') as save_file:
            json.dump(data, save_file, indent=2)
    else:
        with open(file_path, 'r', encoding='utf-8') as save_file:
            data = json.load(save_file)

        length = len(data['ongoing_tasks'])
        data['ongoing_tasks'][f"TASK {length+1}"] = task

        with open(file_path, 'w', newline='') as save_file:
            json.dump(data, save_file)

    print(f"\n Task ({task}) added successfully \n")


def remove_task(task):
    if task in list(todo.values()):
        todo.pop
        print(f"Task ({task}) removed successfully")
    else:
        print("Task not found")


def display_todo():
    if todo:
        print("TASKS In YOUR LIST")
        for index, task in enumerate(todo, 1):
            print(f"Task {index}. {task.capitalize()}")
    else:
        print("You haven't aadded any tasks to your list.")


def display_completed():
    if completed_tasks:
        print('Completed Tasks')
        for index, task in enumerate(completed_tasks, 1):
            print(f" Task {index}: {task}")


def mark_complete(task):
    if task in todo:
        todo.remove(task)
        completed_tasks.append(task)
        print(f"Task ({task} marked as complete)")
    else:
        print("This task doesn't exist. Please, try again")


while True:
    # try:
    print("Welcome to TO-DO List Manager")
    print("\n 1. Create A Task \n 2. Delete a Task \n 3. View Ongoing Tasks. \n 4. View Completed Tasks \n 5. Mark Task as Complete \n 6. Exit")
    print("What do you want to do Today? ")
    choice = int(input("Enter Choice: "))
    if choice and choice <= 6:
        # Valid Choice
        if choice == 1:
            task = input('Enter Task: ').lower()
            add_task(task)
        if choice == 2:
            task = input('Enter Task: ').lower()
            remove_task(task)
        if choice == 3:
            display_todo(task)
        if choice == 4:
            display_completed
        if choice == 5:
            task = input('Enter Task to mark as complete: ').lower()
            mark_complete(task)
        if choice == 6:
            print('Exiting Program')
            break
    else:
        print("Choice is invalid! Enter a Valid Choice \n")
    # except ValueError:
    # print('This program only accepts Integers as Options')
