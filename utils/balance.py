import json

def calculate_spent(file_path):
    try:
        with open(file_path, 'r') as f:
            transactions = json.load(f)
    except json.JSONDecodeError:
        print("No transactions found.")
        return

    total = sum(txn['amount'] for txn in transactions)
    print(f"Total Spent: ${total:.2f}")
