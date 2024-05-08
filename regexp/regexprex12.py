#regexprex12.py
#search for all except capital and small alphabets only

import re
matinfo=re.finditer("[^A-Za-z]","Ak#4v@R5$Vw%8rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

