def conti_maxi(A):
	current_index = -1
	current_sum = 0
	best_start_index = -1
	best_end_index = -1
	best_sum = 0

	for i in range(0,len(A)):
		val = current_sum + A[i]
		if val > 0:
			if current_sum == 0:
				current_index = i
			current_sum = val
		else:
			current_sum = 0

		if current_sum > best_sum:
			best_start_index = current_index
			best_end_index = i
			best_sum = current_sum

	return best_sum

def noncont(A):
	plus = 0
	for i in A:
		if i >= 0:
			plus += i
	return plus

def check_positive(A):
	n = 0
	for i in range(0,len(A)):
		if A[i] >= 0:
			n += 1
	if n == len(A):
		return sum(A)
	else:
		return 0

def check_negative(A):
	n = 0
	for i in range(0,len(A)):
		if A[i] <= 0:
			n += 1
	if n == len(A):
		return max(A)
	else:
		return 1


T = int(input())
for x in range(0,T):
	N = int(input())
	A = list(map(int,input().split()))
	add = check_positive(A)
	neg = check_negative(A)
	if add != 0:
		print(add,end=" ")
		print(add)
	elif neg != 1:
		print(neg,end=" ")
		print(neg)
	else:
		print(conti_maxi(A),end=" ")
		print(noncont(A))