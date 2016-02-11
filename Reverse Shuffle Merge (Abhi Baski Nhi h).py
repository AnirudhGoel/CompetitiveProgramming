T = input()
A = [0] * 26
F = []
for x in range(len(T)):
	A[ord(T[x]) - 97] += 1
for x in range(26):
	F.extend([chr(x + 97)] * int(A[x] / 2))
print(''.join(F))