symTbl = dict()

def addSym(tlc,var):
	if var not in symTbl:
		symTbl[var] = None

	if not symTbl[var] == None:
		print("Error: Sysmbol declared twice")
	else:
		symTbl[var] = tlc

def addSym1(var):
	if var not in symTbl:
		symTbl[var] = None

def writeTbl():
	f1 = open("Symboltable.txt","a")
	a = False

	for key,value in symTbl.items():
		if value is None:
			a = True
			print("Error: Used symbol not defined") 

	if(not a):
	    for key,value in symTbl.items():
	    	f1.write(key+" "+str(value)+"\n")  

	f1.close()	
	return