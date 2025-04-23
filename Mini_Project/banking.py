from DB_connection import get_connection
import pandas as pd

conn = get_connection()
cursor = conn.cursor()

# Functions
# creating account
def create_account(name, balance):
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name,balance))
    conn.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    account_id = cursor.fetchone()[0]
    print(f"Account created successfully. Your account ID is: {account_id} do not share.")

# check user account
def view_account(account_id,name):
    cursor.execute("SELECT * FROM accounts WHERE account_id = %s AND name = %s",(account_id,name))
    rows = cursor.fetchall()
    
    if rows:
        df = pd.DataFrame(rows, columns=['Account ID', 'Name', 'Balance'])
        print("\n Account Details: \n")
        print(df.to_string(index=False))
    else:
        print("No account found with that customer name")

# deposit amount
def deposit(account_id, name, amount):
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (account_id, name))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
        conn.commit()
        print("Deposit successful.\n")
    else:
        print("Account not found.")

# Withrow amount
def withdraw(account_id,name,amount):
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,name))
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
def delete_account(account_id,name):
    cursor.execute("SELECT * FROM accounts WHERE account_id = %s AND name = %s", (account_id,name))
    result = cursor.fetchone()

    if result:
        cursor.execute("DELETE FROM accounts WHERE account_id = %s AND name = %s", (account_id,name))
        conn.commit()
        print("Account deleted.\n")
    else:
        print("No account found")

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

        if choice == '1':
            name = input("Enter customer name: ")
            balance = float(input("Enter initial balance: "))
            create_account(name,balance)

        elif choice == '2':
            account_id = int(input("Enter Account ID: "))
            name = input("Enter Account Holder name: ")
            view_account(account_id,name)

        elif choice == '3':
            account_id = int(input("Enter Account ID: "))
            name = input("Enter Account Holder name: ")
            amount = float(input("Enter deposit amount: "))
            deposit(account_id, name, amount)

        elif choice == '4':
            account_id = int(input("Enter Account ID: "))
            name = input("Enter Account Holder name: ")
            amount = float(input("Enter withdrawl amount: "))
            withdraw(account_id, name, amount)

        elif choice == '5':
            account_id = int(input("Enter Account ID: "))
            name = input("Enter Account Holder name: ")
            delete_account(account_id,name)

        elif choice == '6':
            print("Exiting. Thank you!")
            break

        else:
            print("Invalid choice. Try agign.")


menu()

cursor.close()
conn.close()