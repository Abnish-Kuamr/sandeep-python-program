#Ascending and Descending orders
n=int(input("Enter How many value you Entered:"))
if(n<=0):
	print("You are entered Invalid input of {}".format(n))
else:
	list=[]
	for i in range(0,n):
		m=float(input())
		list.append(m)
		print("Given list elements:\n{}".format(list))
		print("-"*40)
		list.sort()
		print("list elements in Ascending orders:\n{}".format(list))
		print("-"*40)
		list.reverse()
		print("list elements in Descending orders:\n{}".format(list))

		