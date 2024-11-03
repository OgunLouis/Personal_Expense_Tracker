import sqlite3
import sys
sys.stdout.reconfigure(encoding='utf-8')


def balance(user_name):
    # Connect to the database
    conn = sqlite3.connect('PersonalExpense.db')
    cursor = conn.cursor()
    # Sum the Income column from the income table
    cursor.execute(f"SELECT SUM(Income) FROM {user_name}_income")
    total_income = cursor.fetchone()[0] or 0  # Default to 0 if no income data

    # Sum the Amount column from the expenses table
    cursor.execute(f"SELECT SUM(amount) FROM {user_name}_expenses")
    total_expenses = cursor.fetchone()[0] or 0  # Default to 0 if no expense data

    # Calculate the balance or net amount
    net_balance = total_income - total_expenses

    # Print the results
    print('----------------------------------')
    print(f"Total Income: ₦{total_income}")
    print(f"Total Expenses: ₦{total_expenses}")
    print(f"Net Balance: ₦{net_balance}")
    print('----------------------------------')
    print('----------------------------------')
    # Close the database connection
    conn.close()




