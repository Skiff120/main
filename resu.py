result = []


def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a/b
    except ValueError as error:
        print("ValueError", error)
    except IndexError as error2:
        print("IndexError", error2)
    except TypeError as error3:
        print("TypeError:", error3)
    except ZeroDivisionError as error4:
        print("ZeroDivisionError:", error4)


data = {10: 2, 2: 5, "123": 4, 18: 0, 0: 15, 8: 4}  # []: 15 - list not allowed as a Key in Dictionary
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)

