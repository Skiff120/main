class Student:
    print("hello")
    def __init__(self, height):
        self.height = 150
        print("I am studentf")


student = Student(height = 160)
student1 = Student(height = 170)
student2 = Student(height = 150)
print(student.height)
print(student1.height)
print(student2.height)