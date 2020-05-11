def maxheapify(a, i):
	l=len(a)
	if not l or l==1: return a
	lar=i
	x = 2*i+1
	if x<l and a[x]>a[lar]: lar=x
	if x+1<l and a[x+1]>a[lar]: lar=x+1
	if lar!=i:
		a[i], a[lar] = a[lar], a[i]
		a=maxheapify(a, lar)
	return a


def buildHeap(a):
	l = len(a)
	if not l or l==1: return a
	for i in range((l-2)//2, -1, -1):
		a=maxheapify(a, i)
	return a

def heapSort(a):
	l = len(a)
	if not l or l==1: return a
	a=buildHeap(a)
	while l>=2:
		a[0], a[l-1] = a[l-1], a[0]
		l-=1
		a[:l] = maxheapify(a[:l], 0)
	return a


print(heapSort([int(i) for i in input().split(" ")]))

# 1 3 5 4 6 13 10 9 8 15 17