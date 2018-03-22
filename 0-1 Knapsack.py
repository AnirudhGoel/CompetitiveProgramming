T = int(input())

for x in range(0, T):
	N = int(input())
	W = int(input())
	val = list(map(int, input().split()))
	wt = list(map(int, input().split()))

	K = [[0 for p in range(W+1)] for q in range(N+1)]

	for n in range(N + 1):
		for w in range(W + 1):
			if n == 0 or w == 0:
				K[n][w] = 0

			elif wt[n - 1] <= w:
				K[n][w] = max(val[n - 1] + K[n - 1][w - wt[n - 1]], K[n - 1][w])

			else:
				K[n][w] = K[n - 1][w]

	print(K[N][W])