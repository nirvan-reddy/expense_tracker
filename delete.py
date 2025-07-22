import json

def delete_transaction(index, file_path):
    try:
        with open(file_path, 'r') as f:
            transactions = json.load(f)
    except json.JSONDecodeError:
        print("No transactions found.")
        return

    if 0 <= index < len(transactions):
        removed = transactions.pop(index)
        with open(file_path, 'w') as f:
            json.dump(transactions, f, indent=4)
        print(f"Deleted: {removed['description']} - ${removed['amount']}")
    else:
        print("Invalid index.")
