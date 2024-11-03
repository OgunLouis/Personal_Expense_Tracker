from datetime import datetime
import sqlite3
from add_expense import add_expense
from balance_checker import balance
from add_income import add_income
from history import history
import loading_screen
from clear_screen import clear_screen
from Creating_User import create_user_table
# Get the current date and time
now = datetime.now()
# Format to day/month/year
date_str = now.strftime("%d/%m/%y")
# Prompt user to enter a username
#User information
print("---------MAIN MENU--------")
user_name = input("Enter your username: \n")
create_user_table(user_name)
while True:
    # Prompt user for menu choice
    print("---------MAIN MENU--------")
    menu = int(input('Enter 1 to add an expense\nEnter 2 to record an income\nEnter 3 to view history\nEnter 4 to view your Balance\nPress 0 to exit\n'))
    if menu == 1:
        loading_screen.show_loading_screen()
        add_expense(user_name)  # Call your add_expense function
        
    elif menu == 2:
        loading_screen.show_loading_screen()
        add_income(user_name)  # Call your add_income function
    elif menu == 3:
        loading_screen.show_loading_screen()
        history(user_name)  # Call your history function
    elif menu == 4:
        loading_screen.show_loading_screen()
        balance(user_name)  # Call your balance function
    elif menu == 0:
        loading_screen.exit_screen()  # Optional: Show an exit screen
        print("Exiting program. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid option. Please enter a number from 0 to 4.")


    



