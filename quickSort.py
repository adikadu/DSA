def quickSort(a):
	l = len(a)
	if not l or l == 1: return a
	p=a[l-1]
	j=0
	i=j-1
	while j<l-1:
		if a[j]<p:
			i+=1
			a[j], a[i] = a[i], a[j]
		j+=1
	a[i+1], a[l-1] = a[l-1], a[i+1]

	x = quickSort(a[:i+1])
	y = quickSort(a[i+2:]) if i+2<l else []
	return x + [a[i+1]] + y

print(quickSort([int(i) for i in input().split(" ")]))