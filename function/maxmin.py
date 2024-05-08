#maxmin.py
def findmaxmin(lst):
	maxelement=max(lst)
	minelement=min(lst)
	return maxelement, minelement

def dispresult(xl,he,se):
	print("----------------------------")
	print("Elements of List:")
	print("-----------------------------")
	for v in xl:
		print("\t{}".format(v))
	print("------------------------------")
	print("Max Element={}".format(he))
	print("Min Element={}".format(se))

#main program 
lst=[10,20,30,4,-5,0.56,23,234,-45]
maxe,mine=findmaxmin(lst)
dispresult(lst,maxe,mine)

	



