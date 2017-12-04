#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:38:20 2017

@author: itachi1793
"""

def memoization(fn):
    fact_dict = {}
    def fact_storage(n):
        if n not in fact_dict:
            fact_dict[n] = fn(n)
        return fact_dict[n]
    return fact_storage

@memoization
def fact(n):
    # first check whether n < 0
    if n < 0:
        raise ValueError("Not possible to calculate factorialf or a negative integer")
    elif n >= 1:
        return n * fact(n-1)
    else:
        return 1
    
n = 100
ans = fact(n)
res = [int(i) for i in str(ans)]
sum = 0
for i in res:
    sum += i

print(sum)