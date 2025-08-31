import datetime
from datetime import datetime
import json
import os

# JSON file name
JSON_FILE = "expenses.json"

def load_expenses():
    """Load expenditure from JSON file. Create fil if it doesn't exist"""
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w', encoding='utf-8') as f:  # Add encoding
            json.dump([], f)
    with open(JSON_FILE, 'r', encoding='utf8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
def save_expenditure(expenses_list,):
    """Save expenditure to JSON file."""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:  # Add encoding
        json.dump(expenses_list, f, indent=2)
# Load expenditure at startup
expenditure = load_expenses()

def add_expenditure():
    while True:
        try:
            expense_list = int(input("\n£"))
            break
        except ValueError:
            print(f"Invalid amount: '{input()}' is out of range please enter a valid integer")
        return
    expenditure.append({"£":expense_list,})
    save_expenditure(expenditure)
    print(f"£{expense_list} added to the list -\n")
def edit_expense():
    expense= input("\n update ")
    try:
        i = int(expense) - 1
        new_expense = input("£")
        if 0 <= i < len(expenditure):
            expenditure[i]["expense"] = new_expense
            save_expenditure(expenditure)
            print(f"expense '{expenditure}' edited -\n")
        else:
            print("\n" + "-" * 50)
            print(f"Invalid amount: '{expense}' is out of range please enter a valid integer between 1 and {len(expenditure)}")
            print("-" * 50 + "\n")
    except ValueError:
        print("\n" + "*" * 50)
        print(f"ERROR: '{expense}' is not a valid amount. Please enter a valid number.")
        print("*" * 50 + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_expenditure():
    if not expenditure:
        print("There are no expenses currently")
        return
    print("Current expenses: ")
    for index, expense in enumerate(expenditure):
        print(f"{index+1}.{expense}")
        

def delete_expense():
    list_expenditure()
    user_input = input("Enter the number to delete: ")
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
        save_expenditure(expenditure)
        print(f"expense {expenditure_to_delete} ('{deleted_expense}') has been removed -\n")
        x = datetime.datetime.now()
        print(x.strftime("%c"))
    else:
        print("\n" + "-" * 50)
        print(f"Invalid number: '{expenditure_to_delete}' is out of range. Please enter a valid number between 1 and {len(expenditure)}.")
        print("-" * 50 + "\n")
        return

if __name__ == "__main__":
    while True:
        print("\n")
        print("Please select one of the following options")
        print("_" * 50 + "\n")
        m = """
        1. Add a new expense
        2. Delete an expense
        3. List expenditure
        4. Quit
        5. Update
        """
        print(m)
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
            edit_expense()
        else:
            print(f"Please enter a valid option between 1-6, not '{choice}'")
