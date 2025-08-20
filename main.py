class Student:
    def __init__(self, name, age, yaer):
        self.name = name
        self.age = age
        self.yaer = yaer

    def info(self):
        print(f" Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Yaer in university: {self.yaer}")


student1 = Student(name= "David", age= 23, yaer= 5)
student1.info()

student2 = Student(name= "Kris", age= 21,yaer= 3)
student2.info()

student3 = Student( name=  "Elizaveta", age= 18, yaer= 1)
student3.info()

student_list = []

for i in range(3):
    print()
    student_name = input("ведите имя студента: ")
    student_age = int(input("Введите возраст студента: "))
    student_yaer = int(input("ведите год оюучения: "))
    student = Student(student_name, student_age, student_yaer)
    student.info()
    student_list.append(student)

for student in student_list:
    print(student)



