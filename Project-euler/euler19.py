#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:03:35 2017

@author: itachi1793
"""

import timeit

start = timeit.default_timer()
# 1 Jan 1901 - Tuesday
days = ('mon','tue','wed','thu','fri','sat','sun')
monthsWith31 = (1,3,5,7,8,10,12)
monthswith30 = (4,6,9,11)

startingDay = 'tue'
count = 0

for year in range(1901,2001):
    for month in range(1,13):
        if month == 2 and year % 100 == 0 and year % 400 == 0:
            # feb = 29 
            indexOfStartingDay = days.index(startingDay)
            startingDay = days[(indexOfStartingDay + 1) % 7] # modules is done to wrap around the days
            
        elif month == 2 and year % 100 != 0 and year % 4 == 0:
            # feb = 29
            indexOfStartingDay = days.index(startingDay)
            startingDay = days[(indexOfStartingDay + 1) % 7] # modules is done to wrap around the days
            
        elif month == 2:
            # feb = 28
            indexOfStartingDay = days.index(startingDay)
            startingDay = days[(indexOfStartingDay + 0) % 7] # modules is done to wrap around the days
            
        elif month in monthswith30:
            # 30 days
            indexOfStartingDay = days.index(startingDay)
            startingDay = days[(indexOfStartingDay + 2) % 7] # modules is done to wrap around the days
            
        elif month in monthsWith31:
            # 31 days
            indexOfStartingDay = days.index(startingDay)
            startingDay = days[(indexOfStartingDay + 3) % 7] # modules is done to wrap around the days
            
        if startingDay == 'sun':
            count += 1

print(count)     

stop = timeit.default_timer()
print("the running time is", stop - start)