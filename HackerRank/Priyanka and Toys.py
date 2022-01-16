num = int(input())
skip = 0
W = list(map(int, input().split()))

W.sort()

temp = W[0]
buy = 1

for x in W[1:]:
	if x - temp > 4:
		buy += 1
		temp = x

print(buy)