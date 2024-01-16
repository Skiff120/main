import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

cursor.exception