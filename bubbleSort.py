def bubble(a):
	print(a)
	for i in range(len(a)):
		swapped=0
		x = 0
		for j in range(1, len(a)):
			if a[x]>a[j]:
				a[x] += a[j]
				a[j] = a[x]-a[j]
				a[x] = a[x]-a[j]
				swapped = 1
			x += 1
		if swapped == 0: break
		print(a)

x=[int(i) for i in input().split(" ")]
bubble(x)
