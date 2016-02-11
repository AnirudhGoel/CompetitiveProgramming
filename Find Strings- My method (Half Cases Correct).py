S = []
P = []
B = []
N = int(raw_input())
for x in range(0,N):
	S.append(raw_input())

for y in S:
	length = len(y)
	for i in range(0,length):
		for j in range(i,length):
			P.append(y[i:j + 1])

P.sort()
l = len(P)
z = 1
while z < l:
	if P[z] == P[z-1]:
		P = P[:z] + P[z+1:]
		l -= 1
	if P[z] != P[z-1]:
		z += 1

q = int(raw_input())
for k in range(0,q):
	B.append(int(raw_input()))
	
	if B[k] > len(P) or B[k] < 0:
		print "INVALID"
	else:
		print P[B[k]-1]