import DBAccess
import sys
import getpass

def AskLoginPass():
	while 1:
		login = input("Введите логин\n")
		password = getpass.getpass("Введите пароль\n")
		#login = 'Admin'
		#password = 'Admin'
		if DBAccess.Control(login, password):
			return login			
		else:
			print("Неверный логин или пароль")			
			
def AskIsRegistered():
	result = input("Вы зарегистрированы? (Y/N)\n")
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
			print("Попробуйте еще раз")
			result = input()
		
def Register():
	login = input("Выберите логин\n")
	while 1:
		if DBAccess.FreeLogin(login):
			break
		else:
			print("Такой логин уже занят. Придумайте другой")
			login = input()
	
	password = getpass.getpass("Придумайте пароль\n")
	while 1:		
		if len(password) > 5:
			password1 = getpass.getpass("Подтверите пароль\n")
			if password == password1:
				break
			else:
				print("Пароли не совпадают")
				password = None
				password1 = None
		else:
			print("Пароль должен содержать более 5 символов")
		password = getpass.getpass("Придумайте пароль\n")
	
	date = input("Напишите свою дату рождения в формате YYYY-MM-DD\n")
	while 1:
		if len(date) == 10:
			break
		else:
			date = input("IНеверная дата! Попробуйте еще раз\n")
	DBAccess.AddUser(login, password, date)
	return login
		
