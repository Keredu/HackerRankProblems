#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    l1 = []
    l2 = []
    for a in arr:
        if a in l1:
            i = l1.index(a)
            l2[i] += 1
        else:
            l1.append(a)
            l2.append(1)
    return sum(b for b in sorted(l2)[:-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

