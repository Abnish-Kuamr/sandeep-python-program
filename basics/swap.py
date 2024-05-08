#swap.py
a=input("Enter first value: ")
b=input("Enter second value: ")
print("-"*50)
print("original val of a={}".format(a))
print("original val of b={}".format(b))
print("-"*50)
a,b = b,a  #multi Line Assignment
print("swappwd val of a={}".format(a))
print("swappwd val of b={}".format(b))
print("-"*50)
