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
						break
				else:
					print("Error: Arguments Missing for the given Opcode\n")

			elif len(arr) >= 2 and ifOpcode(arr[0]):
				if len(arr) > 2:
					print("Error: Too many arguments")

				elif ifLabel(arr[1]):
					addSym1(arr[1])
					if(arr[0] == "INP"):
						addSym(locptr,arr[1])
				else:
					print("Error: Argument cannot be Opcode")

			elif len(arr) >= 2 and ifLabel(arr[0]):
				if len(arr) == 2:
					if check(arr[1]):
						addSym(locptr,arr[0])
					else:
						print("Error: Arguments Missing for the given Opcode")

				elif len(arr) > 2:
					if len(arr) > 3:
						print("Error: Too many arguments")
					elif ifOpcode(arr[1]) and ifLabel(arr[2]):
						addSym(locptr,arr[0])
						addSym1(arr[2])
						if(arr[1] == "INP"):
							addSym(locptr,arr[2])
					else:
						print("Error:")
			else:
				print("Error: Line must have an Opcode as instruction\n")
			
			# if(len(arr)>1 and ifLabel(arr[0]) and ifOpcode(arr[1])):
			# 	f1.write(arr[0]+" "+str(locptr)+"\n")
				

			# elif(len(arr)>1 and ifOpcode(arr[0]) and arr[0] == "INP"):
			# 	f1.write(arr[1]+" "+str(locptr)+"\n")
				

			# elif(ifOpcode(arr[0]) and arr[0] == "STP"):
			# 	break

			locptr += 1
	
	writeTbl()