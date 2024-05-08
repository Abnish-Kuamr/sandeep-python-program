#innerloopex3.py
nom=int(input("Enter how many multipliction tables you want:"))
if(nom<=0):
	print("{} invalid input".format(nom))
else:
	lst=list()
	for i in range(1,nom+1):
		print("Enter a number for which you want mul table:")
		v=int(input())
		lst.append(v)
	else:
		print("-----------------------------------")
		print("List values:",lst)
	for n in lst:
		print("------------------------------------")
		print("\tMul table for :{}".format(n))
		print("-----------------------------")
		for i in range(1,11):
			print("\t{} X {}={}".format(n,i,n*i))
		else:
			print("--------------------------")
	else:
		print("ALL MUL TABLES OVER")
