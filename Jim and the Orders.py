N = int(input())
A = []
B = []
C = []
NC = []
for x in range(0,N):
	l = input() #take input as string
	l,d=l.split() #split input
	A.append(int(l))
	B.append(int(d))
	C.append([A[x] + B[x], x + 1])

NC = sorted(C,key=lambda x: x[0])

for p in NC:
	print(p[1], end = " ")