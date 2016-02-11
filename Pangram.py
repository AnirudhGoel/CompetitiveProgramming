A = [0] * 170
S = input()
S = S.upper()
N = len(S)
x = 0
p = 0
r = 0
for x in S:
	if ord(x) == 32:
		p = p + 1
	elif A[ord(x)] == 0:
		A[ord(x)] = 1
for y in range(65,91):
	if A[y] == 1:
		r = r + 1
if r == 26:
	print("pangram")
else:
	print("not pangram")