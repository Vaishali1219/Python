# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:31:06 2019

@author: vaish
"""

n = int(input('Enter a number: '))
n - abs(n)

count = 1
n //= 10

while n > 0:
    n //= 10
    count += 1

print(count)