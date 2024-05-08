#FileEx2.py
wp=open("stud.data","w")
print("File Opened in write mode successfully:")
print("Type of wp=",type(wp))   #TextIOWrapper
print("---------------------------------------")
print("File Opening Mode=",wp.mode)   #w
print("is it readable?=",wp.readable())  #False
print("is it writable?=",wp.writable()) #True 
print("---------------------------------------")


