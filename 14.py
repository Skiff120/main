import sqlite3
import math

connection = sqlite3.connect("db3.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer primary key autoincrement not null, login TEXT, password TEXT, email TEXT);")
connection.commit()

connection.close()



def restart():
   chois()
def login():
    print("Вход в аккаунт")
    log = input("Введите логин: ")
    if len(log) <= 3:
        print("Логин должен содержать больше 3-х символов")
        restart()
    elif len(log) > 19:
        print("Логин не может содержать больше 19-и символов")
        restart()
    password = input("Введите пароль: ")
    if len(password) < 8:
        print("Пароль должен содержать больше 8-ми символов")
        restart()
    elif len(password) > 19:
        print("Длинна пароля не может превышать больше 19-и символов")
        restart()
    connection = sqlite3.connect("db3.sl3", 5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE login='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        print("")
        restart()
    else:
        res = list(res[0])
        if res[2] == password:
            print("Вы успешно вошли в свой аккаунт")
            a = input("Введите первое число: ")
            b = input("Введите действие(+, -, *, /, -^, ^, sqrt, sin, cos, tan, ctg, asin, acos, atan, actg, !, lg, ln): ")
            c = input("Введите второе число: ")
            try:
                if b == "+":
                    print(int(a) + int(c))
                    print(int(a) - int(c))
                elif b == "*":
                    print(int(a) * (c))
                elif b == "/":
                    print(int(a) / int(c))
                elif b == "-^":
                    d = int(a) ** int(c)
                    print(1 / int(d))
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
                elif b == "sin":
                    print(math.sin(math.radians(int(a))))
                    print(math.sin(math.radians(int(c))))
                elif b == "cos":
                    print(math.cos(math.radians(int(a))))
                    print(math.cos(math.radians(int(c))))
                elif b == "tan":
                    print(math.tan(math.radians(int(a))))
                    print(math.tan(math.radians(int(c))))
                elif b == "ctg":
                    print(1 / (math.tan(math.radians(int(a)))))
                    print(1 / (math.tan(math.radians(int(c)))))
                elif b == "asin":
                    print(math.degrees(math.asin(int(a))))
                    print(math.degrees(math.asin(int(c))))
                elif b == "acos":
                    print(math.degrees(math.acos(int(a))))
                    print(math.degrees(math.acos(int(c))))
                elif b == "atan":
                    print(math.degrees(math.atan(int(a))))
                    print(math.degrees(math.atan(int(c))))
                elif b == "actg":
                    print((math.degrees(math.atan(1 / (int(a))))))
                    print((math.degrees(math.atan(1 / (int(c))))))
                elif b == "!":
                    print(math.factorial(int(a)))
                    print(math.factorial(int(c)))
                elif b == "lg":
                    print(math.log(int(a), int(c)))
                elif b == "ln":
                    print(math.log(int(a)))
                    print(math.log(int(c)))
                elif b == "stop":
                    exit(0)
                else:
                    print(":/")
                    restart()
            except ZeroDivisionError as error:
                print(error)
                print(":/")
                restart()
            except ValueError as error1:
                print(error1)
                print(":/")
                restart()
        else:
            print("Неверный логин или пароль")
            restart()

def register():
    print("Регистрация")
    log = input("Введите логин: ")
    if len(log) <= 3:
        print("Логин должен содержать больше 3-х символов")
        restart()
    elif len(log) > 19:
        print("Логин не может содержать больше 19-и символов")
        restart()
    mail = input("Введите електронную почту: ")
    if '@gmail.com' not in mail:
        print("Такой електронной почты не существует")
        restart()
    if len(mail) <= 10:
        print("Ваша електронная почта слишком короткая")
        restart()
    connection = sqlite3.connect("db3.sl3", 5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE login='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        password = input("Введите пароль: ")
        if 'й' in password or 'ц' in password or 'у' in password or 'к' in password or 'е' in password or 'н' in password or 'г' in password or 'ш' in password or 'щ' in password or 'з' in password or 'х' in password or 'ъ' in password or 'ф' in password or 'ы' in password or 'в' in password or 'а' in password or 'п' in password or 'р' in password or 'о' in password or 'л' in password or 'д' in password or 'ж' in password or 'э' in password or 'я' in password or 'ч' in password or 'с' in password or 'м' in password or 'и' in password or 'т' in password or 'ь' in password or 'б' in password or 'ю' in password:
            print("Пароль не может содержать кирилицу")
            restart()
        if '!' in password or '@' in password or '#' in password or '$' in password or '%' in password or '^' in password or '&' in password or '*' in password or '(' in password or ')' in password or '`' in password or '~' in password or ',' in password or '.' in password or '<' in password or '>' in password or '/' in password or '?' in password or '|' in password or '"' in password or '\'' in password or ';' in password or ':' in password or '[' in password or ']' in password or '{' in password or '}' in password or '\\' in password:
            print("Пароль не может содержать данные символы: !@#$%^&*(){}{}:;'?><,./`~\"\\")
            restart()
        if len(password) < 8:
            print("Пароль должен содержать больше 8-ми символов")
            restart()
        elif len(password) > 19:
            print("Длинна пароля не должна содержать больше 19-и символов")
            restart()
        cur.execute(f"INSERT INTO Users (login, password, email) VALUES ('{log}', '{password}', '{mail}')")
        connection.commit()
        print("Вы зарегистрировались")
        a = input("Введите первое число: ")
        b = input("Введите действие(+, -, *, /, -^, ^, sqrt, sin, cos, tan, ctg, asin, acos, atan, actg, !, lg, ln): ")
        c = input("Введите второе число: ")
        try:
            if b == "+":
                print(int(a) + int(c))
            elif b == "-":
                print(int(a) - int(c))
            elif b == "*":
                print(int(a) * int(c))
            elif b == "/":
                print(int(a) / int(c))
            elif b == "-^":
                d = int(a) ** int(c)
                print(1 / int(d))
            elif b == "^":
                print(int(a) ** int(c))
            elif b == "sqrt":
                print(math.sqrt(int(a)))
                print(math.sqrt(int(c)))
            elif b == "sin":
                print(math.sin(math.radians(int(a))))
                print(math.sin(math.radians(int(c))))
            elif b == "cos":
                print(math.cos(math.radians(int(a))))
                print(math.cos(math.radians(int(c))))
            elif b == "tan":
                print(math.tan(math.radians(int(a))))
                print(math.tan(math.radians(int(c))))
            elif b == "ctg":
                print(1 / (math.tan(math.radians(int(a)))))
                print(1 / (math.tan(math.radians(int(c)))))
            elif b == "asin":
                print(math.degrees(math.asin(int(a))))
                print(math.degrees(math.asin(int(c))))
            elif b == "acos":
                print(math.degrees(math.acos(int(a))))
                print(math.degrees(math.acos(int(c))))
            elif b == "atan":
                print(math.degrees(math.atan(int(a))))
                print(math.degrees(math.atan(int(c))))
            elif b == "actg":
                print((math.degrees(math.atan(1 / (int(a))))))
                print((math.degrees(math.atan(1 / (int(c))))))
            elif b == "!":
                print(math.factorial(int(a)))
                print(math.factorial(int(c)))
            elif b == "lg":
                print(math.log(int(a), int(c)))
            elif b == "ln":
                print(math.log(int(a)))
                print(math.log(int(c)))
            elif b == "stop":
                exit(0)
            else:
                print(":/")
                restart()
        except ZeroDivisionError as error:
            print(error)
            print(":/")
            restart()
        except ValueError as error1:
            print(error1)
            print(":/")
            restart()
    else:
        print("Такой логин уже существует")
        restart()

def chois():
    choise = input("1. Войти\n2. Зарегистрироватся\n")
    if choise == "1":
        login()
    elif choise == "2":
        register()
    else:
        print(":/")
        restart()

chois()

