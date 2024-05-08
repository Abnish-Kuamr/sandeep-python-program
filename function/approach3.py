#approach3.py

#approach3----Logic
#------------------------------------------------
#Taking input:--- Function Call(outside)
#Processing:---Function Body(inside)
#Giving Output:---Function Body(inside)
#-------------------------------------------------

def addition(a,b):
	c=a+b
	print("sum of {} and {}={}".format(a,b,c))

#main program
x1=float(input("Enter First value:"))
x2=float(input("Enter Second value:"))
addition(x1,x2)