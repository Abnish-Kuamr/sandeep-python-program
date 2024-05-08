#regexprex24.py
#searching for either zero or one 'a' or more 'a' s

import re
matinfo=re.finditer("a*","abaabaaab")
print("----------------------------------------------------------")
for mat in matinfo:
	print("start Index: {}\t Value:{}".format(mat.start(),mat.group()))
else:
	print("-------------------------------------------------------")
