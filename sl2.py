import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

#cur.execute("CREATE TABLE Users (name TEXT);")

#names = input("Add name: ")

#cur.execute("INSERT INTO Users (name) VALUES ('Kirill')")

#cur.execute("DELETE FROM Users")

#cur.execute("SELECT rowid, name FROM Users WHERE name='Anna'")

cur.execute("UPDATE Users SET name='Kate' WHERE name='Anna'")

res = cur.fetchall()
connection.commit()

print(res)

connection.close()

