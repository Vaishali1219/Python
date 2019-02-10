# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:28:17 2019

@author: vaish
"""

n = int(input("Enter the number: "))

fact = 1

while n > 1:
    fact *= n
    n -= 1
print(fact)