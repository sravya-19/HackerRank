#!/bin/python3

import math
import os
import random
import re
import sys


def minimumBribes(q):
	tot = 0
	for i in range(len(q)):
		b = abs(i + 1 - q[i])
		if b > 2:
			print('Too chaotic')
			return
		else:
			if (q[i] > i + 1):
				tot += b
	print(tot)


if __name__ == '__main__':
	t = int(input())

	for t_itr in range(t):
		n = int(input())

		q = list(map(int, input().rstrip().split()))

		minimumBribes(q)
