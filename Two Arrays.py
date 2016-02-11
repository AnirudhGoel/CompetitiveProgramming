T = int(input())
for x in range(0,T):
	A = []
	N = input()
	N,K = N.split()
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	A.sort()
	B.sort()
	B.reverse()
	for y in range(0,int(N)):
		if A[y] + B[y] < int(K):
			print("NO")
			break
		elif y == int(N)-1 and A[y] + B[y] >= int(K):
			print("YES")