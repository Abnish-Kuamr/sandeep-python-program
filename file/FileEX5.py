#FileEX5.py
try:
	with open("stud.data","r") as rp:
		print("File opened in read mode successfully:")
		print("---------------------------------------")
		print("File Opening Mode=",rp.mode)   #r
		print("is it readable?=",rp.readable())  #True
		print("is it writable?=",rp.writable()) #False
		print("Line-9-->is files closed?=",rp.closed)    #False
		print("---------------------------------------")
	print("i am out of with open()...Line--11-->is file closed?=",rp.closed) #True
except FileNotFoundError:
	print("Files does not exits:")
else:
	print("i am out of with open()...Line--15-->is file closed?=",rp.closed) #True
finally:
	print("i am out of with open()...Line--17-->is file closed?=",rp.closed) #True








