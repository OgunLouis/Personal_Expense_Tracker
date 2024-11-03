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

now = datetime.now()
date_str = now.strftime("%d/%m/%y")

def add_income(user_name):
    income_amount = int(input("How much did you earn: \n"))
    description = str(input("Income source?: \n"))
    a_date = date_str
    income_table = f"{user_name}_income"
    
    # Insert expense data into the database
    cursor.execute(f'''
    INSERT INTO {income_table} (Date, Income, Description)
    VALUES (?, ?, ?)
    ''', (date_str, income_amount, description))
    
    # Commit the transaction to save changes
    conn.commit()
    data = (
        
    f"Income: ₦{income_amount}\n"
    f"Description: {description}\n"
    f"Date: {date_str}\n"
    "------------------------\n")
    print("------------------------\n", data)
    conn.close()
# Close the database connection when done
#conn.close()