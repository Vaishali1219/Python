# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:34:17 2019

@author: vaish
"""

a = input('a: ')
a = int(a)
b = input('b: ')
b = int(b)
c = input('c: ')
c = int(c)
print("The maximum is ", end="")
if (b < a) and (a > c):
    print(a)
elif (a < b) and (b > c):
    print(b)
elif (a < c) and (c > b):
    print(c)
    
