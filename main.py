#
#  Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item)  – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other)  – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min

class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time
    def __str__(self):
        return  self.name

    def __contains__(self, item):
        return item.lower() in [x.lower() for x in self.ingredients]

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print("***********************************")
        print(f"Блюдо: {self.name}")
        print(f"Ингредиенты: {', '.join(self.ingredients)}")
        print(f"Описание: {self.text}")
        print(f"Время приготовления: {self.time} мин.")
        print("***********************************\n")

recipes = [
    Recipe("Пицца", ["мука", "вода", "дрожжи", "томат", "сыр"],
           "Готовим тесто, добавляем ингридиенты и готовим", 30),

    Recipe("Салат", ["томат", "огурец", "зелень", "олия"],
           "Нарезаем овощи, добавляем зелень и поливаем олией", 10),

    Recipe("Суп", ["вода", "картошка", "морковь", "мясо"],
           "Варим все ингридиенты до готовности", 45)
]
print("Рецепты с томатом: ")
for recipe in recipes:
    if "томат" in recipe:
        print(recipe)
print()

min_recipe = min(recipes, key= lambda r: r.time)

print("Рецепт с наименьшим временем приготовления:")
min_recipe.display_info()