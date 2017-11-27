#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:59:43 2017

@author: itachi1793
"""

import timeit
import math

start = timeit.default_timer()

value = int(math.pow(2,1000))
print(value)
v = [int(i) for i in str(value)]
tot = 0
for i in v:
    tot += i
print(tot)
stop = timeit.default_timer()

print("the program ran for ",stop - start)

