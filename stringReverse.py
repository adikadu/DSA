def esr(a):
	if not a: return
	esr(a[1:])
	print(a[0], end="")

esr(input())
print()