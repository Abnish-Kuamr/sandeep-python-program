#rmdirsex.py
import os
try:
	os.removedirs("e:\mango/apple") 
	print("Folder(s) removed--verify") 
except FileNotFoundError:
	print("specifed folder hierarchy does not exists") 
except OSError:
	print("Specified Folder is not empty:")


