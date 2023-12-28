import random

class Human:
    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 2000
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        if home != None:
            print("Продали будинок")
        self.home = home
        print("Придбали новий будинок")

    def get_car(self, car):
        if car != None:
            print(f"Продали авто марки {car.marka}")
        self.car = car
        print(f"Придбана автівка, марка {car.marka}")

    def work(self):
        print("Ідем працювати :(")
        d = random.randint(50, 200)
        print(f"Сьогодні заробили {d}$")
        self.money += d
        self.enjoyment -= 5
        self.home.food -= 2

    def chill(self):
        print("Отдыхаем")
        n = random.randint(20, 40)
        print(f"Вы отдохнули и у вас повысилось настроение на {n} процентов")
        self.enjoyment += n

    def shopping(self):
        print(f"Идём за покупками")
        money = random.randint(250, 500)
        print(f"Сегодня я потратил {money} гривен в магазине")
        self.money -= money
        self.home.food += random.randint(5, 10)
        self.enjoyment += random.randint(-5, 10)


    def clean_house(self):
        if self.home == None:
            print(f"Вы не можете убираться")
        else:
            print("Убираемся")
            self.home.cleanlinies_level += 1
            self.enjoyment -= 20

    def life(self):
        pass

    def is_alive(self):
        if self.money <= 0 or self.home.food <= 0:
            return False
        return True

    def info(self):
        print("===============================")
        print(f"Стан {self.name}:")
        print(f"Рівень задоволення - {self.enjoyment}")
        print(f"Залишок грошей     - {self.money}")
        print(f"Наявність їжі      - {self.home.food}")
        print(f"Порядок в кімнаті  - {self.home.cleanlinies_level}")




class Car:
    def __init__(self, marka):
        self.marka = marka
        self.passengers = []

    def add_passenger(self, *human):
        for h in human:
            self.passengers.append(h)

    def passengers_info(self):
        print(f"Авто {self.marka}, ", end='')
        if self.passengers != []:
            print(f"зараз в салоні:")
            for p in self.passengers:
                print(p.name)
        else:
            print("пасажири відсутні.")


class Home:
    def __init__(self):
        self.food = 50
        self.cleanlinies_level = 50




human = Human("Serg", car=Car("BMW X11"), home=Home())
day = 1
while(human.is_alive()):
    print()
    print(f"День {day}")
    human.life()
    human.info()
    day += 1

'''car = Car("BMW X9")
car.add_passenger(human1, human2, human3)
car.passengers_info()'''