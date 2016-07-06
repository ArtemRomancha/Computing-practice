import sqlite3 as sql

connector = sql.connect('BioDataBase.db')
cursor = connector.cursor()

cursor.execute('delete from users where id != 1')
cursor.execute('delete from data where user_id != 0')
cursor.execute('delete from request where user_id != 0')

connector.commit()
connector.close()
