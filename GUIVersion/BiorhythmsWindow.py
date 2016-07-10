from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as tm
import DBAccess as DB
from datetime import datetime, timedelta
import Graph
import CreateWindow


class BioFrame(Frame):
	def __init__(self, master):
		super().__init__(master)
		
		self.BioLB = Label(self, text="Составленные прогнозы", font=("Arial", 14))
		self.BioLB.grid(row=0, padx = (5,5), pady = (10, 5))
		
		requestList = self._load_request_list()
		self.ComboBox = Combobox(self,values = requestList, height=5, foreground='#FF0000',state='readonly', font=("Arial", 12))
		self.ComboBox.grid(column = 0, pady=(10, 10), padx=(10, 10))
				
		self.logbtn = Button(self, text="Посмотреть", command = self._view_btn_clickked)
		self.logbtn.grid(columnspan = 2, row = 3, pady=(5, 5))
		
		self.regbtn = Button(self, text="Составить новый", command = self._new_btn_clickked)
		self.regbtn.grid(columnspan = 2, pady=(5, 15))
		
		self.pack()
	
	def _view_btn_clickked(self):		
		global requests		
		request = requests[self.ComboBox.current()]		
		data = DB.GetData(request[0])
		   
		DataSet = []
   
		for line in data:      
			userID = int(line[0])
			requestID = int(line[1])
			date = line[2]
			phis = float(line [3])
			emo = float(line [4])
			intell = float(line[5])
			DataSet.append([userID, requestID, date, phis, emo, intell])
		Graph.CreateGraph(DataSet,int(request[3]))

	def _new_btn_clickked(self):
		global userData		
		cr = CreateWindow.NewBiorhythms(self.master, userData)		
		cr.getAccept()
		
		requestList = self._load_request_list()
		self.ComboBox["values"] = requestList		
			
	def _load_request_list(self):
		global requests	
		requests = DB.GetRequest(userData[0])
			
		requestList = []
		for i in range(0, len(requests)):
			date = datetime.strptime(requests[i][2], '%d-%m-%Y')
			d = timedelta(days = int(requests[i][3] - 1))
			requestList.append("%10s - %10s" % (date.strftime('%d-%m-%Y'), (date + d).strftime('%d-%m-%Y')))
		return requestList

class Main:	
	def __init__(self, master):
		self.master = master
		self.set_center(self.master)
		self.master.title("Biorhythms")			
		BioFrame(self.master)
				
		self.master.mainloop()
		
	def set_center(self, root):
		root.withdraw()
		root.update_idletasks()
		x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
		y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
		root.geometry("+%d+%d" % (x, y))
		root.deiconify()
	


def Run(user):
	global userData 
	userData = user
	root = Tk()	
	Main(root)
		 
userData = 0 
requests = []

