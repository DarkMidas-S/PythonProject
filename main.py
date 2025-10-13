# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).

class BankAccount:
    currency_rates = {
        "UAH": 1.0,
        "USD": 39.5,
        "EUR": 42.8,
        "GBP": 49.2,
        "PLN": 10.0
    }

    def __init__(self, name, currency, balance=0.0):
        self.name = name
        self.check_currency(currency)
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.currency = currency
        self.balance = float(balance)

    def __str__(self):
        return f"Клиент: {self.name} | Баланс: {self.balance:.2f} {self.currency}"

    def info(self):
        print("******************************************************")

        print(f"Клиент: {self.name}")
        print(f"Баланс: {self.balance:.2f} {self.currency}")
        print(f"Курсы валют: {self.__class__.currency_rates}")
        print("******************************************************")
        print()

    def check_currency(self, currency):
        if currency not in self.__class__.currency_rates:
            raise ValueError(f"Валюта '{currency}' не поддерживается.")
        return True

    def convert(self, amount, from_currency, to_currency, ndigits=2):
        self.check_currency(from_currency)
        self.check_currency(to_currency)
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной.")
        uah = amount * BankAccount.currency_rates[from_currency]
        result = uah / BankAccount.currency_rates[to_currency]
        return round(result, ndigits)

    def change_currency(self, new_currency):
        self.check_currency(new_currency)
        if new_currency == self.currency:
            print("Валюта уже установлена.")
            return
        self.balance = self.convert(self.balance, self.currency, new_currency)
        self.currency = new_currency
        print(f"Валюта счёта изменена. Новый баланс: {self.balance:.2f} {self.currency};")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount
        print(f"Счёт пополнен на {amount:.2f} {self.currency}. Баланс: {self.balance:.2f} {self.currency};")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте.")
        self.balance -= amount
        print(f"Снято {amount:.2f} {self.currency}. Баланс: {self.balance:.2f} {self.currency};")

acc = BankAccount("Иван", "USD", 100)
acc.info()
acc.deposit(50)
acc.withdraw(30)
print("50 USD в EUR =", acc.convert(50, "USD", "EUR"))
acc.change_currency("EUR")
print(acc)
