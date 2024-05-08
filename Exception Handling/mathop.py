#mathop.py-----treated as a module name
from hyd import KvrZeroError 
def	division():
	a=int(input("Enter Value of a:")) 
	b=int(input("Enter Value of b:")) 
	if (b==0):
		raise KvrZeroError # hitting / raising an exception by using raise kwd
	else:
		c=a/b 
		print("div={}".format(c))

