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