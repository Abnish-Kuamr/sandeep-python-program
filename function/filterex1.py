#filterex1.py

def positive(x):
	if (x>0):
		return True
	else:
		return False

#main program
lst=[10,-20,20,-30,-40,50,60,-15,-34,23]
obj=filter(positive,lst)
print("type of obj=",type(obj))