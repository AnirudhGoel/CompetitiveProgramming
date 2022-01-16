N = int(input())
a = list(map(int,input().split()))
l = 0
while N-l > 0:
	min = 1001
	l = 0
	for x in range(0,N):
		if a[x] < min and a[x] != 0:
			min = a[x]
	for x in range(0,N):
		if a[x] == 0:
			l += 1
		else:
			a[x] -= min
	if N-l != 0:
		print(N-l)