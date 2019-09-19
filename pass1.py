def pass1(file,):
	locptr = 0
	f = open("input.txt","r")
	
	for x in f:
		instr = x.readline()
		arr = list(instr.split(" "))
		if(ifLabel(arr[0]) and ifOpcode(arr[1])):
			add_toSymbTable(arr[0],locptr)

		elif(ifOpcode(arr[0]) and arr[0] == "INP"):
			add_toSymbTable(arr[1],locptr)

		locptr += 1

	f.close()


	




