from Opcode import *

def pass1():
	locptr = 0
	f1 = open("SymbolTable.txt","a")
	arr = list()
	
	with open("input.txt","r") as f:
		for x in f:
			x = x.strip("\n")
			arr = x.split(' ')
			
			if(len(arr)>1 and ifLabel(arr[0]) and ifOpcode(arr[1])):
				f1.write(arr[0]+" "+str(locptr)+"\n")
				

			elif(len(arr)>1 and ifOpcode(arr[0]) and arr[0] == "INP"):
				f1.write(arr[1]+" "+str(locptr)+"\n")
				

			elif(ifOpcode(arr[0]) and arr[0] == "STP"):
				break

			locptr += 1

	f1.close()

	


	




