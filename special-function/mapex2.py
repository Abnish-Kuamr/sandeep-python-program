#mapex2.py

print("Enter Integer Value dynamically separated by space:")
oldlst=[int(x) for x in input().split()]      #oldlst=old list
sqlst=list(map(lambda x: x**2, oldlst))       #sqlst= Square list
print("-"*40)
print("Orginal List={}".format(oldlst))
print("Square List={}".format(sqlst))

