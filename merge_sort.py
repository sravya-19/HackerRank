def merge_list(li1, li2):
	li3 = [0] * (len(li1) + len(li2))
	i = 0
	j = 0
	k = 0
	while i < len(li1) and j < len(li2):
		if li1[i] < li2[j]:
			li3[k] = li1[i]
			i += 1
		else:
			li3[k] = li2[j]
			j += 1
		k += 1
	while i < len(li1):
		li3[k] = li1[i]
		i += 1
		k += 1
	while j < len(li2):
		li3[k] = li2[j]
		j += 1
		k += 1
	return li3


def merge_sort(li):
	if len(li) < 2:
		return
	else:
		mid = len(li) // 2
		left = li[0:mid]
		right = li[mid:]
		merge_sort(left)
		merge_sort(right)
		li = merge_list(left, right)
	print(li)


if __name__ == '__main__':
	li = list(map(int, input().strip().split(' ')))
	merge_sort(li)
