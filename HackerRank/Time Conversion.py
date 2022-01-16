T = input()
if T[8] == 'A':
	if T[0] == '1' and T[1] == '2':
		print("00",end="")
		print(T[2:8])
	else:
		print(T[:8])
elif T[8] == 'P':
	if T[0] == '1' and T[1] == '2':
		print(T[:8])
	else:
		A = int(T[0])
		B = int(T[1])
		A += 1
		B += 2
		print(A,end="")
		print(B,end="")
		print(T[2:8])