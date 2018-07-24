def lcp(string1, string2):
	inc = 0
	o = 0
	for i in range(len(string1)):
		if string1[i] == string2[i]:
			inc += 1
		else:
			o = inc
			return o
	return inc


def create_fruit(string):
	li = []
	for i in range(len(string)):
		li.append(string[i:])
	return (sorted(li))


def func(string):
	li = create_fruit(string)
	ans = len(li[0])
	for i in li[1:]:
		ans += len(i) - lcp(li[li.index(i) - 1], i)
	print(ans)


if __name__ == '__main__':
	n,q = input().strip().split(' ')
	n,q = [int(n),int(q)]
	s = input().strip()
	for a0 in range(q):
		left,right = input().strip().split(' ')
		left,right = [int(left),int(right)]
		if len(s) == 1:
			print(1)
		elif len(s) == 0:
			continue
		else:
			func(s[left:right])
