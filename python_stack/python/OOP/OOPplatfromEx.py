# class User:
#     def __init__(self, username, email_address):
#         self.name = username
#         self.email = email_address
#         self.account_balance = 0
#     def make_deposit(self, amount):
#         self.account_balance += amount

# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# chris = User("Christopher Holley", "chris@mail.com")

# print(chris.name)
# chris.make_deposit(99)
# chris.make_deposit(99)
# chris.make_deposit(2)
# print(chris.account_balance)


# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


#  Create a file with the User class, including the __init__ and make_deposit methods
#  Add a make_withdrawal method to the User class
#  Add a display_user_balance method to the User class




class User:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer(self, recipient, amount):
        recipient.account_balance += amount
        self.account_balance-= amount

    
#  Create 3 instances of the User class
chris = User("Christopher")
tony = User("Antoinette")
hiro = User("Hiro")
print(chris.name)
print(chris.account_balance)
print(tony.name)
print(tony.account_balance)
print(hiro.name)
print(hiro.account_balance)
#  Have the first user make 3 deposits and 1 withdrawal and then display their balance
chris.make_deposit(101)
chris.make_deposit(109)
chris.make_deposit(102)
chris.make_withdrawal(12)
print(chris.name)
print(chris.account_balance)
#  Have the second user make 2 deposits and 2 withdrawals and then display their balance
tony.make_deposit(999)
tony.make_deposit(676)
tony.make_withdrawal(899)
tony.make_withdrawal(149)
print(tony.name)
print(tony.account_balance)
#  Have the third user make 1 deposits and 3 withdrawals and then display their balance
hiro.make_deposit(753)
hiro.make_withdrawal(666)
hiro.make_withdrawal(666)
hiro.make_withdrawal(666)
print(hiro.name)
print(hiro.account_balance)
#  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

chris.transfer(hiro, 1)

print(chris.name)
print(chris.account_balance)
print(hiro.name)
print(hiro.account_balance)