N = int(input())
arr = list(map(int,input().split()))
num = arr[N-1]
for x in range(N-2,-1,-1):
	if num < arr[x]:
		arr[x+1] = arr[x]
		for y in range(0,N-1):
			print(arr[y],end=" ")
		print(arr[N-1])
	
	else:
		arr[x+1] = num
		for y in range(0,N-1):
			print(arr[y],end=" ")
		print(arr[N-1])
		break

	if x == 0 and num < arr[0]:
		arr[0] = num
		for y in range(0,N-1):
			print(arr[y],end=" ")
		print(arr[N-1])