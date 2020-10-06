#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "AM":
        return ("0" + str(int(s[:2]) % 12) + s[2:8])[-8:]
    else:
        return ("0" + str((int(s[:2]) % 12) + 12) + s[2:8])[-8:]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

