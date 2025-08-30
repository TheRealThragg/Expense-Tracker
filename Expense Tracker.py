import datetime
import json
import os
# JSON file name
JSON_FILE = "expenses.json"

def load_expenses():
    """Load tasks from JSON file. Create fil if it doesn't exist"""
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w', encoding='utf-8') as f:  # Add encoding
            json.dump([], f)
        return []
    with open(JSON_FILE, 'r', encoding='utf8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(expenses_list):
    """Save tasks to JSON file."""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:  # Add encoding
        json.dump(expenses_list, f, indent=2)

# Load tasks at startup
expenditure= load_expenses()

def add_expenditure():
    expense_list = input("\ntask-cli add ")
    if not expense_list.strip():
        print("-" * 50 + "\n")
        print("Task cannot be empty. Please enter a valid task.")
        return
    expenditure.append({"task": expense_list, "completed": False})
    save_tasks(expenditure)
    print(f"task-cli '{expense_list}' added to the list -\n")
    x = datetime.datetime.now()
    print(x.strftime("%c"))

def complete_expenses():
    list_expenditure()
    user_input = input("Task to mark as completed: ")

    try:
        expense_to_complete = int(user_input)
        i = expense_to_complete - 1

        if 0 <= i < len(expenditure):
            expenditure[i]["completed"] = True
            save_tasks(expenditure)  # Save to file
            print(f"Task {expense_to_complete} marked as completed! -\n")
        else:
            print("\n" + "-" * 50)
            print(f"Invalid task number: '{expense_to_complete}' please enter a valid integer between 1 and {len(expenditure)}")
            print("-" * 50 + "\n")

    except ValueError:
        print("\n" + "*" * 50)
        print(f"ERROR: '{user_input}' is not a valid number. Please enter a valid integer.\n")
        print("*" * 50 + "\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")

def update_expense():
    expense= input("\ntask-cli update ")
    try:
        i = int(expense) - 1
        new_task = input('task-cli ')
        if 0 <= i < len(expenditure):
            expenditure[i]["task"] = new_task
            save_tasks(expenditure)
            print(f"task-cli '{expenditure}' edited -\n")
        else:
            print("\n" + "-" * 50)
            print(
                f"Invalid task number: '{expense}' is out of range please enter a valid integer between 1 and {len(expenditure)}")
            print("-" * 50 + "\n")
    except ValueError:
        print("\n" + "*" * 50)
        print(f"ERROR: '{expense}' is not a valid number. Please enter a valid task number.")
        print("*" * 50 + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_expenditure():
    if not expenditure:
        print("There are no tasks currently to complete")
        return

    print("Current Tasks: ")
    print("task-cli list:")
    for index, expense in enumerate(expenditure):
        status = "✓" if expense ["completed"] else "✗"
        print(f"{index + 1}. [{status}] {expense}")

def delete_expense():
    list_expenditure()
    user_input = input("Enter number to delete: ")
    expenditure_to_delete = None
    try:
        expenditure_to_delete = int(user_input)
    except ValueError:
        print("\n" + "*" * 50)
        print(f"ERROR: '{expenditure_to_delete}' is not a valid number. Please enter a valid integer.\n")
        print("*" * 50 + "\n")
        return
    except Exception as e:
        print(f"An error occurred: {e}\n")

    if 0 <= expenditure_to_delete - 1 < len(expenditure):
        deleted_expense = expenditure.pop(expenditure_to_delete - 1)
        save_tasks(expenditure)
        print(f"task-cli {expenditure_to_delete} ('{deleted_expense['task']}') has been removed -\n")
        x = datetime.datetime.now()
        print(x.strftime("%c"))
    else:
        print("\n" + "-" * 50)
        print(
            f"Invalid task number: '{expenditure_to_delete}' is out of range. Please enter a valid number between 1 and {len(expenditure)}.")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    while True:
        print("\n")
        print("Please select one of the following options")
        print("_" * 50 + "\n")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        print("5. Update")
        print("6. Complete a task")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_expenditure()
        elif choice == "2":
            delete_expense()
        elif choice == "3":
            list_expenditure()
        elif choice == "4":
            break
        elif choice == "5":
            update_expense()
        elif choice == "6":
            complete_expenses()
        else:
            print(f"Please enter a valid option between 1-6, not '{choice}'")