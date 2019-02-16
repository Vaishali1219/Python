# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:25:15 2019

@author: vaish
"""

def shift(lis, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lis.append(lis.pop(0))
    else:
        for i in range(steps):
            lis.insert(0, lis.pop())
            
nums = [4 , 5, 6, 7 , 8, 9, 0]
print(nums)

shift(nums, -2)
print(nums)

shift(nums, 1)
print(nums)