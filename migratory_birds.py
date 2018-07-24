#!/bin/python3

'''import os
import sys
import collections as c
import collections


# Complete the migratoryBirds function below.
def migratoryBirds(n, ar):
	x = c.Counter(ar).most_common()
	#os.system("cls")
	#print(x)
	#print(ar.count('3'), 'a', ar.count('1') )
	if x[0][1] == x[1][1]:
		return int(x[0][0]) if int(x[0][0]) > int(x[1][0]) else int(x[1][0])
	else:
		return int(x[0][0])
	

if __name__ == '__main__':

    n = int(input())

    ar = list(input().rstrip().split())

    result = migratoryBirds(n, ar)

    print(str(result))
'''
input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))
