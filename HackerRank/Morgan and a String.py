T = int(input())
for x in range(T):
	A = input()
	B = input()
	index_A = 0
	index_B = 0
	final = ""
	len_A = len(A)
	len_B = len(B)
	A += 'a'
	B += 'b'
	for p in range(0,len_A + len_B):
		if ord(A[index_A]) < ord(B[index_B]):
			final += A[index_A]
			index_A += 1
		elif ord(A[index_A]) > ord(B[index_B]):
			final += B[index_B]
			index_B += 1
		else:
			n = 0
			while(ord(A[index_A]) == ord(B[index_B])):
				index_A += 1
				index_B += 1
				n += 1
			if(ord(A[index_A]) < ord(B[index_B])):
				index_A -= n
				index_B -= n
				final += A[index_A]
				index_A += 1
			elif(ord(A[index_A]) > ord(B[index_B])):
				index_A -= n
				index_B -= n
				final += B[index_B]
				index_B += 1
	print(final)