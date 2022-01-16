T = int(input())
for x in range(0,T):
	A = input()
	B = input()
	C = [0] * 26
	D = [0] * 26
	p = 0
	for y in A:
			C[ord(y) - 97] += 1

	for z in B:
			D[ord(z) - 97] += 1

	for w in range(0,26):
		if C[w]>0 and D[w]>0:
			p += 1
			break

	if p > 0:
		print("YES")
	elif p==0:
		print("NO")