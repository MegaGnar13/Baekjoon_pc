class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        self.balance-=amount
        return self.balance


    def deposit(self, amount):
        self.balance+=amount
        return self.balance

    def getBalance(self):
        return self.balance


if __name__ == '__main__':
    b1 = BankAccount(500)
    b2 = BankAccount(2000)
    b1.withdraw(400)
    print(b1.getBalance())
    b2.deposit(1000)
    print(b2.getBalance())
    b2.withdraw(5000)
    print(b2.getBalance())
