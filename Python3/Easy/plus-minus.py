#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    ac = [0,0,0]
    for x in arr:
        if x > 0:
            ac[0] += 1
        elif x < 0:
            ac[1] += 1
        else:
            ac[2] += 1
    print("{}\n{}\n{}".format(ac[0]/len(arr),ac[1]/len(arr),ac[2]/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

