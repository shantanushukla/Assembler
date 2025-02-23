dec = {

	"CLA":"0000",
	"STP":"1100"
}

instr = {
    
    "LAC":"0001",
    "SAC":"0010",
    "ADD":"0011",
    "SUB":"0100",
    "BRZ":"0101",
    "BRN":"0110",
    "BRP":"0111",
    "INP":"1000",
    "DSP":"1001",
    "MUL":"1010",
    "DIV":"1011"
    
}

def ifOpcode(a):
    if ((a in dec) or (a in instr)):
        return True
    else:
        return False

def ifVariable(a):
	if ifOpcode(a):
		return False
	else:
		return True

def ifLabel(a):
    if ifOpcode(a):
        return False
    elif (a[-1] == ":"):
        return True

def getOpcode(a):
	if a in dec:
		return dec[a]
	elif a in instr:
		return instr[a]

def check(s):
	if s in dec:
		return True

	else:
		return False