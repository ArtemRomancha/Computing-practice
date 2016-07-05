import sqlite3 as sql

connector = sql.connect('BioDataBase.db')	

def ConnectDB():
	connector = sql.connect('BioDataBase.db')	
	return connector.cursor()

def Control(login, password):
	cursor = ConnectDB()		
	cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password))
	connector.close()
		
	if cursor.fetchone() != None:
		return True
	else: 
		return False