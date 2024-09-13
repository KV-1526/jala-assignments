class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = []

for i in range(1, 11):
    name = input(f"Enter name for student {i}: ")
    age = int(input(f"Enter age for student {i}: "))
    grade = input(f"Enter grade for student {i}: ")
    students.append(Student(name, age, grade))

for student in students:
    print(student.name, student.age, student.grade)