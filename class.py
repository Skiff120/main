class Student:
    count = 0
    print("Hello")
    def __init__(self, name="No name", height=160):
        self.height = height
        Student.count += 1
        self.name = name


    def __str__(self):
        return (f"Я {self.name}. Мій зріст {self.height} см")

print(Student.count)
student = Student("Vitalik", 170)
student.print()
print(student)

#student = Student(height=160)
#student1 = Student(height=170)
#student2 = Student(height=150)
#print(student.height)
#print(student1.height)
#print(student2.height)
#print(student.count)