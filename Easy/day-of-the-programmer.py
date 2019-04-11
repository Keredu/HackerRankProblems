#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    def leap(year):
        if year < 1918 and year%4 == 0:
            return 1
        elif year >= 1918 and ((year%400 == 0) or (year%4 == 0and not year%100 == 0)):
            return 1
        return 0
    if not year == 1918:
        return str(13-leap(year))+".09."+str(year)
    else:
        return "26.09.1918"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

