#mapex1.py
def square(x):
	return(x**2)

#main progarm
print("Enter Integer Value dynamically separated by space:")
oldlst=[int(x) for x in input().split()]    #oldlst=old list
sqlst=list(map(square,oldlst))               #sqlst= Square list
print("-"*40)
print("Orginal List={}".format(oldlst))
print("Square List={}".format(sqlst))

