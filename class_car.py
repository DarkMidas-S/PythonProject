# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.

class Car:
    def __init__(self, brand, year, is_ready = False):
        self.brand = brand
        self.yaer = year
        self.is_ready = is_ready

    def start_engine(self):
        if self.is_ready == False:
            self.is_ready = True
        else:
            self.is_ready = False
    def move(self):
        if self.is_ready == False:
            print("Автомобиль не готов к поездке")
        else:
            print("Автомобиль готов к поездке")


car1 = Car("BMW", 2025)
car1.move()

car1.start_engine()
car1.move()