#  Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо  energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5
from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, satiety=50, energy=50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100
        print(f"{self.name} поспал(-а) и полностью восстановил(-а) энергию!")

    def eat(self, food_amount):
        self.satiety = min(100, self.satiety + food_amount)
        print(f"{self.name} поел(-а). Сытость: {self.satiety}/100")

    @abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass

class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy = max(0, self.energy - 2 * activity_level)
            self.satiety = max(0, self.satiety - 2 * activity_level)
            print(f"{self.name} активно играет! Энергия: {self.energy}, Сытость: {self.satiety}")
        else:
            print(f"{self.name} слишком голоден, чтобы играть!")

    def make_sound(self):
        print("Мяу!")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"{self.name} поймал(-а) мышь!")
            if self.satiety > 40:
                print(f"{self.name} играет с мышью.")
                self.energy = max(0, self.energy - 10)
            else:
                print(f"{self.name} съел(-а) мышь.")
                self.eat(20)
        else:
            print(f"{self.name} слишком устал(-а), чтобы ловить мышь.")

class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy = max(0, self.energy - activity_level // 2)
            self.satiety = max(0, self.satiety - activity_level // 2)
            print(f"{self.name} играет! Энергия: {self.energy}, Сытость: {self.satiety}")
        else:
            print(f"{self.name} слишком голоден, чтобы играть!")

    def make_sound(self):
        print("Гав!")

    def fetch_ball(self):
        if self.satiety > 10:
            print(f"{self.name} принес(-ла) мяч!")
            self.energy = max(0, self.energy - 5)
        else:
            print(f"{self.name} слишком голоден, чтобы играть с мячом!")

cat = Cat("Мурка")
dog = Dog("Бім")

cat.make_sound()
dog.make_sound()

cat.play(10)
cat.catch_mouse()
cat.sleep()

dog.play(8)
dog.fetch_ball()
dog.eat(20)
dog.play(5)