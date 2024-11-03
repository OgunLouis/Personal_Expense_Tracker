from datetime import datetime
import sqlite3
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Get the current date and time
now = datetime.now()
# Format to day/month/year
date_str = now.strftime("%d/%m/%y")

# Connect to the database (creates the file if it doesn’t exist)
conn = sqlite3.connect('PersonalExpense.db')
cursor = conn.cursor()

# Define function to add expense
def add_expense(user_name):
    item = str(input("Please input item purchased: \n"))
    description = str(input("What is the intended use?: \n"))
    amount = int(input("Amount of purchase: \n"))
    a_date = date_str
    expense_table = f"{user_name}_expenses"
    income_table = f"{user_name}_income"
    # Insert expense data into the database
    cursor.execute(f'''
    INSERT INTO {expense_table} (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    ''', (a_date, item, amount, description))
    
    # Commit the transaction to save changes
    conn.commit()
    
    # Print summary for the user
    data = (
        f"-----------------------\nItem: {item}\n"
        f"Description: {description}\n"
        f"Amount: ₦{amount}\n"
        f"Date: {a_date}\n"
        "------------------------\n"
    )
    print(data)
    conn.close()
