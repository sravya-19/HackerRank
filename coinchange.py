def coin_count(s, m, n):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if m <= 0 and n >= 1:
		return 0
	return coin_count(s, m - 1, n) + coin_count(s, m, n - s[m - 1])


if __name__ == '__main__':
	amt, size = map(int, input().split(' '))
	coins = sorted(list(map(int, input().split(' '))))
	print(coin_count(coins, size, amt))
