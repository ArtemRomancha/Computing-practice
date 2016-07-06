import Entry
import BioMenu
import DBAccess

reg = Entry.AskIsRegistered() #

if reg:
	user = Entry.AskLoginPass() #			
else: 
	user = Entry.Register() #

print("Welcome, %s\n" % user) #

userData = DBAccess.GetDateOfBirth(user) #
recover = BioMenu.AskIsRecoverResults(userData)

if recover:
	print("Recover data")
else:
	BioMenu.AskBiorhythms(userData) #
