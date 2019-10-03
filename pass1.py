from Opcode import *
from SymbolTable import *

def pass1():
	locptr = 0
	arr = list()
	error = False
	stp = False
	
	with open("input.txt","r") as f:
		for x in f:
			x = x.strip("\n")
			arr = x.split(' ')

			if len(arr) == 1 and ifOpcode(arr[0]):
				if check(arr[0]):
					if arr[0] == "STP":
						stp = True
						break
				else:
					print("Error: Arguments Missing for the given Opcode\n")
					error = True

			elif len(arr) >= 2 and ifOpcode(arr[0]):
				if len(arr) > 2:
					print("Error: Too many arguments")
					error = True

				elif ifLabel(arr[1]):
					addSym1(arr[1])
					if(arr[0] == "INP"):
						error = addSym(bin(locptr),arr[1])
				else:
					print("Error: Argument cannot be Opcode")
					error = True

			elif len(arr) >= 2 and ifLabel(arr[0]):
				if len(arr) == 2:
					if check(arr[1]):
						error = addSym(bin(locptr),arr[0])
					else:
						print("Error: Arguments Missing for the given Opcode")
						error = True

				elif len(arr) > 2:
					if len(arr) > 3:
						print("Error: Too many arguments")
						error = True
					elif ifOpcode(arr[1]) and ifLabel(arr[2]):
						error = addSym(bin(locptr),arr[0])
						addSym1(arr[2])
						if(arr[1] == "INP"):
							error = addSym(bin(locptr),arr[2])
					else:
						if not ifOpcode(arr[1]):
							print("Error: No valid Opcode given")
							error = True

						elif ifOpcode(arr[2]):
							print("Error: Opcode cannot be given as Arguments")
							error = True

						
			else:
				print("Error: Line must have an Opcode as instruction\n")
				error = True

			locptr += 1

	if stp:
		print("Error: No STP Opcode for stopping the program\n")
		error = True

	if (not error) and stp:
		error = writeTbl()

	return error