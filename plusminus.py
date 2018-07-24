import time
start = time.time()
@profile
def plus_minus():
	n = int(input().strip())
	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	neg_count = 0
	pos_count = 0
	for i in range(n):
		if arr[i] < 0:
			neg_count += 1
		elif arr[i] > 0:
			pos_count += 1
	neg_count = neg_count / n
	pos_count = pos_count / n
	print(pos_count, neg_count, 1 - neg_count - pos_count, sep='\n')


if __name__ == '__main__':
	plus_minus()
end = time.time()
print('time = ', end - start)
