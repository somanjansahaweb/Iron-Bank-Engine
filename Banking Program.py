import os
import sys
from datetime import datetime

# --- CONFIGURATION ---
USERS_FILE = "Iron.txt"
TRANSACTION_LOG_FILE = "Transact.txt"
DEFAULT_BALANCE = 1200. 


class IronBankEngine:
    """The Persistence Layer: Handles all file reading and writing."""

    @staticmethod
    def initialize_systems():
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'w') as f:  
                pass
        if not os.path.exists(TRANSACTION_LOG_FILE):
            with open(TRANSACTION_LOG_FILE, 'w') as f:
                f.write("------------ TRANSACTION LOG STARTED ------------\n") 
                 


    @staticmethod
    def save_user_state(email, balance, new_password=None):
        """Finds user by email and updates their balance or password."""
        updated_lines = []
        with open(USERS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    stored_email, stored_pass, stored_balance = parts
                    if stored_email == email:
                        # If a new_password is provided, use it; otherwise keep the old one
                        pass_to_save = new_password if new_password else stored_pass
                        updated_lines.append(f"{stored_email},{pass_to_save},{balance}\n")
                    else:
                        updated_lines.append(line) 
                         
                                 
        with open(USERS_FILE, "w") as f:
            f.writelines(updated_lines) 
             


    @staticmethod
    def log_transaction(email, action, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {email} | {action}: ${amount:,.2f}\n"
        with open(TRANSACTION_LOG_FILE, "a") as f:
            f.write(entry)

class BankAccount:
    """The Business Logic: Handles user actions in memory."""
    def __init__(self, email, balance):
        self.email = email
        self.balance = float(balance)

    def deposit(self):
        amount = self._get_amount("DEPOSIT")
        if amount:
            self.balance += amount
            IronBankEngine.save_user_state(self.email, self.balance)
            IronBankEngine.log_transaction(self.email, "DEPOSIT", amount)
            print(f"\n[SUCCESS] NEW BALANCE: ${self.balance:,.2f}")

    def withdraw(self):
        
        print(f"\n YOU HAVE: ${self.balance}")
        
        amount = self._get_amount("WITHDRAWAL")
        
        if amount:
            print(f" COMPARING: Is {amount} > {self.balance}?")
            
            if amount > self.balance:
                print(f"[ERROR] YES. {amount} is greater than {self.balance}.")
                print(f"[ERROR] INSUFFICIENT FUNDS! YOU HAVE: ${self.balance:,.2f}")
                return
            self.balance -= amount
            IronBankEngine.save_user_state(self.email, self.balance)
            IronBankEngine.log_transaction(self.email, "WITHDRAWAL", amount)
            print(f"\n[SUCCESS] WITHDRAWAL COMPLETE.")
            print(f"[SUCCESS] NEW BALANCE: ${self.balance:,.2f}")

    def change_password(self):
        new_password = input("ENTER NEW PASSWORD (MIN 8): ")
        if len(new_password) >= 8:
            # We call the engine to update the password in the file
            IronBankEngine.save_user_state(self.email, self.balance, new_password=new_password)
            print("\n[SUCCESS] PASSWORD UPDATED.")
        else:
            print("\n[ERROR] TOO SHORT.")

    def _get_amount(self, action):
        try:
            val = float(input(f"ENTER {action} AMOUNT: $"))
            return val if val > 0 else None
        except ValueError:
            print("[ERROR] INVALID INPUT.")
            return None

# --- APP FLOW ---
def authenticate():
    email = input("EMAIL: ")
    pwd = input("PASSWORD: ")
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 3:
                    u, p, b = data
                    if u == email and p == pwd:
                        return BankAccount(u, b)
    return None

def register():
    email = input("NEW EMAIL: ")
    password = input("NEW PASSWORD: ")
    with open(USERS_FILE, "a") as f:
        f.write(f"{email},{password},{DEFAULT_BALANCE}\n")
    print("\n[SUCCESS] REGISTRATION COMPLETE.")

def main():
    IronBankEngine.initialize_systems()
    while True:
        print("\n" + "="*30 + "\n  THE IRON BANK\n" + "="*30)
        print("1. LOGIN\n2. REGISTER\n3. EXIT")
        choice = input("SELECT > ")
        if choice == "3": break
        if choice == "2": register()
        elif choice == "1":
            user_account = authenticate()
            if user_account:
                banking_menu(user_account)
            else:
                print("\n[DENIED] INVALID LOGIN.")

def banking_menu(account):
    while True:
        print(f"\n--- WELCOME {account.email} ---")
        print("1. DEPOSIT\n2. WITHDRAW\n3. BALANCE\n4. CHANGE PASSWORD\n5. LOGOUT")
        opt = input("ACTION > ")
        if opt == "1": account.deposit()
        elif opt == "2": account.withdraw()
        elif opt == "3": print(f"\nCURRENT BALANCE: ${account.balance:,.2f}")
        elif opt == "4": account.change_password()
        elif opt == "5": break

if __name__ == "__main__":
    main()
