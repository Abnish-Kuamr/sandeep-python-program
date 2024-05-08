#rmdirex.py
import os 
try:
	os.rmdir("e:\TVR123") 
	print("Folder Removed-verify")
except FileNotFoundError:
	print("Folder Name does not Exists")
except OSError:
	print("Specified Folder Contains files-can't be removed")
 



