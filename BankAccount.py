# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

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
