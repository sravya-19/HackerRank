def getTotalX(a, b):
	step = 1
	count = 0
	for i in range(max(a), min(b) + 1, step):
		if (len([1 for x in a if i % x != 0]) == 0) and (len([1 for y in b if y % i != 0]) == 0):
			count += 1
			if step == 1:
				step = i
	return count

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
