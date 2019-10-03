symTbl = dict()

def addSym(tlc,var):
	if var not in symTbl:
		symTbl[var] = None

	if not symTbl[var] == None:
		print("Error: Symbol/Label declared twice")
		return True
	else:
		symTbl[var] = tlc

def addSym1(var):
	if var not in symTbl:
		symTbl[var] = None

def writeTbl():
	f1 = open("Symboltable.txt","w")
	a = False

	for key,value in symTbl.items():
		if value is None:
			a = True
			print("Error: Used symbol/Label not defined") 
			return True

	if(not a):
	    for key,value in symTbl.items():
	    	f1.write(key+" "+str(value)+"\n")  

	f1.close()	
	return