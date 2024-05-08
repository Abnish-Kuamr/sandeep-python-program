#FileReadEx2.py
rp=open("hyd.data","r") 
fdata=rp.read(3) 
print(fdata)
print
print("--------------------")
print("Pos of rp=",rp.tell())
fdata=rp.read(6) 
print(fdata)
print("Pos of rp=",rp.tell())
rp.seek(0)
print("after seek, Pos of rp=",rp.tell())


