# bank_account.py
# TASK 10: Object-Oriented Programming (OOP)

class BankAccount:
    """
    Base class representing a bank account
    Demonstrates encapsulation using protected attributes
    """

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance


# Inheritance example
class SavingsAccount(BankAccount):
    """
    Child class inheriting from BankAccount
    Demonstrates inheritance and method overriding
    """

    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def deposit(self, amount):
        super().deposit(amount)
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest added: {interest}")


# Creating multiple objects
account1 = BankAccount("Ashok", 5000)
account2 = SavingsAccount("Ravi", 3000)

print("\n--- BankAccount Operations ---")
account1.deposit(2000)
account1.withdraw(1500)
print("Balance:", account1.get_balance())

print("\n--- SavingsAccount Operations ---")
account2.deposit(1000)
account2.withdraw(500)
print("Balance:", account2.get_balance())
