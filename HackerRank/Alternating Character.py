T = int(input())
for x in range(0,T):
	S = input()
	N = len(S)
	p = 0
	for i in range(1,N):
		if S[i-1] == S[i]:
			p = p + 1
	print(p)