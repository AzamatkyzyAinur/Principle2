class Account:
   def __init__(self, owner, balance=0):
       self.owner = owner
       self.balance = balance
       print(f"Account created for {self.owner} with initial balance of ${self.balance:.2f}.")
   def __str__(self):
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
               print("Funds unavailable! Withdrawal denied.")
               print(f"Available balance: ${self.balance:.2f}")
       else:
           print("Withdrawal amount must be positive.")
print("\n")
owner_name = input("Enter a name: ")
initial_balance = float (input("Enter the initiAL BALANCE: "))
acct = Account(owner_name, initial_balance)
print("-" * 30)
while True:
   action = input("Type 'deposit' to add money, 'withdraw' to take money, or 'exit' to quit: ").lower()
   if action == "deposit":
       amount = float(input("Enter deposit amount: "))
       acct.deposit(amount)
   elif action == "withdraw":
       amount = float(input("Enter withdrawal amount: "))
       acct.withdraw(amount)
   elif action == "exit":
       print("Exiting...")
       break
   else:
       print("Invalid option. Please choose 'deposit', 'withdraw', or 'exit'.")
   print(f"Current balance: ${acct.balance:.2f}")
   print("-" * 30)
print("Final account status:")
print(acct)
 