#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:45:50 2017

@author: itachi1793
"""

import timeit
import copy
start = timeit.default_timer()

with open("p067_triangle.txt") as f:
    data = f.read();
    
ip = [[int(n) for n in ln.split()]for ln in data.splitlines()]
#print(ip)

op = copy.deepcopy(ip)
for i in range(len(ip) - 2, -1, -1):
    for j in range(0, len(ip[i])):
        if op[i+1][j] > op[i+1][j+1]:
            op[i][j] += op[i+1][j]
        else:
            op[i][j] += op[i+1][j+1]

#print(np.matrix(op))
print(op[0])

stop = timeit.default_timer()
print("The runtime is ", stop - start)