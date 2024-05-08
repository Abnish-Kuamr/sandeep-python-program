#filterex1.py

def positive(x):
	if (x>0):
		return True
	else:
		return False

def negative(a):
	if (a<0):
		return True
	else:
		return False

#main program
lst=[10,-20,20,-30,0,-40,50,60,-15,-34,23]
pl=tuple(filter(positive,lst))      #pl=positive list
print("---------------------------------------")
print("Original List={}".format(lst))
print("Positive elements List={}".format(pl))
print("-----------------------------------------")
nl=list(filter(negative,lst))       #nl=negative list
print("Negative elements List={}".format(nl))

