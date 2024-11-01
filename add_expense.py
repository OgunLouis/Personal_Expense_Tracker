from datetime import datetime
import sqlite3
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Get the current date and time
now = datetime.now()
# Format to day/month/year
date_str = now.strftime("%d/%m/%y")

# Connect to the database (creates the file if it doesn’t exist)
conn = sqlite3.connect('PET.db')
cursor = conn.cursor()

# Create the expenses table if it doesn’t already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    amount INT,
    description TEXT
)
''')

# Ask for user income
#income = int(input("Please enter your income: \n"))

# Define function to add expense
def add_expense():
    item = str(input("Please input item purchased: \n"))
    description = str(input("What is the intended use?: \n"))
    amount = int(input("Amount of purchase: \n"))
    a_date = date_str
    
    # Insert expense data into the database
    cursor.execute('''
    INSERT INTO expenses (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    ''', (a_date, item, amount, description))
    
    # Commit the transaction to save changes
    conn.commit()
    
    # Print summary for the user
    data = (
        f"Item: {item}\n"
        f"Description: {description}\n"
        f"Amount: ₦{amount}\n"
        f"Date: {a_date}\n"
        "------------------------\n"
    )
    print(data)
    conn.close()

# Prompt user for details and add expense
#add_expense()

# Close the database connection when done
