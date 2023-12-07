import random

chislo = random.randint(1, 1000000)

if chislo % 2 == 0:
    print("Четное: ", chislo)
else:
    print("Не четное: ", chislo)