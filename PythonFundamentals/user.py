import from bankAccount import BankAccount
class user:
    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)



    def display_into(self):
        print(user.first_name)
        print(user.last_name)
        print(user.email)
        print(user.age)
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self,amount):
        if(self.gold_card_points == 0):
            print(f"{self.first_name} has no points")
        else:
            self.amount = amount
            self.gold_card_points -= 10
    
    def make_deposit(self, amount):
    	# your code here




kav = user("kavita","thomas","kavitathomas13@gmail.com", 22)   

print(kav.first_name)
print(kav.last_name)
print(kav.email)
print(kav.age)
