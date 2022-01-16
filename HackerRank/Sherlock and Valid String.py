import sys
S = input()
A = [0] * 26
for x in S:
	A[ord(x)-97] += 1

small = 100000
p = 0
gr = 0
one = 0

for y in range(0,26):
	if A[y] == 1:
		one += 1

	if A[y] > 1:
		gr += 1

	if one > 1 and gr > 1:
		print("NO")
		sys.exit()

	if A[y] < small and A[y] != 0:
		small = A[y]

if one == 1:
	print("YES")
	sys.exit()

for u in range(0,26):
	if A[u] != 0:
		p += abs(small - A[u])
		if p > 1:
			print("NO")
			break

if p == 0 or p == 1:
	print("YES")