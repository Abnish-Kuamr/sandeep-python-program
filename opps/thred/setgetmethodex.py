#setgetmethodex.py
import threading,time
def show():
	print("i am from in  show started execution...")
	ct=threading.current_thread()
	print("Name of child thread=",ct.getName())  #thread-1
	#change the Name of child thread as student
	ct.setName("student")    #ct.name="student"
	print("Name of child thread after changing=",ct.getName())

#main program
t1=threading.Thread(target=show)
t1.start()
mt=threading.current_thread()
print("Name of main thread before changing=",mt.getName())
#change the Name of main thread as KVR
mt.setName("KVR")  #mt.name="KVR"
print("Name of main thread after changing=",mt.getName())




