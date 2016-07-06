import Bio
import DBAccess
from datetime import datetime, timedelta

def AskBiorhythms(user):	
	while 1:
		duration = input("Введите количество дней для прогноза\n")
		try:
			duration = int(duration)
			requestID = DBAccess.AddRequest(user[0], (datetime.today()).strftime('%d-%m-%Y'), duration)
			DataSet = Bio.CalculateBiorhythms(user[0], user[3], duration, requestID)
			DBAccess.WriteData(DataSet)
			print("Прогноз составлен")
			break
		except:
			print("Неверная продолжительность. Попробуйте снова")

def AskIsRecoverResults(user):
	if DBAccess.HaveResults(user[0]):
		result = input("Хотите восстановить предыдущий результат? (Y/N)\n")
		while 1: 		
			result = result.lower()
			if result == 'y':
				return True
			elif result == 'n':
				return False
			else:
				print("Попробуйте еще раз")
				result = input()			
	else:
		return False
		

