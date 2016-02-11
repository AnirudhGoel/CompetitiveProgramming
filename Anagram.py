T = int(input())
for x in range(0,T):
	S = input()
	N = len(S)
	A = [0] * 26
	B = [0] * 26
	p = 0
	if N%2 == 1:
		print("-1")
	else:
		for y in range(0,int(N/2)):
			A[ord(S[y]) - 97] += 1

		for z in range(int(N/2),N):
			B[ord(S[z]) - 97] += 1

		for w in range(0,26):
			p = p + abs(A[w] - B[w])

		print(int(p/2))