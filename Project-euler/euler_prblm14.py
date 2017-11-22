#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:41:22 2017

@author: itachi1793
"""
import math
import timeit

start = timeit.default_timer()
# necessary variables
limit = 1000000
longestChainNum = 1
longestChainCount = 0
collatzChain = {}
# optimize first by memeoization
# then by powers of 2. i.e, if ever encountered a num which is a power of 2, 
# then no need to recursively go down . if we get the power value , incrmeent count by
# that number.
  
def collatz(i, tempCount):
    # Base condition
    if i == 1:
        return tempCount + 1
    # Check whether it's already there in dictionary
    elif i in collatzChain.keys():
        return tempCount + collatzChain[i]
    # check for powers of 2
    elif ( int(i) & int(i - 1) ) == 0:
        return tempCount + int(math.log(i, 2)) + 1
    # check for even
    elif i % 2 == 0:
        tempCount = tempCount + 1
        return collatz( int(i / 2), tempCount)
    # check for odd
    elif i % 2 != 0:
        tempCount = tempCount + 1
        return collatz( int((3 * i) + 1), tempCount )
    
for i in range(1, limit + 1):
    tempCount = 0
    count = collatz(i, tempCount)
    
    if i not in collatzChain.keys():
        collatzChain[i] = count
        
#    print(i, count)
    if count > longestChainCount:
        longestChainCount = count
        longestChainNum = i
print("the winnner is")
print(longestChainNum, longestChainCount)

stop = timeit.default_timer()

print('runtime is - ', stop - start)