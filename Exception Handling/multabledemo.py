#multabledemo.py
from wipro import multable
from tcs import InValidNumberError
try:
	multable()
except InValidNumberError:
	print("DON'T ENTER -VE/ZERO NUMBER:")
except ValueError:
	print("\nDon't Enter Strs/alpha-numric values.Special Symbols:")
finally:
	print("i am from finally block")



