#createfoldersEX1.py
import os
try:
	os.makedirs("e:\mango/apple/grapes") 
	print("Folder Hierarchy Created..")
except FileExistsError:
	print("Folder Hirrachy was already created:")

