#lstsum.py
lst=[10,20,30,12.34,-12,45,-5.34]
s=0
i=0
print("-"*50)
print("Elements of List:")
print("-"*50)
while(i<len(lst)):
	print("\t{}".format(lst[i]))
	s=s+lst[i]
	i=i+1
else:
	print("-"*50)
	print("\tsum={}".format(s))
	print("-"*50)




