t = int(input())
for i in range(t):
	size = int(input())
	a = list(map(int, input().split(' ')))
	b = list(map(int, input().split(' ')))
	answer = None
	for i in range(size):
		start = i
		end = size - 1
		while start <= end:
			if start < i:
				break
			mid = (start + end) // 2
			if b[mid] < a[i]:
				end = mid - 1
			elif b[mid] >= a[i]:
				monk = mid - i
				if answer is None:
					answer = monk
				elif answer < monk:
					answer = monk
				start = mid + 1

	print(answer)
