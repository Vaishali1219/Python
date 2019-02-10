# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:32:20 2019

@author: vaish
"""

n = int(input('Enter a number: '))

f1 = f2 = 1
print(f1,'\t', f2,'\t', end='')

i = 2
while i < n:
    f1, f2 = f2, f1 + f2
    print(f2,'\t', end='')
    i += 1
    
print()