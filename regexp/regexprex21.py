#regexprex21.py
#search for all 

import re
matinfo=re.finditer(".", " A#6aB^ 7@H Pa")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

