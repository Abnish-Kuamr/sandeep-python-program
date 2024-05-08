#multable.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid number:".format(n))
else:
	print("-"*40)
	print("\tMul Table for :{}".format(n)) 
	print("-"*40)
	i=1
	while(i<=10):
		print("\t{} X {}={}".format(n,i,n*i))
		i=i+1
	else:
		print("-"*40)












