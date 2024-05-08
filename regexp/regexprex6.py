#regexprex6.py
#search for all except small alphabets

import re
matinfo=re.finditer("[^a-z]","Ak#4v@R5$Vw%rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")
