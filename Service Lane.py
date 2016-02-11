N = input()
N,T = N.split()
N = int(N)
T = int(T)
width = list(map(int,input().split()))
for x in range(0,T):
	i = input()
	i,j = i.split()
	i = int(i)
	j = int(j)
	min = width[i]
	for p in range(i,j+1):
		if width[p] < min:
			min = width[p]

	print(min)