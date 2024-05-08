#kwdargsex1.py

def disp(stno,stname,stmarks,stcname):
  print("{}\t{}\t{}\t{}".format(stno,stname,stmarks,stcname))

#main program
print("============================================")
print("Number\tNmae\tMarks\tColl.Name")
print("============================================")
disp(stcname="OUCET",stno=10,stname="KVR",stmarks=66.66)  #function call-1
disp(stmarks=34.56,stcname="JNTU(H)",stno=11,stname="sharma") #function call-2
disp(12,"Bilal",stcname="HCU",stmarks=33.33)  #function call-3
#disp(stcname="JNTU(K)",stmarks=23.33, 13,"Sampath") #error
disp(13,stmarks=23.44,stcname="SKU",stname="Sampth") #function call-4
print("===============================================")

