#approach1.py

#approach1----Logic
#------------------------------------------------
#Taking input:--- Function call(outside)
#Processing:---Function Body(inside)
#Giving Output:---Function Call(outside-return)
#-------------------------------------------------

def addition(a,b): #here 'a' and 'b' are called formal params
	c=a+b          #here 'c' is called Local variable
	return c

#main program
x1=int(input("Enter First value:"))
x2=int(input("Enter second value:"))
res1=addition(x1,x2)   #Function call
print("{} + {}={}".format(x1,x2,res1))


