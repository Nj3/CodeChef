# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calc_divisor(num):
    """Calculates the sum of proper divisors of a number"""
    result = []

    for i in range(1, round(math.sqrt(num))+1):
        if num % i == 0:
            
            if num / i != num and num / i != i:
                result.append(i)
                result.append(int(num / i))
            else:
                result.append(i)
            
    return sum(result)

def calc_abund_num(num):
    """Calculates whether the given number is abundant or not."""
    if num < calc_divisor(num):
        # the number is abundantso return True.
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    abundant_nums = []
    abundant_sums = []
    non_abundant_sums = []
    upper_limit = 28123
    for i in range(1,upper_limit + 1):
        if calc_abund_num(i):
            abundant_nums.append(i)
    
    while upper_limit > 0:
        left = 0
        right = len(abundant_nums) - 1
        
        if upper_limit % 2 == 0 and int(upper_limit / 2) in abundant_nums:
            abundant_sums.append(upper_limit)
            upper_limit -= 1
            continue
        
        while left < right:
            if abundant_nums[left] + abundant_nums[right] == upper_limit:
                abundant_sums.append(upper_limit)
                break
            elif abundant_nums[left] + abundant_nums[right] < upper_limit:
                left += 1
            else:
                right -= 1
                
        upper_limit -= 1
    
    for j in range(1, 28124):
        if j not in abundant_sums:
            non_abundant_sums.append(j)
    
    print(sum(non_abundant_sums))

    
