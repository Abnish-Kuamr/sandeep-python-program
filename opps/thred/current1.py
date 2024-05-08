#current1.py
import threading,time
def show():
	print("i am from show started execution...")
	print("Name of child thread=",threading.current_thread().getName())
	time.sleep(10)
	print("i am from show ended execution...")

t1=threading.Thread(target=show)
t1.start()
print("i am from python main program")
print("Name of main thread=",threading.current_thread().getName())
print("no. of active threads=",threading.active_count())
t1.join()
print("no. of active threads=",threading.active_count())

