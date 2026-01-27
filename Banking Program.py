import os
from datetime import datetime

BALANCE_FILE = "balance.txt"
LOG_FILE = "transaction_log.txt"
DEFAULT_BALANCE = "0"


def initialize_system():
    """Create files if they don't exist"""
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as f:
            f.write(DEFAULT_BALANCE)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("-----Transaction Log Started-----\n")

def get_balance():
    """Read balance from file"""
    with open(BALANCE_FILE, "r") as f:
        return float(f.read().strip())

def save_balance(balance):
    """Save balance to file"""
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def log_transaction(transaction_type, amount):
    """Log transaction to file"""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {transaction_type}: ${amount:.2f}\n")


def deposit(balance):
    try:
        amount = float(input("ENTER AMOUNT TO DEPOSIT: "))
        if amount <= 0:
            print("Amount must be positive!")
            return balance
        
        balance += amount
        save_balance(balance)
        log_transaction("DEPOSIT", amount)
        print(f"Successfully deposited ${amount:.2f}")
        return balance
    except ValueError:
        print("Invalid input! Enter a number.")
        return balance

def withdraw(balance):
    try:
        amount = float(input("ENTER AMOUNT TO WITHDRAW: "))
        if amount <= 0:
            print("Amount must be positive!")
            return balance
        
        if amount > balance:
            print(f"Insufficient Funds! Balance: ${balance:.2f}")
            return balance
            
        balance -= amount  
        save_balance(balance)
        log_transaction("WITHDRAW", amount)
        print(f"Successfully withdrew ${amount:.2f}")
        return balance
    except ValueError:
        print("Invalid input! Enter a number.")
        return balance


initialize_system()
print("\n--------- WELCOME TO IRON BANK -----------")

while True:
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")
    print("-" * 30)
    
    choice = input("Select Option: ")

    if choice == "1":
        email = input("Enter Email: ").strip()
        if email == "sahasomanjan@gmail.com":
            password = input("Enter Password: ")
            if password == "Somanjan2006@$":
                print("\nACCESS GRANTED!")
                current_balance = get_balance()
                banking_active = True
                
                while banking_active:
                    print(f"\n--- ACCOUNT MENU (Balance: ${current_balance:.2f}) ---")
                    print("1. Show Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    
                    op = input("Select: ")
                    
                    if op == "1":
                        print(f"\nCurrent Balance: ${current_balance:.2f}")
                    elif op == "2":
                        current_balance = deposit(current_balance)
                    elif op == "3":
                        current_balance = withdraw(current_balance)
                    elif op == "4":
                        print("Logging out...")
                        banking_active = False 
                    else:
                        print("Invalid Option.")
            else:
                print("Invalid Password")
        else:
            print("User not found")

    elif choice == "2":
        # --- REGISTER FLOW ---
        print("\n--- REGISTRATION ---")
        new_email = input("Enter Email: ")
        if "@" not in new_email:
            print("Invalid Email.")
            continue
            
        while True:
            new_pass = input("Set Password (Min 8 chars): ")
            if len(new_pass) >= 8:
                print(" Account Created! (Please Login now)")
                break
            print(f"Too short ({len(new_pass)}/8).")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid Option.")


