import json
import os

def view_transactions(file_path):
    if not os.path.exists(file_path):
        print(" No transactions found.")
        return

    try:
        with open(file_path, 'r') as f:
            transactions = json.load(f)
    except json.JSONDecodeError:
        print(" No transactions found.")
        return

    if not transactions:
        print(" No transactions to display.")
        return

    print("\n All Transactions:")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. ₹{t['amount']} - {t['category']} ({t['description']})")