#filterex3.py
print("Enter List of elements Dynamcally:")
lst=[int(x) for x in input().split()]
#define filters for even and odd

el=list(filter(lambda x: x%2==0, lst))     #Even List
ol=tuple(filter(lambda a: a%2!=0, lst))    #Odd List
print("----------------------------------------------")
print("Original List of Elements={}".format(lst))
print("\nEven List of Elements={}".format(el))
print("\nOdd List of Elements={}".format(ol))

