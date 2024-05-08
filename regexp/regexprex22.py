#regexprex22.py
#program for searching only 'b'

import re
matinfo=re.finditer("b","abaabaaab")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

