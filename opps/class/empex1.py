#empex1.py
class Employee:

	@classmethod
	def appendcompname(cls):
		cls.compname="Wipro-HYD"
	def appendempvalues(self):
		print("id in method=",id(self))
		print("--------------------------------")
		self.empno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee salary:"))
		self.dsg=input("Enter Employee Designation:")
		print("----------------------------------")

	def dispempvalues(self):
		print("id in method=",id(self))
		print("-----------------------------------")
		print("Employee Number:{}".format(self.empno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Designation:{}".format(self.dsg))
		print("Employee salary:{}".format(self.sal))
		print("Employee comp name:{}".format(Employee.compname))
		print("--------------------------------------")

	@staticmethod
	def operation(a,b,ops):
		if(ops=="+"):
			print("{} {} {}={}".format(a,ops,b,a+b))
		elif(ops=="-"):
			print("{} {} {}={}".format(a,ops,b,a-b))
		elif(ops=="*"):
			print("{} {} {}={}".format(a,ops,b,a*b))
		elif(ops=="/"):
			print("{} {} {}={}".format(a,ops,b,a/b))
		elif(ops=="//"):
			print("{} {} {}={}".format(a,ops,b,a//b))
		elif(ops=="%"):
			print("{} {} {}={}".format(a,ops,b,a%b))
		elif(ops=="**"):
			print("{} {} {}={}".format(a,ops,b,a**b))
		else:
			print("You Don't know Arithmetic Operators ---plz learn")

#main program
Employee.appendcompname()
eo1=Employee()
#print("id of eo1 in main program",id(eo1))
#eo1.appendempvalues()
eo2=Employee()
#print("id of eo2 in main program",id(eo2))
#eo2.appendempvalues()
#print("==================================================")
#eo1.dispempvalues()
#eo2.dispempvalues()  
print("==================================================")
print("Utility Operation")
print("==================================================")
eo1.operation(10,20,"*")
eo2.operation(10,20,"**")














