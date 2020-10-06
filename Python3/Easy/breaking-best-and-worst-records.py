#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maximum = scores[0]
    minimum = scores[0]
    ac = [0,0]
    for score in scores[1:]:
        if score > maximum:
            ac[0] +=1
            maximum = score
        elif score < minimum:
            minimum = score
            ac[1] +=1
    return ac

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

