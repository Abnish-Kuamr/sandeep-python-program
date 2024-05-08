#emp1.py
class Employee:
	def __init__(self):
		print("---------------------------------------")
		self.eno=int(input("Enter Emp Number:")) 
		self.ename=input("Enter Emp Name:") 
		self.dsg=input("Enter Emp Designation:")
		print("---------------------------------------")
			
	def dispempvalues(self):
		print("---------------------------------------")
		print("Emp Number:{}".format(self.eno)) 
		print("Emp Name:{}".format(self.ename))
		print("Emp Designation:{}".format(self.dsg))
		print("---------------------------------------")

#main program
eo1=Employee()
eo2=Employee()
eo3=Employee()


