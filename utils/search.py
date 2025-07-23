import json
import os

def search_transaction(file_path, keyword):
    try:
        with open(file_path, 'r') as f:
            transactions = json.load(f)
    except json.JSONDecodeError:
        print("No transactions found.")
        return
 
    if not transactions:
        print("No transactions to display.")
        return
 
    keyword = keyword.lower()
    matches = []
 
    for txn in transactions:
        description = txn.get('description', '').lower()
        category = txn.get('category', '').lower()
        date = txn.get('date', '').lower()
 
        if keyword in description or keyword in category or keyword in date:
            matches.append(txn)
 
    if not matches:
        print(f"No transactions found for '{keyword}'.")
    else:
        print(f"\nTransactions matching '{keyword}':\n")
        for txn in matches:
            print(f"Date: {txn.get('date', 'N/A')}, "
                  f"Amount: ₹{txn.get('amount', 0):.2f}, "
                  f"Category: {txn.get('category', 'Uncategorized')}, "
                  f"Description: {txn.get('description', '')}")