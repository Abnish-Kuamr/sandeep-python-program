#joinex.py
import threading,time
def emp():
	print("Employee started working...")
	time.sleep(10)
	print("Employee stopped working...")

#main program
print("office opend by main thread")
t1=threading.Thread(target=emp)
t1.start()
t1.join()
print("office closed")

