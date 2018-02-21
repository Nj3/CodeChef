#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 07:28:28 2018

@author: itachi1793
"""
import timeit
#import copy

start = timeit.default_timer()

def insertion_sort(a):
    # Performs insertion sort
    for i in range(1,len(a)):
        j = i
        while j > 0:
            if int(a[j]) < int(a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]
            j-=1
    return a

def merge(left, right, a):
    """Merges two sublists into one by sorting.
    Use b as reference array to place the sorted elements in a"""
    i = 0
    j = 0
    k = 0
#    print("the length of each sublist is ", len(left), len(right))
    while i < len(left) and j < len(right):
#        print(i, j)
        if int(left[i]) <= int(right[j]):
#            mergedLst.append(left[i])
            a[k] = left[i]
            i += 1
        else:
#            mergedLst.append(right[j])
            a[k] = right[j]
            j += 1
        k += 1
    
    #When any elements are left in left or right sub-lists
    while i < len(left):
#        mergedLst.append(left[i])
        a[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
#        mergedLst.append(right[j])
        a[k] = right[j]
        j += 1
        k += 1
    
    return a
            

def merge_sort(a):
    """Performs merge sort recursively. Use insertion sort as base case for list
    length <= 7"""
    if len(a) <= 7:
        return insertion_sort(a)
    
    mid = int(len(a) / 2)
    left = merge_sort(a[:mid+1])
    right = merge_sort(a[mid+1:])
    sortedLst = merge(left, right, a)
    
    return sortedLst
    
def bigSorting(arr):
    # Complete this function
    result = merge_sort(arr)
    return result

if __name__ == "__main__":
    with open('input02.txt','r') as f:
        arr = []
        for line in f.readlines():
            line = line.strip('\n')
            arr.append(line)
    result = bigSorting(arr)
    print ("\n".join(map(str, result)))
    
stop = timeit.default_timer()
print("the runtime is ",stop - start)