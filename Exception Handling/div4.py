#program cal division of two numbers by accepting the values dynamically from KBD
#div4.py
try:
	s1=input("Enter First Value:") 
	s2=input("Enter Second Value:")
	a=int(s1) 
	b=int(s2) 
	c=a/b 
except:
	print("\n exception occured")
else:
	print("==============================")
	print("\tResult")
	print("===============================")
	print("Val of a={}".format(a))
	print("Val of b={}".format(b))
	print("Div={}".format(c))
	print("===============================")
finally:
	print("i am from finally block:")


