#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
	max_turns = (n - 1) // 2 if n % 2 != 0 else n //2
	num = (p - 1) / 2 if p % 2 != 0 else p / 2
	return num if num < max_turns - num else  num < max_turns - num 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
