"""
Usage:

Run the script to interact with the banking management system through the console.

"""


"""
Banking Management System

This script implements a simple command-line banking management system that allows users
to perform the following operations with a MySQL database backend:
1. Create a new account
2. View account details
3. Deposit money
4. Withdraw money
5. Delete an account
6. Exit the System

"""

"""
Modules:
    1. Import get_connection function from DB_connection.py file to connect the MySQL database.
    2. Import pandas : To display account details in a tabular format.
    3. Import time : To add delay.

"""
from DB_connection import get_connection
import pandas as pd
import time

conn = get_connection()
cursor = conn.cursor()

# Functions of users use
# creating account
"""
create_account(name: str, balance: float):
    Create a new account with the given name and initial balance.
    Commit the changes and give to user newly generated account ID.
    Parameters:
        name (str): The name of account holder.
        balance (float): The initial balance to be added to the account. 

"""
def create_account(name, balance):
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name,balance))
    conn.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    account_id = cursor.fetchone()[0]
    print(f"Account created successfully. Your account ID is: {account_id} do not share.")


# view the account
"""
view_account(account_id (int), name (str)):
    Retrives and display the account details for a specific account ID and name user.
    IF account_id and name not match in MySQL database then display "No account found with that customer name" message.
    If found with account_id and name in MySQL database then pandas used to prints details in table format.
    Parameters:
        account_id (int): The account ID to search for.
        name (str): The name of the account holder.

"""
def view_account(account_id,name):
    cursor.execute("SELECT * FROM accounts WHERE account_id = %s AND name = %s",(account_id,name))
    rows = cursor.fetchall()
    
    if rows:
        df = pd.DataFrame(rows, columns=['Account ID', 'Name', 'Balance'])
        print("\n Account Details: \n")
        print(df.to_string(index=False))

        time.sleep(2)
    else:
        print("No account found with that customer name")

# deposit amount
"""
deposit(account_id: int, name: str, amount: float)
    Deposits a specified amount into the user's account after validating the credentials.
    1 check:
        Given user is stored in MySQL database or not, if there deposit amount neither show "Account not found" message. 
    Parameters:
        account_id (int): The ID of the account.
        name (str): The name of the account holder.
        amount (float): The amount to be deposited.

"""
def deposit(account_id, name, amount):
    cursor.execute("SELECT * FROM accounts WHERE account_id = %s AND name = %s", (account_id, name))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
        conn.commit()
        print("Deposit successful.\n")
    else:
        print(f"Account not found.")


# Withrow amount
"""
withdraw(account_id: int, name: str, amount: float)
    Withdraws a specified amount into the user's account after validating the credentials.
    1 check:
        Withdraws a specified amount from the account after ensuring sufficient balance.
    2 check:
        If user credentialse not match then display "Account not found or name mismatch" message.
    Parameters:
        account_id (int): The ID of the account.
        name (str): The name of the account holder.
        amount (float): The amount to withdraw.

"""
def withdraw(account_id,name,amount):
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s AND name = %s", (account_id,name))
    result = cursor.fetchone()

    if result:
        current_balance = result[0]
        if current_balance >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, account_id))
            conn.commit()
            print("Withdraw successful.\n")
        else:
            print("Insufficient balance.\n")
    else:
        print("Account not found or name mismatch.\n")


# deleting account
"""
delete_account(account_id: int, name: str)
    Deletes the account matching the provided account ID and name.
    Parameters:
        account_id (int): The ID of the account.
        name (str): The name of the account holder.

"""
def delete_account(account_id,name):
    cursor.execute("SELECT * FROM accounts WHERE account_id = %s AND name = %s", (account_id,name))
    result = cursor.fetchone()

    if result:
        cursor.execute("DELETE FROM accounts WHERE account_id = %s", (account_id,))
        conn.commit()
        print("Account deleted.\n")
    else:
        print("No account found")

# menu
"""
menu()
    Displays the main menu with options for each of the supported operations.
    Handles user input and dispatches function calls accordingly.
    Includes error handling for invalid inputs and unexpected exceptions.

"""
def menu():
    while True:
        print("\n_______ Banking Management ________")
        print("1. Create Account")
        print("2. View Accounts details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Exit")
        print("______________________________")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter customer name: ")
                balance = float(input("Enter initial balance: "))
                create_account(name, balance)

            elif choice == '2':
                account_id = int(input("Enter Account ID: "))
                name = input("Enter Account Holder name: ")
                view_account(account_id, name)

            elif choice == '3':
                account_id = int(input("Enter Account ID: "))
                name = input("Enter Account Holder name: ")
                amount = float(input("Enter deposit amount: "))
                deposit(account_id, name, amount)

            elif choice == '4':
                account_id = int(input("Enter Account ID: "))
                name = input("Enter Account Holder name: ")
                amount = float(input("Enter withdrawal amount: "))
                withdraw(account_id, name, amount)

            elif choice == '5':
                account_id = int(input("Enter Account ID to delete account: "))
                name = input("Enter Account Holder name: ")
                delete_account(account_id, name)

            elif choice == '6':
                print("Exiting. Thank you!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input type. Please enter numbers for account ID and amount.")
        except Exception as e:
            print("An error occurred:", e)

menu()

cursor.close()
conn.close()