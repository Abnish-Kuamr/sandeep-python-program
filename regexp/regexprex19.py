#regexprex19.py
#Search for word character [A-Za-z0-9](exceptspecial symbols)

import re
matinfo=re.finditer("\w", " A#6aB^ 7@H Pa")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")

