#posparamex1.py
def disp(stno,stname,stmarks,stcname):   #function definition--stno,stname,stmarks,stcname are called
                                          # formal parameters
  print("=======================================")
  print("Student Number={}".format(stno))
  print("Student Name={}".format(stname))
  print("Student Marks={}".format(stmarks))
  print("Student College Name={}".format(stcname))
  print("========================================")

#main program
sno=10
sname="KVR"
smarks=45.77
cname="OUCET"
disp(sno,sname,smarks,cname)  #function call--sno,sname,smarks,cname are called arguments




                                         