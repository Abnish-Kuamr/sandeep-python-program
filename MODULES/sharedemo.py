#sharedemo.py
import shares
import time
import importlib

shares.sharesinfo()
print("Line-7-->hello viewers i am going to sleep for 20 secs")
time.sleep(20)
print("Line-9-->hello viewers i am coming out from  sleep after 20 secs")
importlib.reload(shares)
shares.sharesinfo()

