#  Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

class Cart:
    def __init__(self, client, items = None):
        self.client = client
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    def add_item(self, item):
        self.items.append(item)

    def delet_item(self, item):
        self.items.remove(item)

    def info_cart(self):
        print(f"\nКлиент: {self.client}")
        print()
        print(f"Корзина:")
        print()
        for i in self.items:
            print(i)
            print("**************")

products = ["Молоко", "Яйца", "Хлеб"]
client1 = Cart("David", products)
client1.info_cart()

client1.add_item("Сода")
client1.info_cart()

client1.delet_item("Молоко")
client1.info_cart()

# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.

class Phone:
    def __init__(self, number, battery_level = 100):
        self.number = number
        self.battery_level = battery_level

    def percent(self, percent):
        self.battery_level -= percent
        if self.battery_level < 20:
            print(f"У вашего телефона {self.battery_level} %. Перейдите в режим энергосбережения!")
        elif self.battery_level == 0:
            print("Ваш телефон полностью разряжен!")

    def info(self):
        print(f"Номер телефона: {self.number}")
        print(f"Уровень зарядки: {self.battery_level} %\n")

my_phone = Phone("+34 777 888 111")
my_phone.info()

my_phone.percent(15)
my_phone.info()

my_phone.percent(70)
my_phone.info()