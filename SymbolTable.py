
symTbl = dict()

def addSym(tlc,var):
	symTbl[var] = tlc

def addSym(var):
	symTbl[var] = None

def writeTbl():
	f1 = open("SymbolTable.txt","a")
	bool a = False

	for key, value in symTbl.iteritems():
    	if value is None:
    		a = True
    		print("Error")
    		return 

    if(not a):
	    for key, value in symTbl.iteritems():
	    	f1.write(key+" "+value+"\n")  	