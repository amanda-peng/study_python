
def fabi(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return fabi(n-1) + fabi(n-2)

for i in range(0,10):
	print(fabi(i))

