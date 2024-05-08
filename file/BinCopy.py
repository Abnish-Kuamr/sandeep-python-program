#copy binary file content into another binary file 
#BinCopy.py
bsfile=input("Enter Binary Source File:") 
try:
	with open(bsfile, "rb" ) as rp: 
		bdfile=input("Enter Binary Dest File:") 
		with open(bdfile,"w+b") as wp:
			sfdata=rp.read() 
			wp.write(sfdata)
			print("{} data copied into {}--plz verify".format(bsfile,bdfile))
except FileNotFoundError:
	print("Source File Does not exists:") 




