#regexprex17.py
#Search for digit only

import re
matinfo=re.finditer("\d", " A#6aB^ 7@H Pa")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

