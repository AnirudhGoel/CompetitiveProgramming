T = int(input())
for x in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	left_index = 0
	right_index = N - 1
	left_sum = 0
	right_sum = 0
	while left_index < right_index:
		if left_sum < right_sum:
			left_sum += A[left_index]
			left_index += 1
		else:
			right_sum += A[right_index]
			right_index -= 1
	if left_sum == right_sum:
		print("YES")
	else:
		print("NO")