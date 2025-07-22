import json
import os

def add_transaction(amount, category, description, file_path):
    transaction = {
        "amount": amount,
        "category": category,
        "description": description
    }

    transactions = []

    # Load existing transactions if the file exists
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    transactions = data
                else:
                    print("Warning: data.json is not a list. Resetting to new list.")
        except json.JSONDecodeError:
            print("Warning: JSON decode error. Starting with empty list.")

    # Append new transaction
    transactions.append(transaction)

    # Save updated list back to the file
    with open(file_path, 'w') as f:
        json.dump(transactions, f, indent=4)

    print(f"Added: {description} - ₹{amount}")
