#aop.py
def readvalues(op):
	print("Enter Two value for {}:".format(op))
	a=float(input())
	b=float(input())
	return a,b

def addition():
	a,b=readvalues("addition")
	print("Sum of {} and {}={}".format(a,b,a+b))

def substraction():
	k,v=readvalues("substract")
	print("Sub of {} and {}={}".format(k,v,k-v))

def multiply():
	k,v=readvalues("multiplication")
	print("mul of {} and {}={}".format(k,v,k*v))

def division():
	k,v=readvalues("division")
	print("Div of {} and {}={}".format(k,v,k/v))

def modulas():
	x,y=readvalues("modulo division")
	print("Modulus of {} and {}={}".format(x,y,x%y))

def expo():
	k,v=readvalues("exponentation")
	print("{} to the power of {}={}".format(k,v,k**v))








