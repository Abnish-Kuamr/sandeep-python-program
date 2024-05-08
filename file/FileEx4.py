#FileEx4.py
try:
	wp=open("atten.data","x")
	print("File Opened in write mode successfully:")
	print("Type of wp=",type(wp))   #TextIOWrapper
	print("---------------------------------------")
	print("File Opening Mode=",wp.mode)   #x
	print("is it readable?=",wp.readable())  #False
	print("is it writable?=",wp.writable()) #True 
	print("---------------------------------------")
except FileExistsError:
	print("File Already Opened in write mode, we can't open again")



