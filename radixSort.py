def counting(a, r):
	dt = {i:[] for i in range(10)}
	for j in a:
		dt[(j//int(pow(10, r)))%10].append(j)
	a.clear()
	for j in range(10):
		for k in dt[j]:
			a.append(k)
	return a


def radixSort(a, pl):
	l = len(a)
	if l==1: return a
	for i in range(pl):
		a = counting(a, i)
	return a

# print(counting([22,21,1], 0))
print(radixSort([int(i) for i in input("input array: ").split(" ")], int(input("input radix: "))))
