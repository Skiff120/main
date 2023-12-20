class Human:

    def __init__(self, name):
        self.name = name

class Car:

    def __init__(self, marka):
        self.marka = marka
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def passengers_info(self):
        print(f"Авто: {self.marka} \n", end= '')
        if self.passengers != []:
            print("Зараз у салоні: ")
            for p in self.passengers:
                print(p.name)
        else:
            print("Пасажири відсутні")


human1 = Human("Vitalya")
human2 = Human("Sanya")
human3 = Human("Leha")
car = Car("BMW X9")
car.add_passenger(human1)
car.add_passenger(human2)
car.add_passenger(human3)
car.passengers_info()


