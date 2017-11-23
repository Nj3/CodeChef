#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:01:21 2017

@author: itachi1793
"""

"""
Number of the lattice paths is given by the central binomail co-efficients.

it is calculated by (2n)!/(n!*n!)
"""

import math

n = 20

value = math.factorial(2 * n) / (math.factorial(n) * math.factorial(n))

print(value)