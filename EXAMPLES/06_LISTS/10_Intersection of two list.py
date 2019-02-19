# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:10:48 2019

@author: vaish
"""

a = [5, [1 , 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1 , 2]]
c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break
        
print(c)