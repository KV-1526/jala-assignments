class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student("Alice", 18, "10th"),
    Student("Bob", 17, "9th"),
    Student("Charlie", 19, "11th")
]

for student in students:
    print(student.name, student.age, student.grade)