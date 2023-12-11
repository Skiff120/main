import random

a = random.randint(1, 1000000)
def chislo():
    if a % 2 == 0:
        print("Четное: ", a)
    else:
        print("Не четное: ", a)

chislo()