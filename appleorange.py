#!/bin/python3

import sys


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) + a for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) + b for orange_temp in input().strip().split(' ')]
app_count = len([x for x in apple if x >= s and x <= t])
orange_count = len([i for i in orange if i >= s and i <= t])
print(app_count, orange_count, sep='\n')
