#simpleint.py
p=float(input("Enter Principe amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of interest:"))
#cal si and amtpay
si=(p*t*r)/100
amtpay=p+si
#display the Result
print("-"*50)
print("Result")
print("-"*50)
print("Principle Amount:",p)
print("Time:",t)
print("interest:",r)
print("-"*50)
print("simple interest in amount:",si)
print("Total amount to pay=",amtpay)
print("-"*50)

