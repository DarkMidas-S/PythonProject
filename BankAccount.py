class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, add_money):
        self.balance += add_money

    def withdraw(self, withdraw_money):
        self.balance -= withdraw_money

    def info(self):
        print(f"Владелец счета: {self.owner}")
        print(f"на счете: {self.balance}")

owner1 = BankAccount("David", 1000)
owner1.info()
print()

owner1.deposit(1200)
owner1.info()
print()

owner1.withdraw(200)
owner1.info()
