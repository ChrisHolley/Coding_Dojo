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
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer(self, username, amount):
        username.account_balance += amount
        self.account_balance-= amount
        return self

class BankAccount:
    def __init__(self, int_rate = .01, balance = '99'):
        self.interest = int_rate
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            return self
        else:
            print("Insufficient funds")
        return self
    def display_account_info(self):
        print("Balance:", self.account_balance)
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            print("Interest:", self.account_balance * self.interest)
        return self    

# david = BankAccount(.03, 99)
# print(david.account_balance)
# david.deposit(100)
# print(david.account_balance)
# david.withdraw(200).deposit(999)
# david.display_account_info()
# david.yield_interest()

daredevil = BankAccount(.05, 0)
daredevil.deposit(50).deposit(50).deposit(400).withdraw(1).yield_interest().display_account_info()
kingpin = BankAccount(.1, 100000000)
kingpin.deposit(1000000).deposit(8888).withdraw(9999999).withdraw(9999999).withdraw(9999999).withdraw(9999999).yield_interest().display_account_info()







# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
#  To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
        # The class should also have the following methods:
# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like this:


# #  Create 3 instances of the User class
# chris = User("Christopher")
# tony = User("Antoinette")
# hiro = User("Hiro")
# print(chris.name)
# print(chris.account_balance)
# print(tony.name)
# print(tony.account_balance)
# print(hiro.name)
# print(hiro.account_balance)
# #  Have the first user make 3 deposits and 1 withdrawal and then display their balance
# chris.make_deposit(109).make_deposit(999).make_deposit(999).make_deposit(999).make_deposit(109).make_deposit(109).make_withdrawal(12)
# print(chris.name)
# print(chris.account_balance)
# #  Have the second user make 2 deposits and 2 withdrawals and then display their balance
# tony.make_deposit(999).make_deposit(676)
# tony.make_withdrawal(899).make_withdrawal(149)
# print(tony.name)
# print(tony.account_balance)
# #  Have the third user make 1 deposits and 3 withdrawals and then display their balance
# hiro.make_deposit(753)
# hiro.make_withdrawal(666).make_withdrawal(666).make_withdrawal(666)
# print(hiro.name)
# print(hiro.account_balance)
# #  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
# chris.transfer(hiro, 1).transfer(hiro, 1).transfer(hiro, 999).transfer(hiro, 999)
# print(chris.name)
# print(chris.account_balance)
# print(hiro.name)
# print(hiro.account_balance)

