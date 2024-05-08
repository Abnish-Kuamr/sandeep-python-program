#kwvarlenparamex1.py
def findtotalmarks(sname,scls,**marks):
	tot=0
	print("------------------------------------------")
	print("\tStudent Name={}".format(sname))
	print("\tStudent Class={}".format(scls))
	print("------------------------------------------")
	for k,v in marks.items():
		print("\t{}\t{}".format(k,v))
		tot=tot+v
	print("-------------------------------------------")
	print("\tTotal Marks={}".format(tot))
	print("\n------------------------------------------")

#main program
findtotalmarks("Harshita","X",Eng=50,Hindi=60,Sco=70,Sci=80,maths=90)
findtotalmarks("Rajeshwari","XII",Bio=55,zoo=60,che=58)
findtotalmarks("Akhila","B.Tech",C=70,CPP=74,Python=80,java=79)
findtotalmarks("Rossum","Research")
