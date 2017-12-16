#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:37:55 2017

@author: itachi1793
"""
import timeit
import math

start = timeit.default_timer()

def divisors(n):
    """Returns proper divisors of number n"""
    divisor = list()
    if n == 0 or n == 1:
        return divisor
    limit = int(math.sqrt(n)) + 2
    for i in range(1,limit):
        if n % i == 0:
            divisor.append(i)
            if int(n / i) != i:
                divisor.append(int(n / i))
    divisor.remove(n)
    return divisor
"""
The runtime is 980s
def amicablePair(limit):
    numList = range(1, limit + 1)
    amiPairs = list()
    
    for a in numList:
        for b in numList:
            if a == b:
                continue
            else:
                prop_divisor_a = divisors(a)
                prop_divisor_b = divisors(b)
                d_of_a = sum(prop_divisor_a)
                d_of_b = sum(prop_divisor_b)

                if d_of_a == b and d_of_b == a:
                    if a not in amiPairs:
                        amiPairs.append(a)
                    if b not in amiPairs:
                        amiPairs.append(b)
            
    return amiPairs
"""

def amicablePair(limit):
    """Generates amicable Pair and returns the list.
    Runtime is 0.4s"""
    numList = list(range(1, limit + 1))
    amiPairs = list()
    
    while numList:
        a = numList[0]
        prop_divisor_a = divisors(a)
        d_of_a = sum(prop_divisor_a)
        b = d_of_a
        # check if b in list, if not then amicable Pair not possible.
        # Hence remove a from list
        if b not in numList:
            numList.remove(a)
            continue
        else:
            prop_divisor_b = divisors(b)
            d_of_b = sum(prop_divisor_b)
            if d_of_a == b and d_of_b == a and a != b:
                if a not in amiPairs : amiPairs.append(a)
                if b not in amiPairs : amiPairs.append(b)
                numList.remove(a)
                numList.remove(b)
            else:
                numList.remove(a)
    
    return amiPairs


print(sum(amicablePair(10000)))
stop = timeit.default_timer()
print("the run time is ", stop - start)
    
    