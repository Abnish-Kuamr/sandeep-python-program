#rex7.py
import random 
lst=[10,20,30,40,50]
print("Original Elements={}".format(lst))
random.shuffle(lst)
print("----------------------------------")
print("shuffled Elements={}".format(lst))
strlist=["P","Y","T","H","O","N"]
print("Original String={}".format(strlist))
random.shuffle(strlist)
print("shuffled String={}".format(strlist))
lstcrs=["PYTHON","JAVA","DS","AI"]
print("Original Courses={}".format(lstcrs))
random.shuffle(lstcrs)
print("----------------------------------")
print("shuffled Courses={}".format(lstcrs))



