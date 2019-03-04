# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:50:29 2019

@author: vaish
"""

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']

c = {}

for i in range(len(a)):
    c[b[i]] = a[i]
    
#or just
#c = dict(zip(b, a))
    
print(c)