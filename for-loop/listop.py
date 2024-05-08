#listop.py
n=int(input("Enter how many number of elements:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	lst=list()  #create empty
	print("Enter {} values:".format(n))
	for v in range(1,n+1):
		val=float(input())
		lst.append(val)
	#logic for sum and  average
	s=0
	print("-"*50)
	print("Element of List:")
	print("-"*50)
	for val in lst:
		print("\t{}".format(val))
		s=s+val
	else:
		print("-"*50)
		print("sum={}".format(s))
		print("Average={}".format(s/len(lst)))
		print("-"*50)

