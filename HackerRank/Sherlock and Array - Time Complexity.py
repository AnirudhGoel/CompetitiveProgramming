T = int(input())
for x in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	for i in range(0,N):
		suml = sum(A[:i])
		sumr = sum(A[i + 1:])
		if suml == sumr:
			print("YES")
			break
		elif i == N-1 and suml != sumr:
			print("NO")