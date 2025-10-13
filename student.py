class Student:
    def __init__(self, name, age, grades = None):
        self.name = name
        self.age = age
        if grades is None:
            self.grades = []
        else:
            self.grades = list(grades)

    def add_grade(self, grade):
        self.grades.append(grade)
    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

class SchoolStudent(Student):
    def __init__(self, name, age, school, grades = None):
        super().__init__(name, age, grades)
        self.school = school

    def best_grade(self):
        if len(self.grades) == 0:
            return 'Нет оценок'
        return max(self.grades)

    def info(self):
        nxt = input("Желаете вывести все оценки вместе с информацией? (да/нет): ")
        start = f"{self.name}, {self.age} лет, учится в {self.school}, средний балл: {self.average():.2f}"

        if nxt == 'да':
            return start + f", оценки: {self.grades}"
        else:
            return start


s2 = SchoolStudent("Мария", 14, "Школа №5")
s2.add_grade(5)
s2.add_grade(4)

print(s2.info())        # Мария, 14 лет, учится в Школа №5
print("Лучшая оценка:", s2.best_grade())
