import json
import os

FILE_NAME = "expenses.json"

# Load existing expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Add new expense
def add_expense(expenses):
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)
    print("✅ Expense added!")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
    else:
        print("\nYour Expenses:")
        total = 0
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['title']} - ${e['amount']}")
            total += e['amount']
        print(f"---\nTotal: ${total}")

# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)
    if expenses:
        try:
            num = int(input("Enter expense number to delete: "))
            if 1 <= num <= len(expenses):
                removed = expenses.pop(num-1)
                save_expenses(expenses)
                print(f"🗑️ Deleted {removed['title']} - ${removed['amount']}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

# Edit expense
def edit_expense(expenses):
    view_expenses(expenses)
    if expenses:
        try:
            num = int(input("Enter expense number to edit: "))
            if 1 <= num <= len(expenses):
                exp = expenses[num-1]
                print(f"Editing: {exp['title']} - ${exp['amount']}")
                new_title = input("Enter new title (or press Enter to keep same): ")
                new_amount = input("Enter new amount (or press Enter to keep same): ")

                if new_title.strip():
                    exp['title'] = new_title
                if new_amount.strip():
                    exp['amount'] = float(new_amount)

                save_expenses(expenses)
                print("✏️ Expense updated!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            edit_expense(expenses)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
