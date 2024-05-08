#pat1.py
n=int(input("How many star lines you want:"))
if(n<=0):
	print("{} invalid input".format(n))
else:
	for i in range(0,n):
		for j in range(0,i+1):
			print("*",end="")
		print()


