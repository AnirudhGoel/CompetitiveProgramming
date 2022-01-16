T = int(input())
for x in range(0,T):
	N = input()
	N,C,M = N.split()
	N = int(N)
	C = int(C)
	M = int(M)
	sum = 0
	wrap = 0
	choc = 0
	while int(N / C) + int(wrap / M) >= 1:
		choc = int(N / C)
		sum += choc
		N = int(N % C)
		wrap += choc
		sum += int(wrap / M)
		wrap = int(wrap % M) + int(wrap / M)

	print(sum)