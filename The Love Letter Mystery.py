def palindrome(num):
    if num[::-1] == num:
       return True
    else:
       return False

T = int(input())
for x in range(0,T):
	S = input()
	C = 0
	if palindrome(S) == True:
		print("0")
	else:
		N = len(S)
		for y in range(0,int(N/2)):
			if S[y] != S[N-y-1]:
				C += abs(ord(S[y]) - ord(S[N-y-1]))

		print(C)