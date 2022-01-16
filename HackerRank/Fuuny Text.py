T = int(input())
for x in range(0,T):
	S = input()
	N = len(S)
	i = 1
	c = 0
	for i in range(1,N):
		if abs(ord(S[i])-ord(S[i-1])) == abs(ord(S[N-i])-ord(S[N-i-1])):
			c = c + 1
			if c == N-1:
				print("Funny")
		else:
			print("Not Funny")
			break