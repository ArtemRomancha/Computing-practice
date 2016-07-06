from datetime import datetime, timedelta
import math

def CalculateBiorhythms(userId, date, duration, requestID):
	date = datetime.strptime(date, '%d-%m-%Y')
	today = datetime.today()
	delta = today - date
	delta = delta.days
	
	DataSet = []
	
	d = timedelta(days = 0)
	
	for i in range(0, duration):
		temp = 2 * math.pi * delta 
		phisical = round(math.sin(temp / 23) * 100, 4)
		emotional = round(math.sin(temp / 28) * 100, 4)
		intellectual = round(math.sin(temp / 33) * 100, 4)
		DataSet.append([userId, requestID, (today + d).strftime('%d-%m-%Y'), phisical, emotional, intellectual])
		d += timedelta(days = 1)
		delta += 1
	return DataSet
