def firstRec(arr):
	x = dict()
	for i in range(len(arr)):
		if arr[i] in x:
			if x[arr[i]][0] == 1:
				x[arr[i]][0] = 2
				x[arr[i]][1] = i

		else:
			x[arr[i]] = [1, i]
	# print(x)
	idx = -1
	for i in x:
		if x[i][0] == 2:
			if idx == -1:
				idx = i
			else:
				if x[i][1]<x[idx][1]:
					idx = i
	return(idx)

print(firstRec([2,3,4,5]))

# [2,1,1,2,3,5,1,2,4]
# [2,5,1,2,3,5,1,2,4]
