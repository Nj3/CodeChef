#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:27:40 2017

@author: itachi1793
"""

import timeit

start = timeit.default_timer()

numDict = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
           6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10: 'ten',
           11 : 'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
           15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
           19: 'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
           60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
        }

sum = 0
for i in range(1,1001):
    if i <= 20:
        word = numDict[i]
    elif i == 1000:
        word = 'oneThousand'
    else:
        temp = i
        wordMk = []
        j = 0
        while temp != 0:
            digit = int(temp % 10)
            numChk = (11,12, 13, 14 ,15 ,16, 17, 18, 19)
            # units place
            if j == 0 and digit != 0 and temp % 100 not in numChk:
                wordMk.append(numDict[digit])
            # handling 11-19    
            elif j == 0 and digit != 0 and temp % 100 in numChk:
                wordMk.append(numDict[temp % 100])
            # ten's place
            elif j == 1 and digit != 0 and digit != 1:
                wordMk.append(numDict[digit * 10])
            elif j == 1 and digit == 1 and not wordMk:
                wordMk.append(numDict[10])
            # hundredth place
            elif j == 2 and digit != 0 and not wordMk:
                wordMk.append(numDict[digit] + 'Hundred')
            elif j == 2 and digit != 0 and wordMk:
                wordMk.append(numDict[digit] + 'HundredAnd')
                
            j += 1
            temp = int(temp / 10)
        wordMk = wordMk[::-1]
        word = ''.join(wordMk)
    print(word, end='\n')
        
    sum += len(word)

print(sum)

stop = timeit.default_timer()
print('the program ran for ', stop - start)