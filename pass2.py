from Opcode import *

wr = open("output.txt","a")

def pass2():
	locptr = 0

	with open("input.txt","r") as f1:
		for x1 in f1:
			x1 = x1.strip("\n")
			arr = x1.split(' ')
			wr.write(str(locptr)+" ")

			if len(arr) == 1:
				wr.write(str(getOpcode(arr[0]))+"\n")

			if len(arr) == 2 and ifLabel(arr[0]):
				wr.write(str(getOpcode(arr[1]))+"\n")

			if len(arr) == 2 and ifOpcode(arr[0]):
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