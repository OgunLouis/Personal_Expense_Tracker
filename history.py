
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

def history(user_name):
        user_choice = int(input("Enter 1 for expense History\nEnter 2 for income History:   "))
        if user_choice == 1:
            #Retrieve and print all expenses
            print("\nCurrent Expense Log history:")
            cursor.execute(f'SELECT * FROM {user_name}_expenses')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        elif user_choice == 2:
            #Retrieve and print all income logged
            print("\nCurrent Income Log history:")
            cursor.execute(f'SELECT * FROM {user_name}_income')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            print("Input Error")
