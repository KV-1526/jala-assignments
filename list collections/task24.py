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

new_student = Student("David", 18, "10th")

# Insert the new student at index 1
students.insert(1, new_student)

for student in students:
    print(student.name, student.age, student.grade)