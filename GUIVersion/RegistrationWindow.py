from tkinter import *
import tkinter.messagebox as tm
import DBAccess as DB

class regFrame(Frame):
	def __init__(self, master):
		super().__init__(master)
		
		self.userLB = Label(self, text="Username")
		self.passLB = Label(self, text="Password")
		self.confpassLB = Label(self, text="Confirm password")
		self.dateLB = Label(self, text="Date of birth (DD-MM-YYYY)")
		
		self.userEntry = Entry(self)
		self.passEntry = Entry(self, show="*")
		self.confpassEntry = Entry(self, show="*")
		self.dateEntry = Entry(self)
		
		self.userLB.grid(row=0, sticky=E)
		self.passLB.grid(row=1, sticky=E)
		self.confpassLB.grid(row=2, sticky=E)
		self.dateLB.grid(row=3, sticky=E)
		
		self.userEntry.grid(row=0, column=1)
		self.passEntry.grid(row=1, column=1)
		self.confpassEntry.grid(row=2, column=1)
		self.dateEntry.grid(row=3, column=1)
				
		self.logbtn = Button(self, text="Register", command = self._register_btn_clickked)
		self.logbtn.grid(columnspan = 2)
				
		self.pack()
	
	def _register_btn_clickked(self):
		if not DB.FreeLogin(self.userEntry.get()):
			tm.showerror("Login error", "Имя пользователя уже занято")
			return 
		
		if len(self.passEntry.get()) < 5:
			tm.showerror("Password error", "Длинна пароля должна быть не меньше 5 символов")
			return
		
		if self.passEntry.get() != self.confpassEntry.get():
			tm.showerror("Password error", "Не совпадают пароли")
			return
		
		if len(self.dateEntry.get()) != 10: 
			tm.showerror("Date error", "Неверная дата")
			return
		
		lines = self.dateEntry.get().split("-")
		if int(lines[0]) < 0 or int(lines[0]) > 31:
			tm.showerror("Date error", "Неверная дата")
			return
		if int(lines[1]) < 0 or int(lines[1]) > 12:
			tm.showerror("Date error", "Неверная дата")
			return
			
		DB.AddUser(self.userEntry.get(), self.passEntry.get(), self.dateEntry.get())		
		self.master.destroy()

def set_center(root):
	root.withdraw()
	root.update_idletasks()
	x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
	y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
	root.geometry("+%d+%d" % (x, y))
	root.deiconify()

def Run():
	root = Tk()
	root.title("Registration")
	lf = regFrame(root)
	set_center(root)
	root.mainloop()


