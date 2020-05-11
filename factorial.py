def Rfact(n):
	if n == 0 or n==1 : return 1
	return n*Rfact(n-1)

def Ifact(n):
	if n==0: return 1
	x = 1
	for i in range(2, n+1):
		x *= i
	return x

n=int(input())
print(Rfact(n))
print(Ifact(n))