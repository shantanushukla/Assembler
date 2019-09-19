symbolTable = dict()

def ifLabel(a):
	a = a.split(" ")
	if ifOpcode(a[0]):
		return False
	else:
		return True

def add_toSymbTable(locCounter, label):
	if(ifLabel(label)):
		symbolTable.__setitem__(label,locCounter)
		
	