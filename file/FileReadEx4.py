#FileReadEx4.py 
rp=open("hyd.data","r") 
fdata=rp.readlines() 
print(fdata)
for line in fdata:
	print(line, end=" ")


