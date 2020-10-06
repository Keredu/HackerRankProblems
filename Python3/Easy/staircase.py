#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    s = ""
    for i in range(1,n):
        s += " "*(n-i) + "#"*i + "\n"
    print(s+"#"*n)
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)

