# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:16:40 2019

@author: vaish
"""

from random import *

def search(lis, item):
    mid = len(lis) // 2
    low = 0
    high = len(lis) - 1
    while lis[mid] != item and low <= high:
        if item > lis[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return None
    else:
        return mid
    
a = []
for i in range(10):
    a.append(randint(1, 20))
a.sort()
print(a)

value = int(input("Enter the number you are searching: "))

print()
print(search(a, value))