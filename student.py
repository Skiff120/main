class Student:
    count = 0
    while count == 0:
        def __init__(self, name="Витя", height=178):
            self.grn = 0
            self.zat = 6000
            self.zp = 5000
            self.name = name
            self.height = height
            Student.count += 1

        def __str__(self):
            return print(f"Я {self.name}. Мій зріст{self.height} см. Ваша зарплата {self.zp}, ваші затрати{self.zat}")

        def print(self):
            if self.dej == "работа":
                self.grn += self.zp
                print(self.grn)
            else:
                self.grn -= self.zat
                print(self.grn)
