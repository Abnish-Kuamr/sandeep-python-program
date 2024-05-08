#reduceex3.py
from functools import reduce
n=int(input("Enter value of n:"))
if(n<=0):
	print("{} is invalid".format(n))
else:
	res1=reduce(lambda a,b: a*b , range(1,n+1))
	print("------------------------------------------")
	print("product of First {} natural Numbers:".format(n))
	print("-------------------------------------------")
	for i in range(1,n+1):
		print("\t{}".format(i))
	else:
		print("-------------------------")
		print("Product:{}".format(res1))
		print("-------------------------")







