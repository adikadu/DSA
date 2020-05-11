cal = {}
def DPfibo(n, m):
	if n<0: return "n should be greater than zero..."
	cal[0] = 0
	if n>=2: cal[1] = 1
	if n-1 in cal: return cal[n-1]
	x = DPfibo(n-1, m) + DPfibo(n-2, m)
	cal[n-1] = x
	return x

x=int(input())
DPfibo(x, x)
for i in range(x-1):
	print(cal[i], end=" ")
print(cal[x-1])