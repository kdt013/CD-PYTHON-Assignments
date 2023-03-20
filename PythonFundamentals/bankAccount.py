class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {self.balance}")
        return self
        # your code here

    def withdraw(self, amount):
        if(self.balance < 0):
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            print(f"Withdrew: {self.balance}")
        return self
        # your code here

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        # your code here

    def yield_interest(self):
        self.balance *= self.int_rate
        print(f"Interest Rate: {self.balance}")
        return self
        # your code here

user1=BankAccount(0.01, 1200)
user1.display_account_info().deposit(275).withdraw(420).yield_interest()

user2=BankAccount(0.01, 40000)
user2.display_account_info().deposit(3500).withdraw(20000).yield_interest()
