import DBAccess
import sys
import getpass

def AskLoginPass():
	while 1:
		login = input("Vvedite login\n")
		password = input("Vvedite password\n")
		#login = 'Admin'
		#password = 'Admin'
		if DBAccess.Control(login, password):
			return True			
		else:
			return False			
			
def AskIsRegistered():
	result = input("Have you registered? (Y/N)\n")
	while 1: 		
		res = result.lower()
		if res == 'y':
			return True
		elif res == 'n':
			return False
		elif res == 'q':
			print("Goodbay")
			sys.exit(1)
		else:
			print("Invalid answer")
			result = input()
		
def Register():
	login = input("Viberete login\n")
	while 1:
		if DBAccess.FreeLogin(login):
			break
		else:
			print("Login isn't free. Choose another one")
			login = input()
	
	password = getpass.getpass("Choose the password\n")
	while 1:		
		if len(password) > 2:
			password1 = getpass.getpass("Confirm the password\n")
			if password == password1:
				break
			else:
				print("Passwords not coincide")
				password = None
				password1 = None
		else:
			print("Password must have more symbols")
		password = getpass.getpass("Choose the password\n")
	
	date = input("Write you date of birth (YYYY-MM-DD)\n")
	while 1:
		if len(date) == 10:
			break
		else:
			date = input("Invalid date! Please write one more time\n")
	
		
Register()
