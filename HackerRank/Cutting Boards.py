T = int(input())
for i in range (0,T):
	M = input()
	M,N = M.split()
	M = int(M)
	N = int(N)
	modu = 1000000007
	if M >= 2:
		x = list(map(int,input().split()))
	else:
		x = []
		x.extend(int(input()))
	if N >= 2:
		y = list(map(int,input().split()))
	else:
		y = []
		y.extend(int(input()))
	x.sort()
	x.reverse()
	y.sort()
	y.reverse()
	j = 0
	k = 0
	cost = 0
	segx = 1
	segy = 1
	while j < M and k < N:
		if x[j] >= y[k]:
			cost += (x[j] * segy) % modu
			segx += 1
			j += 1

		elif x[j] < y[k]:
			cost += (y[k] * segx) % modu
			segy += 1
			k += 1
	while j < M:
		cost += (x[j] * segy) % modu
		j += 1
	while k < N:
		cost += (y[k] * segx) % modu
		k += 1
	print(cost%modu)