#defparmex1.py
def dispstudinfo(sno,sname,smarks,crs1="PYTHON",crs2="DS"):
  print("\t{}\t{}\t\t{}\t{}\t{}".format(sno,sname,smarks,crs1,crs2))

#main program
print("====================================================================")
print("\tNumber\tStudentNmae\tMarks\tCourse")
print("====================================================================")
dispstudinfo(10,"dprasad",56.78)
dispstudinfo(20,"Naveen",66.78)
dispstudinfo(30,"yshwant",66.78)
dispstudinfo(40,"vishnu",76.78)
dispstudinfo(50,"krish",78.99,"JAVA")
dispstudinfo(60,"MALLESH",68.99)
dispstudinfo(70,"ANIL",68.99,crs2="JAVA")
dispstudinfo(80,"ANIL",68.99,crs2="R",crs1="ML")
dispstudinfo(sname="sumeet",sno=90,crs1="R",crs2="SPRING",smarks=45.67)
#dispstudinfo(sname="Karthik",sno=75,45.76)===>error
dispstudinfo(75,"Karthik",smarks=34.56)
print("=====================================================================")

