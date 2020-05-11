def binary(a, e):
	l = len(a)
	# if l==1 and a[0]!=e: return -1
	m = l//2
	if a[m] == e: return m
	if e < a[m] and m<l: return binary(a[:m], e)
	elif m+1<l: return binary(a[m+1:], e)

# print(binary([int(i) for i in input().split(" ")], int(input())))
x = binary([int(i) for i in input().split(" ")], int(input()))
if x==None: print("Not Found...")
else: print("Found...")