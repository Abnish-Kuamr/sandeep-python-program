#reduceex2.py
import functools
print("Enter List of Value separated by comma:")
lst=[int (x) for x in input().split(",")]

listsum=functools.reduce(lambda x,y:x+y, lst)
print("Orginal elements of list={}".format(lst))
print("Sum of elements={}".format(listsum))

