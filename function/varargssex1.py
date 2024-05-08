#varargssex1.py
def show( *n): #here *n is called variable parameter name whose type is tuple
   for val in n:
      print("{}".format(val), end=" ")  # 10  20
   print("\n")

def disp( *h): #here *h is called variable parameter name whose type is tuple
   for val in h:
      print("{}".format(val), end=" ")  # 10  20
   print("\n")

#main program
#n-similar function calls with variable number of values
show(10)
show(10,20,30)
show(10,20,30,40)
show("KVR","PYTHON","HYD")
show()

#n-similar function calls with variable number of values
print("------------------------------------------")
disp(10,"java")
disp("jave","python","DS")
disp(10,12.34,34.56,4)
disp(2+3j,True,False,None)
