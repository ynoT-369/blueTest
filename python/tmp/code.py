class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __repr__(self):
        return f"student name: {self.name}"

    def average_grade(self):
        return sum(self.grades)/len(self.grades)

    @classmethod
    def test_class(cls):
        print(f"class method {cls}")

student = Student("Tony", [60, 70, 50])
print(student)
print(student.average_grade())

Student.test_class()
student.test_class()
print(__name__)
