def palindrome(num):
    if num[::-1] == num:
       return True
    else:
       return False

T = int(input())
for x in range(0,T):
	S = input()
	P = S
	if palindrome(S) == True:
		print("-1")
	else:
		N = len(S)
		for y in range(0,N):
			if S[y] != S[N-y-1]:
				S = S[:y] + S[y+1:]
				if palindrome(S) == True:
					print(y)
					break
				else:
					print(N-y-1)
					break