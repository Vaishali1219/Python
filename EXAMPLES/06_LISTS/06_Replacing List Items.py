# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:33:51 2019

@author: vaish
"""

array = [10, -15, 3, 8, 0, 9, -6]
print(array)
print()

for i in range(len(array)):
    if array[i] >= 0:
        array[i] = 1
    elif array[i] < 0:
        array[i] = -1
        
print(array)