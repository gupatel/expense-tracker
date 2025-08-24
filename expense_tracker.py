expenses = []

def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    expenses.append({"title": title, "amount": amount})
    print("✅ Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        print("\nYour Expenses:")
        total = 0
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['title']} - ${e['amount']}")
            total += e['amount']
        print(f"---\nTotal: ${total}")

def delete_expense():
    view_expenses()
    if expenses:
        try:
            num = int(input("Enter expense number to delete: "))
            if 1 <= num <= len(expenses):
                removed = expenses.pop(num-1)
                print(f"🗑️ Deleted {removed['title']} - ${removed['amount']}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
