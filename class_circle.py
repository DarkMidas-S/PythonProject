import math

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


circle = Circle(5)
print("Радіус:", circle.radius)
print("Площа кола:", circle.get_area())
