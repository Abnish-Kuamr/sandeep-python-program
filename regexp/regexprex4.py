#regexprex4.py
#program for seraching the word "python"
# in the line "Python is an OOP Lang. Python is an POP lang also" 

import re
matinfo=re.finditer("[^kvr]","Ak#4v@R5$Vw%rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")


