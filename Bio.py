from datetime import datetime, timedelta
import math

def CalculateBiorhythms(userId, date, duration):
	date = datetime.strptime(date, '%Y-%m-%d')
	today = datetime.today()
	delta = today - date
	delta = delta.days
	
	DataSet = []
	
	d = timedelta(days = 0)
	
	for i in range(0, duration):
		temp = 2 * math.pi * delta 
		phisical = math.sin(temp / 23) * 100
		emotional = math.sin(temp / 28) * 100
		intellectual = math.sin(temp / 33) * 100
		DataSet.append([userId, str(today + d), phisical, emotional, intellectual])
		d += timedelta(days = 1)
		delta += 1
	return DataSet