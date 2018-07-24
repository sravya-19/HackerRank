#!/bin/python3

import os
import sys
from itertools import *

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
   x = [sum(i)  for i in product(keyboards, drives) if sum(i) <= b]
   x = sorted(x, reverse=True)
   return x[0] if len(x) >= 1 else -1
	#
	# Write your code here.
	#

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	bnm = input().split()

	b = int(bnm[0])

	n = int(bnm[1])

	m = int(bnm[2])

	keyboards = list(map(int, input().rstrip().split()))

	drives = list(map(int, input().rstrip().split()))

	#
	# The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
	#

	moneySpent = getMoneySpent(keyboards, drives, b)

	fptr.write(str(moneySpent) + '\n')

	fptr.close()
