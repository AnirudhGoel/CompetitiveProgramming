a = list(map(int,input().split()))
e = list(map(int,input().split()))
if a[2] > e[2]:
	print(10000)
elif a[2] == e[2]:
	if a[1] > e[1]:
		print(500 * (abs(a[1] - e[1])))
	elif a[1] == e[1]:
		if a[0] > e[0]:
			print(15 * (abs(a[0] - e[0])))
		else:
			print(0)
	else:
		print(0)
else:
	print(0)
