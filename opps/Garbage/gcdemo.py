#gcdemo.py
import gc
print("By default Garbage Collector Program is running ..") 
#gc module----- isenabled()--->True(running)	Flase (not running)
print("is Garbage Colletcor Running by default=",gc.isenabled())   #True
#gc module----- disable()--->Garbage Collector program stops running
gc.disable()
print("is Garbage Colletcor Running afer disable()=",gc.isenabled()) # False
#gc module----- enable()--->Garbage Collector program starts running
gc.enable()
print("is Garbage Colletcor Running afer enable()=",gc.isenabled()) # True


