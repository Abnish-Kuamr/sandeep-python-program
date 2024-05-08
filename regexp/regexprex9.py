#regexprex9.py
#search for all digits only

import re
matinfo=re.finditer("[0-9]","Ak#4v@R5$Vw%8rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

