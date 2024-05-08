#varlenparamex2.py
def findsumavg(sname,place,*n,crs="PYTHON"):
	print("=============================================")
	print("Name=",sname)
	print("Place=",place)
	print("Course=",crs)
	print("==============================================")
	s=0
	for val in n:
		print("\t{}".format(val))
		s=s+val
	else:
		print("\tSum={}".format(s))
		print("\tAverage={}".format(s/len(n)))
		print("============================================")

#main program
findsumavg("dilip","hyd",10,20)
#findsumavg(place="MH",sanme=Raj Singh",10,20,30)
findsumavg("prasad","AP",10,20,30,40)

