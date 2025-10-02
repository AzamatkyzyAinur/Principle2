class Account:
   def __init__(self, owner, balance=0):
       self.owner = owner
       self.balance = balance
       print(f"Account created for {self.owner} with initial balance of ${self.balance:.2f}.")
   def __str__(self):
       # A helpful string representation for the object
       return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance:.2f}"
   def deposit(self, amount):
       if amount > 0:
           self.balance += amount
           print(f"Deposit accepted. Current balance: ${self.balance:.2f}")
       else:
           print("Deposit amount must be positive.")
   def withdraw(self, amount):
       if amount > 0:
           if amount <= self.balance:
               self.balance -= amount
               print(f"Withdrawal accepted. Current balance: ${self.balance:.2f}")
           else:
               # Test to make sure the account can't be overdrawn
               print("Funds unavailable! Withdrawal denied.")
               print(f"Available balance: ${self.balance:.2f}")
       else:
           print("Withdrawal amount must be positive.")
print("\n")
# Instantiate the class
acct = Account('Jane Doe', 100)
print(acct)
print("-" * 20)
# Make several deposits and withdrawals
acct.deposit(50)
acct.deposit(200.50)
print("-" * 20)
acct.withdraw(75)
print("-" * 20)
# Test to make sure the account can't be overdrawn (Current balance: 275.50)
acct.withdraw(300)
print("-" * 20)
acct.withdraw(15.50)
print(acct)