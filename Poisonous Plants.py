N = int(input())
P = list(map(int,input().split()))
G = [P[0]]
count = 0
old = N
new = 0
while old != new:
	old = len(P)
	for x in range(1,old):
		if P[x] <= P[x-1]:
			G.append(P[x])
	if G != P:
		count += 1
	P = G
	G = [P[0]]
	new = len(P)
print(count)