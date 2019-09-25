from Opcode import *
from SymbolTable import *

def pass1():
	locptr = 0
	arr = list()
	
	with open("input.txt","r") as f:
		for x in f:
			x = x.strip("\n")
			arr = x.split(' ')

			if len(arr) == 1 and ifOpcode(arr[0]):
				if check(arr[0]):
					if arr[0] == "STP":
						return 0
				else:
					print("Error: Arguments Missing for the given Opcode\n")

			elif len(arr) >= 2 and ifOpcode(arr[0]):
				if len(arr) > 2:
					print("Error: Too many arguments")

				elif ifLabel(arr[1]):
					addSym(arr[1])

				else:
					print("Error: Argument cannot be Opcode")

			elif len(arr) >= 2 and ifLabel(arr[0]):
				#incomplete


			else:
				print("Error: Line must have an Opcode as instruction\n")
			
			# if(len(arr)>1 and ifLabel(arr[0]) and ifOpcode(arr[1])):
			# 	f1.write(arr[0]+" "+str(locptr)+"\n")
				

			# elif(len(arr)>1 and ifOpcode(arr[0]) and arr[0] == "INP"):
			# 	f1.write(arr[1]+" "+str(locptr)+"\n")
				

			# elif(ifOpcode(arr[0]) and arr[0] == "STP"):
			# 	break

			locptr += 1

	f1.close()

	


	




