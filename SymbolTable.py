from pass1 import *

symTbl = dict()

def addSym(tlc,var):
	if ifLabel(var):
		var = var[0:-1]
	if var not in symTbl:
		symTbl[var] = None
		return False

	if not symTbl[var] == None:
		if var in labels:
			print("Error: Label declared twice"+"( at: "+str(tlc)+")")
		else:
			print("Error: Symbol declared twice"+"( at: "+str(tlc)+")")
		return True
	else:
		symTbl[var] = tlc
		return False

def addSym1(var):
	if ifLabel(var):
		var = var[0:-1]
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