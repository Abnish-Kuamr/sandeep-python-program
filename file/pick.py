#pick.py 
import pickle
with open ("emp.data","ab") as wp:
	noe=int(input("Enter How Many Emplyees data u have:")) 
	for i in range(1, noe+1):
		print("--------------------------------------------")
		print("Enter {} Employee Data:".format(i)) 
		print("--------------------------------------------") 
		eno=int(input("Enter Employee Number:")) 
		ename=input("Enter Employee Name:")
		esal=float(input("Enter Employee Salary:")) 
		lst=list()
		lst.append(eno) 
		lst.append(ename) 
		lst.append(esal) 
		pickle.dump(lst,wp) 
		print("--------------------------------------------")
		print("{} Emp Data Record Saved in a file successfully:".format(i))
		print("--------------------------------------------")







