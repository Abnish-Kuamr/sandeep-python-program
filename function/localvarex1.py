#localvarex1.py
def faculty1():
	fname1="KVR" #local variable
	print("Faculty Name--Faculty1()={}".format(fname1))
	#print("Faculty Name--Faculty2()={}".format(fname2))---error--fname2 can't access 
                                                          #bcz it is local to faculty2() 
def faculty2():
    fname2="Sampath" #local variable
    print("Faculty Name--Faculty2()={}".format(fname2))
    #print("Faculty Name--Faculty1()={}".format(fname1))---error--fname1 can't access 
                                                           #bcz it is local to faculty1() 

#main program
faculty1()
faculty2()

