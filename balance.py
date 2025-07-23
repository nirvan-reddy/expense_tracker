import json
from collections import defaultdict

def calculate_balance(file_path):
    try:
        with open(file_path, 'r') as f:
            transactions = json.load(f)
    except json.JSONDecodeError:
        print("No transactions found.")
        return

    if not transactions:
        print("No transactions to display.")
        return

    # Group amounts by category
    category_totals = defaultdict(float)
    for txn in transactions:
        category = txn.get('category', 'Uncategorized')
        category_totals[category] += txn.get('amount', 0)

    print("\nSpending Breakdown:\n")
    for category, amount in category_totals.items():
        print(f"On {category.title()}, you spent ₹{amount:.2f}")

    # Calculate total
    total = sum(category_totals.values())
    print(f"\n Total Spent: ₹{total:.2f}")
