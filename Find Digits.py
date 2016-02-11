T = int(input())
for x in range(0,T):
	N = input()
	P = int(N)
	t = 0
	for y in N:
		if int(y) != 0:
			if P % int(y) == 0:
				t += 1

	print(t)