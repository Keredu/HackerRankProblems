#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = (n-1)//3
    j = (n-1)//5
    k = (n-1)//15
    print((3*i*(i+1) + 5*j*(j+1) - 15*k*(k+1))//2)
