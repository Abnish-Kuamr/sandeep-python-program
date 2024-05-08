#innerloopex1.py
nom=int(input("Enter how many multipliction tables you want:"))
if(nom<=0):
	print("{} invalid input".format(nom))
else:
	for n in range(1,nom+1):
		print("----------------------------")
		print("\tMul table for :{}".format(n))
		print("-----------------------------")
		for i in range(1,11):
			print("\t{} X {}={}".format(n,i,n*i))
		else:
			print("--------------------------")
	else:
		print("ALL MUL TABLES OVER")
