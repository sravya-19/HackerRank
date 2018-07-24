#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	total = 0
	valley = 0
	for ch in s:
		total = total + 1 if ch == 'U' else total - 1
		valley = valley + 1 if (total == 0 and ch == 'U') else valley
	return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
