from Opcode import *
from SymbolTable import *

labels = list()
def pass1():
	locptr = 0
	arr = list()
	error = False
	stp = False
	
	with open("input.txt","r") as f:
		for x in f:
			x = x.strip("\n")
			arr = x.split(' ')
			# print(arr)
			st = ""

			if len(arr) == 1 and arr[0] == st:
				print("Error: Line is Blank"+"( at: "+str(locptr)+")")
				error = True
				continue

			if (st in arr) and len(arr)>1 and arr[-1] != "":
				print("Error: Extra white space between Opcodes/Variables"+"( at: "+str(locptr)+")")
				error = True
				continue

			if len(arr) == 1 and ifLabel(arr[0]):
				print("Error: Label defined does not point to any instruction"+"( at: "+str(locptr)+")")

			if len(arr) == 1 and ifOpcode(arr[0]):
				if check(arr[0]):
					if arr[0] == "STP":
						stp = True
						break
				else:
					print("Error: Arguments Missing for the given Opcode"+"( at: "+str(locptr)+")")
					error = True

			elif len(arr) >= 2 and ifOpcode(arr[0]):
				if len(arr) > 2:
					print("Error: Too many arguments"+"( at: "+str(locptr)+")")
					error = True

				elif ifVariable(arr[1]):
					addSym1(arr[1])
					if(arr[0] == "INP"):
						error = addSym(f'{locptr:08b}',arr[1])
				else:
					print("Error: Argument cannot be Opcode"+"( at: "+str(locptr)+")")
					error = True

			elif len(arr) >= 2 and ifVariable(arr[0]):
				if len(arr) == 2:
					if check(arr[1]):
						if ifLabel(arr[0]):
							labels.append(arr[0][:-1])
							#print(labels)
						error = addSym(f'{locptr:08b}',arr[0])
						if arr[1] == "STP":
							stp = True
							break
					else:
						print("Error: Opcode Missing for the given Label"+"( at: "+str(locptr)+")")
						error = True

				elif len(arr) > 2:
					if len(arr) > 3:
						print("Error: Too many arguments"+"( at: "+str(locptr)+")")
						error = True
					elif ifOpcode(arr[1]) and ifVariable(arr[2]):
						if ifLabel(arr[0]):
							labels.append(arr[0][:-1])
						if arr[2] in labels:
							print("Error: Attribute should be Variable, Label given"+"( at: "+str(locptr)+")")
						error = addSym(f'{locptr:08b}',arr[0])
						addSym1(arr[2])
						if(arr[1] == "INP"):
							error = addSym(f'{locptr:08b}',arr[2])
					else:
						if not ifOpcode(arr[1]):
							print("Error: No valid Opcode given"+"( at: "+str(locptr)+")")
							error = True

						elif ifOpcode(arr[2]):
							print("Error: Opcode cannot be given as Arguments"+"( at: "+str(locptr)+")")
							error = True

						
			else:
				print("Error: Line must have an Opcode as instruction"+"( at: "+str(locptr)+")")
				error = True

			locptr += 1

	if not stp:
		print("Error: No STP Opcode for stopping the program"+"( at: "+str(locptr)+")")
		error = True

	if (not error) and stp:
		error = writeTbl()
	#print(labels)
	return error