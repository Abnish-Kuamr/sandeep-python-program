#aopmain.py
from menu import menuop
from aop import *;
import sys 
while(True):
 menuop()
 ch=int(input("Enter Your Choice:"))

 if(ch==1):
	 addition()
 elif(ch==2):
	 substraction()
 elif(ch==3):
	 multiply()
 elif(ch==4):
	 division()
 elif(ch==5):
	 modulas()
 elif(ch==6):
	 expo()
 elif(ch==7):
	 print("Thanx for Using This Application!")
	 sys.exit()
 else:
	 print("Your Selection of Operation is Wrong:")

