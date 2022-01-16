C = []
total = 0
N = input()
N,K = N.split()
C = list(map(int,input().split()))
C.sort()
C.reverse()
C.extend([0] * int(K))
N = int(N)
K = int(K)
for x in range(0,N + K - (N % K)):
	if (int(x/K))%2 == 0:
		total = total + (C[x] * (int(x/K) + 1))
	else:
		total = total + (C[((int(x/K) + 1) * K) - (int(x%K)) - 1] * (int(x/K) + 1))

print(total)