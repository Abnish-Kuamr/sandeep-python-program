#modifygv.py
a=10 #global variable
def modifyval():
	global a  #refering global variable value
	a=a+1     #modifying global variable value
	print("val of a in modifyval()={}".format(a))  #11
def updateval():
	global a  #refering global variable value
	a=a*2     #modifying global variable value
	print("val of a in updateval()={}".format(a))  #22

#main program
print("val of a befor modification by the function={}".format(a))  #10
modifyval()
print("val of a after modifyval()={}".format(a))   #11
updateval()
print("val of a after updateval()={}".format(a))   #22


