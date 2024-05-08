#unpick.py 
import pickle 
try:
	with open("emp.data","rb") as rp:
		print("--------------------------------------------")
		print("\tEmplyee Records")
		print("--------------------------------------------")
		while(True):
			try:
				emprec=pickle.load(rp) 
				for val in emprec:
					print("{}".format(val), end=" ")
				print()
			except EOFError:
				print("----------------------------------------")
				break
except FileNotFoundError:
	print("File does not exists")












