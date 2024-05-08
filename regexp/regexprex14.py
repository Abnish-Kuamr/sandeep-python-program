#regexprex14.py
#search for only special symbols

import re
matinfo=re.finditer("[^A-Za-z0-9]","Ak#4v@R5$Vw%8rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

