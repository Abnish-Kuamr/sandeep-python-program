#regexprex16.py
#Search for all except space character

import re
matinfo=re.finditer("\S", " A#6aB^ 7@H Pa")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

