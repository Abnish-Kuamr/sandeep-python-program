#wipro.py------->treated as a module
from tcs import InValidNumberError
def multable():
	n=int(input("Enter a Number:"))
	if(n<=0):
		raise InValidNumberError  #hitting or raising the exception 
	else:
		print("------------------------------")
		print("Mul Table for:{}".format(n))
		print("------------------------------")
		for i in range(1,11):
			print("\t{}x{}={}".format(n,i,n*i))
		print("------------------------------")
