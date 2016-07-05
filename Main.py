import Entry
import BioMenu

reg = Entry.AskIsRegistered()

if reg:
	user = Entry.AskLoginPass()			
else: 
	user = Entry.Register()

print("Welcome, %s\n" % user)

BioMenu.AskBiorhythms(user)
