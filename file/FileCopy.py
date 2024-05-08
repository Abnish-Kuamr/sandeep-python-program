#FileCopy.py
sfile=input("Enter The source File:") 
try:
	with open(sfile) as rp:
		dfile=input("Enter Destination File:") 
		with open(dfile,"a") as wp:
			sfdata=rp.read() 
			wp.write(sfdata)
			print("{} data copied into {}--plz verify ".format(sfile,dfile))
except FileNotFoundError:
	print("Source File does not exists")



