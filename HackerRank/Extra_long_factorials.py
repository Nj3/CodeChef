#!/bin/python3

import sys

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
    
n = int(input().strip())
print(fact(n))