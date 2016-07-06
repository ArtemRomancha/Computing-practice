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
		
def FreeLogin(login):
	cursor = ConnectDB()
	cursor.execute("SELECT * FROM users WHERE login = ? ", (login, ))
	connector.close()
	
	if cursor.fetchone() == None:
		return True
	else:
		return False
		
def AddUser(login, password, birthdate):
	connector = sql.connect('BioDataBase.db')	
	cursor = connector.cursor()
	cursor.execute("INSERT INTO users (login, password, date_of_birth) VALUES (?, ?, ?)", (login, password, birthdate))	
	connector.commit()
	connector.close()
	
def AddRequest(userId, date, duration):
	connector = sql.connect('BioDataBase.db')
	cursor = connector.cursor()
	cursor.execute("INSERT INTO request (user_id, date, duration) VALUES (?, ?, ?)", (userId, date, duration))
	requestID = cursor.lastrowid
	connector.commit()
	connector.close()
	return requestID
	
def WriteData(DataSet):
	connector = sql.connect('BioDataBase.db')
	cursor = connector.cursor()
	cursor.executemany("INSERT INTO data VALUES(?, ?, ?, ?, ?, ?)", DataSet)	
	connector.commit()
	connector.close()
	
def GetDateOfBirth(login):
	connector = sql.connect('BioDataBase.db')
	cursor = connector.cursor()
	cursor.execute("SELECT * FROM users WHERE login = ?", (login, ))
	row = cursor.fetchone()
	connector.close()
	return row
