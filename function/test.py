#test.py
#Program for displying the content of any iterabel object

def disp(a):
	print("-----------------------")
	print("\tElememts:")
	print("------------------------")
	for val in a:
		print("\t{}".format(val))
	print("------------------------")

def show(x):
	print("----------------------------")
	print("\tKeys\tValues")
	print("----------------------------")
	for k,v in x.items():
		print("\t{}\t{}".format(k,v))
	print("--------------------------")

#main program
lst=[10,"Rossum","Pythom",12.34,2+3j,True]
disp(lst)
tpl=(11,"KVR","HYD",23.45)
disp(tpl)
s1={10,"Ritche",23.45}
disp(s1)
d={1:"PYTHON",2:"AI",3:"DS",4:"JAVA"}
show(d)
