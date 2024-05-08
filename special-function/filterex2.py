#filterex2.py
#main program
lst=[100,-123,456,123,367,-789,-100,200]
pl=tuple(filter(lambda x: x>0,lst))      #pl=positive list
print("---------------------------------------")
print("Original List={}".format(lst))
print("Positive elements List={}".format(pl))
print("-----------------------------------------")
nl=list(filter(lambda a: a<0,lst))       #nl=negative list
print("Negative elements List={}".format(nl))
