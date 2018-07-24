def solve(n, s, d, m):
	if m > n:
		return 0
	else:
		return len([1 for i in range(n) if i + m <= n and sum(s[i:i + m]) == d])


if __name__ == '__main__':
	n = int(input().strip())
	s = list(map(int, input().strip().split(' ')))
	d, m = map(int, input().strip().split(' '))
	print(solve(n, s, d, m))
