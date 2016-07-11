from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as tm
import DBAccess as DB
from datetime import datetime, timedelta
import Graph
import CreateWindow
import Bio
  
class NewBiorhythms:	
	def __init__(self, master, userData):
		self.slave = Toplevel(master)
		self.slave.title('New Biorhythms')
		self.set_center(self.slave)		
		self.frame = LoginFrame(self.slave, userData)					
	
	def set_center(self, slave):
		slave.withdraw()
		slave.update_idletasks()
		x = (slave.winfo_screenwidth() - slave.winfo_reqwidth()) / 2
		y = (slave.winfo_screenheight() - slave.winfo_reqheight()) / 2
		slave.geometry("+%d+%d" % (x, y))
		slave.deiconify()
		
	def getAccept(self):		
		#self.slave.grab_set()
		self.slave.focus_set()
		self.slave.wait_window()
		return True
	
class LoginFrame(Frame):
	def __init__(self, master, userData):
		super().__init__(master)
				
		self.infLB = Label(self, text="Вариант задания интервала:", font=("Arial", 14))
		self.infLB.grid(columnspan = 2, pady = (10, 0), padx = (5, 5))
		
		self.temp = False
		self.user = userData
		
		requestList = ["Длительность с текущего дня", "Временной интервал"]
		self.ComboBox = Combobox(self,values = requestList, width = 25, height=5,state='readonly', font=("Arial", 12))
		self.ComboBox.grid(columnspan = 2, pady=(5, 5), padx=(5, 5))
		self.ComboBox.bind("<<ComboboxSelected>>", self._combo_box_change)
		self.ComboBox.current(0)
				
		self.dateLB = Label(self, text = "Длительность прогноза", font=("Arial", 11))
		self.dateLB.grid(columnspan = 2, pady = (5, 5))
			
		self.durationEntry = Entry(self, font=("Arial", 11), justify = "center")	
		self.durationEntry.insert(0, "1")
		self.durationEntry.grid(columnspan = 2, pady = (5, 5))
		
		self.applyBT = Button(self, text = "Apply", command = self._apply_btn_clickked)
		self.applyBT.grid(columnspan = 2, pady = (5, 15))
				
		self.temp = False
				
		self.pack()
		
	def _combo_box_change(self, event):
		if self.ComboBox.current() == 0:
			if self.temp:
				self.infLB.destroy()
				self.startDateLB.destroy()
				self.startEntry.destroy()
				self.finishDateLB.destroy()
				self.finishEntry.destroy()
				self.applyBT.destroy()
			else: 
				self.dateLB.destroy()
				self.start.destroy()
				self.applyBT.destroy()
			
			self.dateLB = Label(self, text = "Длительность прогноза", font=("Arial", 11))
			self.dateLB.grid(columnspan = 2, pady = (5, 5))
			
			self.durationEntry = Entry(self, font=("Arial", 11), justify = "center")	
			self.durationEntry.insert(0, "1")
			self.durationEntry.grid(columnspan = 2, pady = (5, 5))
		
			self.applyBT = Button(self, text = "Apply", command = self._apply_btn_clickked)
			self.applyBT.grid(columnspan = 2, pady = (5, 15))
			
			self.temp = True
		else:			
			self.dateLB.destroy()
			self.durationEntry.destroy()
			self.applyBT.destroy()
			
			self.startDateLB = Label(self, text = "Начало прогноза", font=("Arial", 11))
			self.startDateLB.grid(columnspan = 2, pady = (5, 5))
			
			self.startEntry = Entry(self, font=("Arial", 11), justify = "center")	
			self.startEntry.insert(0, (datetime.today()).strftime('%d-%m-%Y'))
			self.startEntry.grid(columnspan = 2, pady = (5, 5))
			
			self.finishDateLB = Label(self, text = "Конец прогноза", font=("Arial", 11))
			self.finishDateLB.grid(columnspan = 2, pady = (5, 5))
			
			d = timedelta(days = 1)
			self.finishEntry = Entry(self, font=("Arial", 11), justify = "center")	
			self.finishEntry.insert(0, (datetime.today() + d).strftime('%d-%m-%Y'))
			self.finishEntry.grid(columnspan = 2, pady = (5, 5))
			
			self.applyBT = Button(self, text = "Apply", command = self._apply_btn_clickked)
			self.applyBT.grid(columnspan = 2, pady = (5, 15))
			
			self.temp = True		
		
	def _apply_btn_clickked(self):
		if self.ComboBox.current() == 0:
			try:
				duration = int(self.durationEntry.get()) + 1					
				requestID = DB.AddRequest(self.user[0], (datetime.today()).strftime('%d-%m-%Y'), duration)
				DataSet = Bio.CalculateBiorhythmsInterval(self.user[0], self.user[3], datetime.today(), duration, requestID)
			except: 
				tm.showerror("Date error", "Неверная длительность прогноза")					
				return
		else:
			try:
				dateS = datetime.strptime(self.startEntry.get(), '%d-%m-%Y')
				dateF = datetime.strptime(self.finishEntry.get(), '%d-%m-%Y')
				d = timedelta(days = 1)
				dateF += d
				duration =  dateF - dateS
				duration = duration.days												
				if duration < 0:
					tm.showerror("Date error", "Неверный интервал прогноза")
					return
				requestID = DB.AddRequest(self.user[0], (dateS).strftime('%d-%m-%Y'), duration)
				DataSet = Bio.CalculateBiorhythmsInterval(self.user[0], self.user[3], dateS, duration, requestID)
			except: 
				tm.showerror("Date error", "Неверный интервал прогноза")
				return
				
		DB.WriteData(DataSet)
		tm.showinfo("Forecast success", "Прогноз составлен успешно")				
		self.master.destroy()
