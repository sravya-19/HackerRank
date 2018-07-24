#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(x - z) == abs(y - z):
        return 'Mouse C'
    else:
        return 'Cat A' if abs(z - x) < abs(z - y) else 'Cat B'
    

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        x,y, z = map(int,input().split())

        result = catAndMouse(x, y, z)

        print(result)