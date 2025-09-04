class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        if not isinstance(account_holder, str) or not account_holder.strip():
            raise ValueError("❌ Account holder name must be a non-empty string.")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("❌ Initial balance must be a non-negative number.")

        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit must be a positive amount.")
            return
        self.balance += amount
        print(f"✅ Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal must be a positive amount.")
            return
        if amount > self.balance:
            print("❌ Insufficient funds.")
            return
        self.balance -= amount
        print(f"✅ Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"💰 Current balance: {self.balance}")
        return self.balance

    def display_info(self):
        print(f"👤 Account Holder: {self.account_holder}")
        print(f"💰 Balance: {self.balance}")
