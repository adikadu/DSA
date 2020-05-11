def selection(a):
	for i in range(len(a)-1):
		print(a)
		s = i
		up=0
		for j in range(i+1, len(a)):
			if a[s]>a[j]:
				s = j
				up = 1
		if up:
			a[i] ^= a[s]
			a[s] ^= a[i]
			a[i] ^= a[s]

	print(a)

x = [int(i) for i in input().split(" ")]
selection(x)

