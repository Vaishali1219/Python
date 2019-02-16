# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:40:24 2019

@author: vaish
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
m = int(input("Enter the series length: "))
print(fibonacci(m))