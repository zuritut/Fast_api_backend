import sqlite3

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

print("Db connected")