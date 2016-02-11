T = int(input())
for x in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	for i in range(0,N):
		suml = 0
		for j in range(0,N):
			if j < i:
				suml = suml + A[j]
			elif j > i:
				suml = suml - A[j]
		if suml == 0:
			print("YES")
			break
		elif i == N-1 and suml != 0:
			print("NO")