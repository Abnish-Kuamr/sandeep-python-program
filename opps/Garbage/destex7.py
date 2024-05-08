#destex7.py 

import time,sys
class Sample:
	def __init__(self):
		print("Object Initliztion---Constructor:")

	def __del__(self):
		print("Memory Space pointed by object removed--Garbage Collector")

#main program 
s1=Sample()
s2=s1
s3=s1
print("Refs os s1=",sys.getrefcount(s1))
print("end of application")



