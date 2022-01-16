N = int(input())
for x in range(1,N+1):
	for j in range(0,N-x):
		print(" ", end="")
	for p in range(0,x-1):
		print("#",end="")
	print("#")