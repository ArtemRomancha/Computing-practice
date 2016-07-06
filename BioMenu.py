import Bio
import DBAccess
from datetime import datetime, timedelta

def AskBiorhythms(login):
	user = DBAccess.GetDateOfBirth(login)
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
