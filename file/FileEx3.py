#FileEx3.py
wp=open("emp.data","r+")
print("File Opened in write mode successfully:")
print("Type of wp=",type(wp))   #TextIOWrapper
print("---------------------------------------")
print("File Opening Mode=",wp.mode)   #r+
print("is it readable?=",wp.readable())  #True
print("is it writable?=",wp.writable()) #True 
print("---------------------------------------")

