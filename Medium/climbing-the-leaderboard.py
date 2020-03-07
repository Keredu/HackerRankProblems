#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))[::-1] + [-1]
    d = dict()
    i = 0
    for a in alice[::-1]:
        for i in range(i,len(scores)):
            if a >= scores[i]:
                d[a] = i+1
                break
    return [d[a] for a in alice]


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

