l1 = input()
l2 = input()
l3=[]

def conv(x):
	if x!="": return int(x)


try:
	l1 = list(map(conv, l1.split(", ")))
	l2 = list(map(conv, l2.split(", ")))
	if(l1[0] == None):
		l1=[]
	if(l2[0] == None):
		l2=[]
	i=0
	j=0

	k=len(l1)
	l=len(l2)
	while(True):
		if(i<k and j<l):
			if(l1[i]<l2[j]):
				l3.append(l1[i])
				i+=1
			elif(l2[j]<l1[i]):
				l3.append(l2[j])
				j+=1
			else:
				l3.append(l1[i])
				i+=1
				l3.append(l2[j])
				j+=1
		elif(j==l and i<k):
			while(i<k):
				l3.append(l1[i])
				i+=1
		elif(i==k and j<l):
			while(j<l):
				l3.append(l2[j])
				j+=1
		else: break
	print(l3)
except:
	print("invalid input...")