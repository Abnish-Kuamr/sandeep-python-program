#current.py
import threading
print("i am from python program")
t=threading.current_thread()
print("type of t=",type(t))    # <class, 'threading.Thread'>
print("Name of thread=",t.getName())
t.setName("KVR")
print("Name of thread=",t.getName())




