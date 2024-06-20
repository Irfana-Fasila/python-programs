class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Deposit amount should be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account Balance: Rs. {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.5):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Interest added: Rs. {interest_amount}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=2000.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount beyond overdraft limit.")
    
    def display_balance(self):
        print(f"Account Balance: Rs. {self.balance} | Overdraft Limit: Rs. {self.overdraft_limit}")

# Example usage:
def main():
    # Create savings account
    savings_acc = SavingsAccount("SA123456", "Alice", balance=5000.0, interest_rate=1.0)
    savings_acc.display_balance()
    savings_acc.deposit(2000.0)
    savings_acc.add_interest()
    savings_acc.display_balance()
    savings_acc.withdraw(3000.0)
    savings_acc.display_balance()

    print("\n")

    # Create current account
    current_acc = CurrentAccount("CA987654", "Bob", balance=10000.0, overdraft_limit=5000.0)
    current_acc.display_balance()
    current_acc.deposit(3000.0)
    current_acc.display_balance()
    current_acc.withdraw(15000.0)
    current_acc.display_balance()

if __name__ == "__main__":
    main()
