from Opcode import *
from pass1 import *

wr = open("output.txt","w")

def pass2():
	locptr = 0
	#print(labels)
	with open("input.txt","r") as f1:
		for x1 in f1:
			x1 = x1.strip("\n")
			arr = x1.split(' ')
			#wr.write(str(bin(locptr))+" ")

			if len(arr) == 1:
				wr.write(str(getOpcode(arr[0]))+" 00000000"+"\n")

			if len(arr) == 2 and ifVariable(arr[0]):
				wr.write(str(getOpcode(arr[1]))+" 00000000"+"\n")

			if len(arr) == 2 and ifOpcode(arr[0]):
				if (arr[0] == "BRZ" or arr[0] == "BRP" or arr[0] == "BRN") and (arr[1] not in labels):
					print("Error: Cannot branch to a variable/opcode, need label")
				wr.write(str(getOpcode(arr[0]))+" "+str(find_address(arr[1]))+"\n")

			if(len(arr) > 2):
				wr.write(str(getOpcode(arr[1]))+" "+str(find_address(arr[2]))+"\n")

			locptr += 1

def find_address(_str):
	with open("Symboltable.txt","r") as f:
		for x in f:
			x = x.strip("\n")
			arr = x.split(' ')

			if(arr[0] == _str):
				return arr[1]