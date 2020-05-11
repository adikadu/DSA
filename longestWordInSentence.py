import re
def LongestWord(sen):
  a = re.findall(r"[a-zA-Z]+", sen)
  l = len(a[0])
  ind = 0
  for i in range(1, len(a)):
    if len(a[i]) > l:
      l=len(a[i])
      ind = i
  # code goes here
  return a[ind]

# keep this function call here 
print(LongestWord(input()))