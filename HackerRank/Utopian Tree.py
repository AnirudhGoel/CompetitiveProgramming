T = int(input())
for x in range(0,T):
	N = int(input())
	Q = int(N / 2)
	R = N % 2
	height = 1
	
	for y in range(0,Q):
		height = (height * 2) + 1

	if R == 1:
		height = height * 2

	print(height)