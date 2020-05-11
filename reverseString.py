import re
# def reverseString(a):
# 	i=0
# 	j=len(a)-1
# 	a=list(a)
# 	while(True):
# 		if i>=j : return "".join(map(str, a)) # Converts list to string.
# 		k=a[i]
# 		a[i]=a[j]
# 		a[j]=k
# 		i+=1
# 		j-=1

# print(reverseString(input()))

def reverseString(a):
	if len(re.findall(r"\S+", a)) == 0: #check if string contains only space.
		return "Type some input bro!!!"
	return a[::-1] # reverse a string

print(reverseString(input()))