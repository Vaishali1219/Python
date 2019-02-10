# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:46:15 2019

@author: vaish
"""

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
        
gcd = a + b
print(gcd)