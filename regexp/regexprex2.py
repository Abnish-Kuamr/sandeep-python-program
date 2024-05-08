#regexprex2.py
#program for seraching the word "python"
# in the line "Python is an OOP Lang. Python is an POP lang also" 

import re
noc=0                 #No. of Occurences
matinfo=re.finditer("a","Python is an OOP Lang. python is an POP lang also")
print("----------------------------------------------------------")
for mat in matinfo:
	noc+=1
	print("start Index: {}\t End Index: {}\t Value:{}".format(mat.start(),mat.end(),mat.group()))
else:
	print("-------------------------------------------------------")
	print("No. of Occurences={}".format(noc))
	print("-------------------------------------------------------")

	



