# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:45:36 2019

@author: vaish
"""

a = input('a: ')
a = int(a)
b = input('b: ')
b = int(b)
#c = input('c: ')
#c = int(c)
if a % b == 0:
    print("yes")
else:
    print("No")
    print("The remainder is ",a % b)
    