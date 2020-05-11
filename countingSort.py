def counting(ll, rl, a):
	if ll>rl: return "lower limit exceeds higher limit..."
	l = len(a)
	if l == 1:
		if a[0]<ll or a[0]>rl: return "list index out of the given range..."
		return a
	z = dict()
	for i in a:
		if i<ll or i>rl: return "list index out of the given range..."
		elif i in z: z[i]+=1
		else: z[i]=1
	ww=list(z.keys())
	ww.sort()
	a.clear()
	for x in ww:
		for i in range(0, z[x]):
			a.append(x)

	return a

print(counting(int(input("enter lower limit: ")), int(input("enter higher limit: ")), [int(i) for i in input("enter array to sort: ").split(" ")]))

