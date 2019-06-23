#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    r = []
    for e in a:
        ac = [e]
        for e2 in a:
            b = True
            for k in ac:
                if abs(k-e2) > 1:
                    b = False
            if b:
                ac.append(e2)
        if len(ac) > len(r):
            r = ac
    return len(r) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

