#regexprex8.py
#search for all except capital alphabets

import re
matinfo=re.finditer("[^A-Z]","Ak#4v@R5$Vw%rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

