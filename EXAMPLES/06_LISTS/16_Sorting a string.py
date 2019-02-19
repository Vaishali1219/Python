# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:54:31 2019

@author: vaish
"""

s = input("Enter a string: ")
w = s.split()
q = len(w)

for i in range(q - 1):
    for j in range(q - 1 - i):
        if len(w[j]) > len(w[j + 1]):
            w[j], w[j + 1] = w[j + 1], w[j]
            
print(' '.join(w))