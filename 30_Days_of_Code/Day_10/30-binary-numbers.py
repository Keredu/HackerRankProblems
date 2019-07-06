#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    maximum, acum= 0, 0
    s = str(bin(n))[2:]
    for c in s:
        if c == '1':
            acum += 1
        if c == '0':
            acum = 0
        if acum > maximum:
            maximum = acum
    print(maximum)

    '''
    Other solution from https://www.geeksforgeeks.org/ :
    
    def maxConsecutiveOnes(x): 
  
    # Initialize result 
    count = 0
   
    # Count the number of iterations to 
    # reach x = 0. 
    while (x!=0): 
      
        # This operation reduces length 
        # of every sequence of 1s by one. 
        x = (x & (x << 1)) 
   
        count=count+1
      
    return count
    '''
