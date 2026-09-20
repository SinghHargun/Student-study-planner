import json
from datetime import datetime


FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()

def display_menu():
    print("\n===== STUDENT STUDY PLANNER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def get_valid_due_date():
    while True:
        due_date = input("Enter the due date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")    


def add_task():
    course = input("Enter the course name: ").strip()
    description = input("Enter the task description: ").strip()
    due_date = get_valid_due_date()

    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

        if priority in ["High", "Medium", "Low"]:
            break

        print("Invalid priority. Please enter High, Medium, or Low.")

    task = {
        "course": course,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
        
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("You currently have no tasks.")
        return

    sorted_tasks = sorted(tasks, key=lambda task: task["due_date"])


    print("\n===== YOUR TASKS =====")

    for number, task in enumerate(sorted_tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Not Completed"

        print(
            f"{number}. {task['course']} | "
            f"{task['description']} | "
            f"Due: {task['due_date']} | "
            f"Priority: {task['priority']} | "
            f"{status}"
        )
def mark_task_complete():
    if len(tasks) == 0:
        print("You currently have no tasks.")
        return

    view_tasks()
    sorted_tasks = sorted(tasks, key=lambda task: task["due_date"])

    try:
        task_number = int(input("Enter the task number to complete: "))

        if 1 <= task_number <= len(sorted_tasks):
            sorted_tasks[task_number - 1]["completed"] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if len(tasks) == 0:
        print("You currently have no tasks.")
        return

    view_tasks()
    sorted_tasks = sorted(tasks, key=lambda task: task["due_date"])

    try:
        task_number = int(input("Enter the task number to delete: "))

        if 1 <= task_number <= len(sorted_tasks):
            task_to_delete = sorted_tasks[task_number - 1]
            tasks.remove(task_to_delete)
            save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")
            
while True:
    display_menu()
    choice = input("Choose an option: ").strip()


    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using the Study Planner!")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 5.")