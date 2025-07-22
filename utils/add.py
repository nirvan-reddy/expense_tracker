import json
import os

def add_transaction(amount, category, description, file_path):
    transaction = {
        "amount": amount,
        "category": category,
        "description": description
    }

    # Load existing transactions or create a new list
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                transactions = json.load(f)
        except json.JSONDecodeError:
            transactions = []
    else:
        transactions = []

    # Append new transaction
    transactions.append(transaction)

    # Save back to file
    with open(file_path, 'w') as f:
        json.dump(transactions, f, indent=4)

    print(f" Added: {description} - ₹{amount}")