from utils.add import add_transaction
from utils.view import view_transactions
from utils.delete import delete_transaction
from utils.balance import calculate_balance

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Transactions")
    print("4. Delete Transaction")
    print("5. Show Balance")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_transaction("expense")
        elif choice == "2":
            add_transaction("income")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            delete_transaction()
        elif choice == "5":
            calculate_balance()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
