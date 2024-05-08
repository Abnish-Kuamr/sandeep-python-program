#approach4.py

#approach4----Logic
#------------------------------------------------
#Taking input:--- Function Call(inside)
#Processing:---Function Body(inside)
#Giving Output:---Function Body(outside)
#-------------------------------------------------
def addition():
	a=float(input("Enter First value:"))
	b=float(input("Enter Second value:"))
	c=a+b
	return a,b,c

#main program
a,b,c=addition()
print("sum of {} and {}={}".format(a,b,c))
print("-------------------------------------")
x=addition() #valid, here variable 'x' is holding all values,
             #which are comming from function Definition and whose type tuple
print("sum of {} and {}={}".format(x[0],x[1],[2]))



