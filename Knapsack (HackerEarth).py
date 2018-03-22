def check(p, numList):
	for w in numList:
		if p % w == 0:
			return True
			break
	return False

T = int(input())

for x in range(T):
	n, Num = list(map(int, input().split()))
	numList = list(map(int, input().split()))

	ansList = [0]

	for y in range(0,Num + 1):
		for z in range(0, len(ansList)):
			p = y - ansList[z]

			if check(p, numList):
				ansList.append(y)
				break

	print(ansList[-1])