#createfoldex1.py
import os
try:
	os.mkdir("e:\Mango\apple\kiwi")
	print("Folder created--Verify")
except FileExistsError:
	print("Folder was already created-it can't create again") 
except OSError:
	print("The Hierarchy of Folders unable create:")

