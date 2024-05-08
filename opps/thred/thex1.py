#thex1.py
import threading
print("Name of the Thread present in this program=",threading.current_thread().getName())  #main Thread 
print("Enter a Number:")
a=int(input())
res=a*a
print("square({})={}".format(a,res))





