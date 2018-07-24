@profile
def print_ans(li):
	li.sort()
	sum_list = sum(li)
	print(sum_list - li[-1], sum_list - li[0])


if __name__ == '__main__':
	lis = list(map(int, input().split()))
	print_ans(lis)
