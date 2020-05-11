x = [0, 1]
def Rfibo(n):
	if len(x)>n: return x[n]
	y = Rfibo(n-1)+Rfibo(n-2)
	x.append(y)
	return y

def Ifibo(n):
	print("Iterative", end=": ")
	if n<1:
		print("Invalid Input...")
		return
	if n == 1:
		print("0")
		return
	if n == 2:
		print("0, 1")
		return
	a = 0
	b = 1
	print(a, end=", ")
	print(b, end=", ")
	for i in range(2, n-1):
		t = b
		b = a+b
		a = t
		print(b, end=", ")
	print(a+b)


n = int(input())
Ifibo(n)
print("Recursive", end=": ")
if n<1: print("Invalid Input...")
else:
	if n == 1: print(x[0])
	elif n == 2:
		print(x[0], end=", ")
		print(x[1])
	else:
		Rfibo(n-1)
		for i in x[:-1]:
			print(i, end=", ")
		print(x[-1])


