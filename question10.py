# create a Account class with two attributes -balence and account number
# create methods for credit,debit and printing he balance


class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accountno = accno

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "is debited")
        print("Balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credit")
        print("Balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 3160)
acc1.debit(1000)
acc1.credit(1500)
