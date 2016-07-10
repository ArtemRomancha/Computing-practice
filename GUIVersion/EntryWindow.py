from tkinter import *
import tkinter.messagebox as tm
import DBAccess as DB
import RegistrationWindow as reg
import BiorhythmsWindow as bio

class LoginFrame(Frame):
	def __init__(self, master):
		super().__init__(master)
		
		self.userLB = Label(self, text="Username")
		self.passLB = Label(self, text="Password")
		
		self.userEntry = Entry(self)
		self.passEntry = Entry(self, show="*")
		
		self.userLB.grid(row=0, sticky=E)
		self.passLB.grid(row=1, sticky=E)
		
		self.userEntry.grid(row=0, column=1)
		self.passEntry.grid(row=1, column=1)
				
		self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
		self.logbtn.grid(columnspan = 2)
		
		self.regbtn = Button(self, text="Registration", command = self._reg_btn_clickked)
		self.regbtn.grid(columnspan = 2)
		
		self.pack()
	def _reg_btn_clickked(self):
		reg.Run()

	def _login_btn_clickked(self):
		username = self.userEntry.get()
		password = self.passEntry.get()

		if DB.Control(username, password):
			tm.showinfo("Login success", "Welcome, %s" % username)
			self.master.destroy()
			bio.Run(DB.GetDateOfBirth(username))
		else:
			tm.showerror("Login error", "Incorrect username or password")					

def set_center(root):
	root.withdraw()
	root.update_idletasks()
	x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
	y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
	root.geometry("+%d+%d" % (x, y))
	root.deiconify()

def Run():
	root = Tk()
	root.title("Login")
	lf = LoginFrame(root)
	set_center(root)
	root.mainloop()
