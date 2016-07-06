import sqlite3 as sql

connector = sql.connect('BioDataBase.db')
cursor = connector.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, login TEXT, password TEXT, date_of_birth TEXT)')
cursor.execute('CREATE TABLE data (user_id INTEGER, request_id INTEGER, date TEXT, physical REAL, emotional REAL, intellectual REAL, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(request_id) REFERENCES request(id))')
cursor.execute('CREATE TABLE request (id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, duration INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))')

cursor.execute('INSERT INTO users (login, password, date_of_birth) VALUES ("admin", "admin", "24-10-1996")')

connector.commit()
connector.close()
