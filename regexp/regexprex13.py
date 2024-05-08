#regexprex13.py
#search for capital and small alphabets and digits only(except special synmbols)

import re
matinfo=re.finditer("[A-Za-z0-9]","Ak#4v@R5$Vw%8rP")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

