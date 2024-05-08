#big.py
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
#logic for finding big
if (a==b) and (b==c) and (c==a):
   print("ALL VALUES ARE EQUAL:")
else:
	big=a
	if(b>big):
		big=b
	if(c>big):
		big=c
	print("big({},{},{})={}".format(a,b,c,big)) 




  