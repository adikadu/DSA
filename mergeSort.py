def mergeSort(a):
	if len(a)==1:
		return a
	m = (len(a))//2
	return merge(mergeSort(a[:m]), mergeSort(a[m:]))



def merge(x, y):
	z=[]
	lx=len(x)
	ly=len(y)
	i=0
	j=0
	while i<lx and j<ly:
		if x[i]<y[j]:
			z.append(x[i])
			i+=1
		elif x[i]>y[j]:
			z.append(y[j])
			j+=1
		else:
			z.append(x[i])
			i+=1
			z.append(y[j])
			j+=1
	
	while i<lx:
		z.append(x[i])
		i+=1

	while j<ly:
		z.append(y[j])
		j+=1

	return z

print(mergeSort([int(i) for i in input().split(" ")]))
# print(merge([2], [1]))

