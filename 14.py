import sqlite3
import math

connection = sqlite3.connect("db2.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer primary key autoincrement not null, login TEXT, password TEXT);")
connection.commit()

connection.close()

def login():
    print("Вход в аккаунт")
    log = input("Введите логин: ")
    password = input("Введите пароль: ")
    connection = sqlite3.connect("db2.sl3", 5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE login='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        print("")
        exit(0)
    else:
        res = list(res[0])
        if res[2] == password:
            print("Вы успешно вошли в свой аккаунт")
            a = input("Введите первое число: ")
            b = input("Введите действие: ")
            c = input("Введите второе число: ")
            try:
                if b == "+":
                    print(int(a) + int(c))
                    print(int(a) - int(c))
                elif b == "*":
                    print(int(a) * (c))
                elif b == "/":
                    print(int(a) / int(c))
                elif b == "^":
                    print()
                elif b == "^":
                    print(int(a) ** int(c))
                elif b == "sqrt":
                    print(math.sqrt(int(a)))
                    print(math.sqrt(int(c)))
                elif b == "sin":
                    print(math.sin(math.radians(int(a))))
                    print(math.sin(math.radians(int(c))))
                elif b == "sin":
                    print(math.cos(math.radians(int(a))))
                    print(math.sin(math.radians(int(c))))
                else:
                    print(":/")
                    exit(0)
            except ZeroDivisionError as error:
                print(error)
                print(":/")
                exit(0)
            except ValueError as error1:
                print(error1)
                print(":/")
                exit(0)
        else:
            print("Неверный логин или пароль")
            exit(0)

def register():
    print("Регистрация")
    log = input("Введите логин: ")
    connection = sqlite3.connect("db2.sl3", 5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE login='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        password = input("Введите пароль: ")
        cur.execute(f"INSERT INTO Users (login, password) VALUES ('{log}', '{password}')")
        connection.commit()
        print("Вы зарегистрировались")
        a = input("Введите первое число: ")
        b = input("Введите действие: ")
        c = input("Введите второе число: ")
        try:
            if b == "+":
                print(int(a) + int(c))
            elif b == "-":
                print(int(a) - int(c))
            elif b == "*":
                print(int(a) * (c))
            elif b == "/":
                print(int(a) / int(c))
            elif b == "^":
                print()
            elif b == "^":
                print(int(a) ** int(c))
            elif b == "sqrt":
                print(math.sqrt(int(a)))
                print(math.sqrt(int(c)))
            elif b == "sin":
                print(math.sin(math.radians(int(a))))
                print(math.sin(math.radians(int(c))))
            elif b == "sin":
                print(math.cos(math.radians(int(a))))
                print(math.sin(math.radians(int(c))))
            else:
                print(":/")
                exit(0)
        except ZeroDivisionError as error:
            print(error)
            print(":/")
            exit(0)
        except ValueError as error1:
            print(error1)
            print(":/")
            exit(0)
    else:
        print("Такой логин уже существует")
        exit(0)

choise = input("1. Войти\n2. Зарегистрироватся\n")
if choise == "1":
    login()
elif choise == "2":
    register()
else:
    print(":/")
    exit(0)

