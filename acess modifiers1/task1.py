class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id        # Public attribute
        self.student_name = student_name    # Public attribute

    def display_details(self):
        """
        Display student details.
        """
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")

# Input: Creating an instance of Student with given details
student = Student(student_id=101, student_name="Santhi")

# Output: Displaying the student details
student.display_details()
