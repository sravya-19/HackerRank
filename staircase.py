@profile
def print_pattern(lines):
	ch = '#'
	for i in range(1, lines + 1):
		print((ch * i).rjust(lines, ' '))


if __name__ == '__main__':
	num = int(input())
	print_pattern(num)
