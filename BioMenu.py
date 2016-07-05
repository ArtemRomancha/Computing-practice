import Bio
import DBAccess

def AskBiorhythms(login):
	user = DBAccess.GetDateOfBirth(login)
	while 1:
		duration = input("Введите количество дней для прогноза\n")
		try:
			DataSet = Bio.CalculateBiorhythms(user[0], user[3], int(duration))
			DBAccess.WriteData(DataSet)
			break
		except:
			print("Неверная продолжительность. Попробуйте снова")
