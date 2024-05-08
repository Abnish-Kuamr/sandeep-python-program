#globalsex2.py
a=10
b=20
c=30
d=40    #here 'a', 'b', 'c', and 'd' are called globals variables 
def operations():
	a=1
	b=2
	c=3
	d=4   #here 'a', 'b', 'c', and 'd' are called local variables 
	ga=globals()['a']
	gb=globals()['b']
	gc1=globals()['c']
	gd=globals()['d']
	localresult=a+b+c+d+ga+gb+gc1+gd
	print("result=",localresult)

#main program
operations()

