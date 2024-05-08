#regexprex20.py
#Search for special symbols except word character [^A-Za- z0-9]

import re
matinfo=re.finditer("\W", " A#6aB^ 7@H Pa")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")


