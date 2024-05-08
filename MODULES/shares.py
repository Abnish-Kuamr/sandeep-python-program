#shares.py---->treated as module 
def sharesinfo():
	sh={"IT":200,"Pharma":400,"Prod":100}
	print("-----------------------------------")
	print("\tshare name\tshare value")
	print("------------------------------------")
	for sn,sv in sh.items():
		print("\t{}\t{}".format(sn,sv))
	print("-------------------------------------")



