#studentmarksreport.py
#validation of student number
while(True):
	sno=int(input("Enter Student Number(1-200):"))
	if((sno>=1) and (sno<=200)):
		break
#Accepting name 
sname=input("Enter Student Nmae:")
#validation marks in C
while(True):
	cm=int(input("Enter Marks in C:"))
	if((cm>=0) and (cm<=100)):
		break
#validation marks in CPP
while(True):
	cppm=int(input("Enter Marks in CPP:"))
	if((cppm>=0) and (cppm<=100)):
		break
#validation marks in python
while(True):
	pym=int(input("Enter Marks in PYTHON:"))
	if((pym>=0) and (pym<=100)):
		break
#calculate total and percentage of marks
totmarks=cm+cppm+pym
percentmarks=(totmarks/300)*100
#give grade
if((cm<40) or (cppm<40) or (pym<40)):
	grade="FAIL"
else:
	if((totmarks>=250) and (totmarks<=300)):
		grade="DISTINCTION"
	elif((totmarks>=200) and (totmarks<=249)):
		grade="FIRST"
	elif((totmarks>=150) and (totmarks<=199)):
		grade="SECOND"
	elif((totmarks>=120) and (totmarks<=149)):
		grade="THIRD"
#Display student marks reports
print("="*50)
print("\t\tStudent Progress Report")
print("="*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in CPP:{}".format(cppm))
print("\tStudent Marks in Python:{}".format(pym))
print("-"*50)
print("\tStudent Total Marks:{}".format(totmarks))
print("\tStudent Percentage of Marks:{}".format(percentmarks))
print("-"*50)
print("\tStudent Result:{}".format(grade))
print("="*50)
