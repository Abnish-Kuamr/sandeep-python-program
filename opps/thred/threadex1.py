#threadex1.py
import threading
import time
def hello():
	for i in range(6):
		print("Child thread1 --> i am from hello()")
		time.sleep(1)
def hi(ms):
	for j in range(6):
		print(ms,"---i am hi()")
#main program
t1=threading.Thread(target=hello)  #t1 is called child thread 
t2=threading.Thread(target=hi ,args=("child thread2",))  #t2 is called child thread 
print("type of t1=",type(t1))
t1.start()
t2.start()
for i in range(6):
	print("main thread--> i am from disp()")
	time.sleep(1)



