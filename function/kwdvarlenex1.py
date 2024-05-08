#kwdvarlenex1.py
def show(**n):    #here n is called keyword variable length parameter and whose type is dict
	print("================================================")
	print("Key\tValue")
	print("================================================")
	for k,v in n.items():
		print("{}\t{}".format(k,v))
	print("=================================================")

#main program
#n-similar function calls with variable Key word params
show(sno=10,sname="Arindam")
show(sname="Rossum",hobby="Research",place="NL")
show(fno=1,fname="KVR",sub1="PYTHON",sub2="JAVA",sub3="Django")

