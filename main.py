#  Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, currency):
        self.currency = currency

    @abstractmethod
    def pay(self,amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата картой: {amount} {self.currency}")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Оплата через PayPal: {amount} {self.currency}")

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата криптокошельком: {amount} {self.currency}")

def create_payment():
    print("Доступные методы оплаты: card / paypal / crypto")
    pay_typ = input("Выберите тип оплаты: ").lower()
    currency = input("Введите валюту (например, USD, EUR, BTC): ")

    if pay_typ == "card":
        return CreditCardPayment(currency)
    elif pay_typ == "paypal":
        return PayPalPayment(currency)
    elif pay_typ == "crypto":
        return CryptoPayment(currency)
    else:
        print("Неверный тип оплаты!")
        return None

# --- тест ---
payments = []

for i in range(3):
    p = create_payment()
    if p:
        payments.append(p)

for payment in payments:
    amount = float(input("Введите сумму: "))
    payment.pay(amount)