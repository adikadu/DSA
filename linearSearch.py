def linear(a, e):
	if not a: return -1
	ind=[]
	for x in range(len(a)):
		if a[x] == e: ind.append(x)
	return ind

e = input("element to be found: ")
x = linear([i for i in input("search array: ").split(" ")], e)
if x == -1: print("search array is empty...")
else:
	l=len(x)
	if not l: print(e+" not found...")
	elif l==1: print(e+" is found at index: "+str(x[0]))
	else: 
		print(e+" is found at indices:", end=" ")
		for i in x[:-1]:
			print(i, end=", ")
		print(x[-1])
