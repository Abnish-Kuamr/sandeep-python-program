#lambdaex2.py
bigop=lambda a,b:a if (a>b) else b

#main program
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
print("big({},{})={}".format(x,y,bigop(x,y)))

