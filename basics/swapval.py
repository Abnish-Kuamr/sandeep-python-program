#swapval.py
x=int(input("Enter the val of x:"))
y=int(input("Enter the val of y:"))
print("-"*50)
print("Original val of x={}".format(x))
print("Original val of y={}".format(y))
print("-"*50)
#swapping Logic by using XOR operator
x=x^y
y=x^y
x=x^y
print("Swapped val of x={}".format(x))
print("Swapped val of y={}".format(y))
print("-"*50)
