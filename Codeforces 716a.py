p = 0
n = input()
n,c = n.split()
n = int(n)
c = int(c)
t = list(map(int, input().split()))
t.reverse()
for x in range(0,n-1):
	if t[x] - t[x+1] <= c:
		p = p + 1
	else:
		break
print(p+1)