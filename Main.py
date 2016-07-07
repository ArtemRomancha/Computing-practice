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
recover = BioMenu.AskIsRecoverResults(userData[0])

if recover:
	res = BioMenu.AskRecoverVersion(userData[0])
	BioMenu.RecoverVersion(res)
else:
	BioMenu.AskBiorhythms(userData) #
