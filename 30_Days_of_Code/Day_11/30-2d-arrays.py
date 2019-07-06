#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    res = -64 # -9 * 7 -1
    for i in range((len(arr) - 2)**2):
        hg = arr[i//4 + 1][i%4 + 1]
        for j in [-1, 0, 1]:
            hg += arr[i//4    ][i%4 + j + 1]
            hg += arr[i//4 + 2][i%4 + j + 1]
        
        if hg > res:
            res = hg
    
    print(res)

