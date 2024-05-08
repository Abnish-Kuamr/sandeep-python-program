#listfiles.py 
import os 
kvr=os.walk(".") 
print(kvr)
for k,v,r in kvr:
	print("Folder path={}".format(k)) 
	print("sub folder path={}".format(v)) 
	print("Files={}".format(r))

