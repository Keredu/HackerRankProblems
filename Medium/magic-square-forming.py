#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
import itertools
def formingMagicSquare(s):
    def is_magic_square(p):
        cond1 = lambda x: all(sum([p[i][j] for j in range(3)]) == 15 for i in range(3)) 
        cond2 = lambda x: all(sum([p[i][j] for i in range(3)]) == 15 for j in range(3))
        cond3 = lambda x: sum(p[i][i] for i in range(3)) == 15
        cond4 = lambda x: sum(p[i][2-i] for i in range(3)) == 15
        return cond1(p) and cond2(p) and cond3(p) and cond4(p)

    def gen_magic_squares():
        perms = list(itertools.permutations(range(1,10)))
        for perm in perms:
            p = [[perm[3*j + i] for i in range(3)] for j in range(3)]
            if is_magic_square(p):
                yield p

    def cost(s, ms):
        return sum(abs(ms[i][j] - s[i][j]) for i in range(3) for j in range(3))

    return min(cost(s, magic_square) for magic_square in gen_magic_squares())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

