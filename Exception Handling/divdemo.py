#divdemo.py
from mathop import division 
from hyd import KvrZeroError 
try:
	division()	# handling the exception 
except KvrZeroError :
	print("DON'T ENTER ZERO FOR DEN...")


