#mapex3.py
lst1=[10,12,13,14,15,16]
lst2=[1,2]

sumlist=list(map(lambda x,y: x+y, lst1,lst2))
print("List1 elements={}".format(lst1))
print("List2 elements={}".format(lst2))
print("Sum of  elements of lst1 and lst2={}".format(sumlist))

