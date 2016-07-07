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
			#Тут вызывай свой метод DataSet - кортеж кортежей, duration интовское значение длительности
			print("Прогноз составлен")
			break
		except:
			print("Неверная продолжительность. Попробуйте снова")

def AskIsRecoverResults(user):
	if DBAccess.HaveResults(user):
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
		
def AskRecoverVersion(user):
	print("Укажите интервал прогноза")	
	versions = DBAccess.GetRequest(user)
	for i in range(0, len(versions)):
		date = datetime.strptime(versions[i][2], '%d-%m-%Y')
		d = timedelta(days = int(versions[i][3]))
		print("%i) %10s - %10s" % (i+1, date.strftime('%d-%m-%Y'), (date + d).strftime('%d-%m-%Y')))
	
	while 1:
		answer = int(input())
		if answer - 1 < len(versions):
			return versions[answer - 1]
		else:
			print("Неверный индекс")
		
def RecoverVersion(request):
	d = timedelta(days = int(request[3]))	
	print("Восстанавливаем данные в промежутке %s - %s" % (request[2], (datetime.strptime(request[2], '%d-%m-%Y') + d).strftime('%d-%m-%Y')))
	data = DBAccess.GetData(request[0])
	
	DataSet = []
	
	for line in data:  		
		userID = int(line[0])
		requestID = int(line[1])
		date = line[2]
		phis = float(line [3])
		emo = float(line [4])
		intell = float(line[5])
		DataSet.append([userID, requestID, date, phis, emo, intell])
		
	#Тут вызывать построение графика

		
		
		
		
		
		
		
		
		
		
		
		
