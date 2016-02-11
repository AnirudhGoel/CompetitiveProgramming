T = int(input())
for x in range(0,T):
	B = input()
	B,W = B.split()
	B = int(B)
	W = int(W)
	X = input()
	X,Y,Z = X.split()
	X = int(X)
	Y = int(Y)
	Z = int(Z)

	if X > Y + Z:
		sum = (Y * W) + (B * (Y + Z))
		print(sum)

	elif Y > X + Z:
		sum = (X * B) + (W * (X + Z))
		print(sum)

	else:
		sum = (X * B) + (Y * W)
		print(sum)