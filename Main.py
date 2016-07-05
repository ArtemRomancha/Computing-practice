import Entry

reg = Entry.AskIsRegistered()

if reg:
	user = Entry.AskLoginPass()			
else: 
	user = Entry.Register()

print("Welcome, %s" % user)
