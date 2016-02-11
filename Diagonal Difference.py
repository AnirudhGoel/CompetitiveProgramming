N = int(input())
suml = 0
sumr = 0
for x in range(0,N):
	A = list(map(int,input().split()))
	suml += A[x]
	sumr += A[N -1 - x]
print(abs(suml-sumr))