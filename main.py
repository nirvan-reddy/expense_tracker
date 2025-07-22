from utils.add import add_transaction
from utils.view import view_transactions
from utils.delete import delete_transaction
from utils.balance import calculate_spent

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Delete Transaction")
    print("4. Total Spent")
    print("5. Exit")

def main():
    show_menu()
    file_path = "data.json"

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (e.g., Food, Travel): ")
                description = input("Enter description: ")
                add_transaction(amount, category, description, file_path)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            view_transactions(file_path)

        elif choice == "3":
            try:
                index = int(input("Enter transaction number to delete: ")) - 1
                delete_transaction(index, file_path)
            except ValueError:
                print("Invalid index. Please enter a number.")

        elif choice == "4":
            calculate_spent(file_path)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
