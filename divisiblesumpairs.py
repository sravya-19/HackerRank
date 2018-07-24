def div_sum(n, a, k):
	a = sorted(a)
	count = 0
	print(len([1 for i in range(n - 1, 0, -1)for j in range(i)if (a[i] + a[j]) % k == 0]))

if __name__ == '__main__':
	n, k = map(int, input().strip().split(' '))
	a = list(map(int, input().strip().split(' ')))
	div_sum(n, a, k)
