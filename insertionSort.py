def insert(a):
	print(a)
	for i in range(1, len(a)):
		f=0
		j=i-1
		k=j
		temp=a[i]
		while j>=0:
			if temp<a[j]:
				f=1
				a[j+1] = a[j]
				k=j
			j-=1
		if f: a[k]=temp
		print(a)

	print()
	print(a)

insert(list(int(i) for i in input().split(" ")))
