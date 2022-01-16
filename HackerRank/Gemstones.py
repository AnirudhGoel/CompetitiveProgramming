N = int(input())
P = ['A'] * N
l = 0
for x in range(0,N):
	P[x] = input()

A = [0] * 150

for y in range(0,N):
	for q in P[y]:
		if A[ord(q)] == y:
			A[ord(q)] = A[ord(q)] + 1

for z in range(97,123):
	if A[z] == N:
		l = l + 1

print(l)