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
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY,
    Income INT,
    Description TEXT,
    Date DATE
)
''')
now = datetime.now()
date_str = now.strftime("%d/%m/%y")

def add_income():
    income_amount = int(input("How much did you earn: \n"))
    description = str(input("Income source?: \n"))
    a_date = date_str
    
    # Insert expense data into the database
    cursor.execute('''
    INSERT INTO income (Date, Income, Description)
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

#add_income(User_name=input('Enter Username:    \n'))
# Close the database connection when done
#conn.close()