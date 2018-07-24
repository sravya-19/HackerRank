def coin_count(s, m, n):
	table = [[0] * m for i in range(n + 1)]
	for i in range(m):
		table[0][i] = 1

	for i in range(1, n + 1):
		for j in range(m):

			x = table[i - s[j]][j] if i - s[j] >= 0 else 0
			y = table[i][j - 1] if j >= 1 else 0

			table[i][j] = x + y
	return table[n][m - 1]


if __name__ == '__main__':
	amt, size = map(int, input().split(' '))
	coins = sorted(list(map(int, input().split(' '))))
	print(coin_count(coins, size, amt))
